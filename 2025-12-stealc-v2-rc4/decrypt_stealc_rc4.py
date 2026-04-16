import base64
import json
import sys
import argparse
import pyshark

def rc4_crypt(key, data):
    # RC4 encryption/decryption
    S = list(range(256))
    j = 0
    key_bytes = key.encode() if isinstance(key, str) else key
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        result.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(result)

def decode_base64_field(value):
    # Decode base64 encoded field if it's a string
    if isinstance(value, str):
        try:
            # Try to decode from base64
            decoded = base64.b64decode(value).decode('utf-8', errors='ignore')
            return decoded
        except Exception:
            # If decoding fails, return original value
            return value
    return value

def extract_http_post_data(pcap_file, target_ip="91.92.240.190"):
    # Extract HTTP POST request data from PCAP file using pyshark
    # Returns list of (frame_number, http_payload) tuples
    print(f"Loading PCAP file: {pcap_file}")

    # Used pyshark to read PCAP with HTTP filter
    cap = pyshark.FileCapture(
        pcap_file,
        display_filter=f'http.request.method == POST and ip.dst == {target_ip}'
    )

    post_requests = []

    print(f"Extracting POST requests...")
    for packet in cap:
        try:
            # Get frame number
            frame_num = int(packet.frame_info.number)

            # Get HTTP file data (POST body)
            if hasattr(packet, 'http') and hasattr(packet.http, 'file_data'):
                # HTTP file_data is hex encoded string, need to convert
                http_body_hex = packet.http.file_data.replace(':', '')
                http_body = bytes.fromhex(http_body_hex)

                post_requests.append((frame_num, http_body))
                print(f"Found POST request in frame {frame_num} ({len(http_body)} bytes)")
        except Exception as e:
            print(f"Error processing packet: {e}")
            continue

    cap.close()
    return post_requests

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='StealC v2 - Decrypt all POST requests from PCAP file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -p infected/lola.pcapng -k ca0de16dff5e468f -o output.json
  %(prog)s --pcap capture.pcapng --rc4-key mykey123 --output decrypted.json
        """
    )

    parser.add_argument(
        '-p', '--pcap',
        dest='pcap_file',
        required=True,
        help='Path to PCAP/PCAPNG file to analyze'
    )

    parser.add_argument(
        '-k', '--rc4-key',
        dest='rc4_key',
        required=True,
        help='RC4 decryption key (hex string)'
    )

    parser.add_argument(
        '-o', '--output',
        dest='output_file',
        required=True,
        help='Output JSON file path for decrypted data'
    )

    parser.add_argument(
        '-t', '--target-ip',
        dest='target_ip',
        default='91.92.240.190',
        help='Target IP address to filter POST requests (default: 91.92.240.190)'
    )

    args = parser.parse_args()

    # Extract POST requests
    print("\nExtracting POST requests from PCAP...")
    print(f"PCAP file: {args.pcap_file}")
    print(f"Target IP: {args.target_ip}")
    print(f"RC4 key: {args.rc4_key}")

    post_requests = extract_http_post_data(args.pcap_file, args.target_ip)
    print(f"Found {len(post_requests)} POST requests\n")

    if not post_requests:
        print("No POST requests found!")
        return

    # Decrypt all posts
    all_decrypted = []

    for idx, (frame_num, http_body) in enumerate(post_requests, start=1):
        print(f"Decrypting POST {idx}/{len(post_requests)}: Frame {frame_num}")

        try:
            # HTTP body should be base64 encoded encrypted data
            http_body_str = http_body.decode('utf-8', errors='ignore').strip()

            # Decode Base64 and decrypt
            encrypted = base64.b64decode(http_body_str)
            decrypted = rc4_crypt(args.rc4_key, encrypted)

            # Parse JSON
            data_json = json.loads(decrypted)

            # Decode filename field if it exists
            if 'filename' in data_json:
                original_filename = data_json['filename']
                decoded_filename = decode_base64_field(original_filename)
                data_json['filename_decoded'] = decoded_filename
                print(f"Type: {data_json.get('type', 'unknown')}")
                print(f"Filename (base64): {original_filename}")
                print(f"Filename (decoded): {decoded_filename}")
            else:
                print(f"Type: {data_json.get('type', 'unknown')}")

            if 'part_index' in data_json:
                print(f"Part: {data_json['part_index']+1}/{data_json['total_parts']}")

            # Add metadata
            data_json['_metadata'] = {
                'frame_number': frame_num,
                'post_index': idx
            }

            all_decrypted.append(data_json)

        except Exception as e:
            print(f"    [!] Error: {e}")
            # Add error entry
            all_decrypted.append({
                '_metadata': {
                    'frame_number': frame_num,
                    'post_index': idx,
                    'error': str(e)
                }
            })

    # Save all decrypted posts to single JSON file
    print(f"\nSaving all decrypted posts to: {args.output_file}")
    with open(args.output_file, 'w', encoding='utf-8') as f:
        json.dump(all_decrypted, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_decrypted)} decrypted posts")
    print(f"Decryption complete!")

if __name__ == "__main__":
    main()
