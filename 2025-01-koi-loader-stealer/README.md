# Network traffic analysis: Koi Loader/Stealer

**Published:** Jan 28, 2025
**Medium:** [Read article](https://medium.com/@pavol.kluka/network-traffic-analysis-koi-loader-stealer-2dfc4daf8b35)
**Domain:** Network Traffic Analysis
**Malware family:** Koi Loader/Stealer

## Script(s)

| File | Purpose |
|------|---------|
| `koi_loader_xor_decrypt.py` | XOR decrypts binary data from Koi Loader network traffic using a key extracted from the C2 config string |

## Usage

```bash
python3 koi_loader_xor_decrypt.py
# Output: decrypted_sd2_bindata.bin
```

> **Note:** The `bindata` array in the script is truncated. To use this script,
> extract the full binary data from TCP stream 20 of the PCAP file
> (malware-traffic-analysis.net exercise 2025-01-21) and populate the `bindata` array.

## Dependencies

- Python 3 (standard library only)
