# Network Traffic Analysis: Analyzing StealC V2 Infostealer with RC4

**Published:** Dec 29, 2025
**Medium:** [Read article](https://medium.com/h7w/network-traffic-analysis-how-to-analyze-stealc-version-2-infostealer-which-uses-rc4-e9f23d89aa06)
**Domain:** Network Traffic Analysis
**Malware family:** StealC V2

## Script(s)

| File | Purpose |
|------|---------|
| `decrypt_stealc_rc4.py` | Extracts HTTP POST requests from a PCAP, Base64-decodes and RC4-decrypts StealC C2 traffic, outputs structured JSON |

## Usage

```bash
python3 decrypt_stealc_rc4.py -p <pcap_file> -k <rc4_key> -o <output.json>

# Example:
python3 decrypt_stealc_rc4.py -p infected/lola.pcapng -k ca0de16dff5e468f -o output.json

# Options:
#   -p, --pcap        Path to PCAP/PCAPNG file (required)
#   -k, --rc4-key     RC4 decryption key as hex string (required)
#   -o, --output      Output JSON file path (required)
#   -t, --target-ip   Target C2 IP to filter (default: 91.92.240.190)
```

## Dependencies

- Python 3
- pyshark
