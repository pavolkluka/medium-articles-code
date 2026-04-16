# Phorpiex Twizt Botnet: A Network Traffic Analysis

**Published:** Feb 2, 2026
**Medium:** [Read article](https://themalwarefiles.com/network-traffic-analysis-detecting-phorpiex-c2-and-p2p-communications-4188d14c3471)
**Domain:** Network Traffic Analysis
**Malware family:** Phorpiex / Twizt

## Script(s)

| File | Purpose |
|------|---------|
| `shannon_entropy_calculator.py` | Calculates Shannon entropy of binary files exported from Wireshark to identify encrypted or packed payloads |

## Usage

```bash
python3 shannon_entropy_calculator.py
# Input: export-objects/195.178.136.19/1, /2, /3 (Wireshark exported objects)
```

> **Note:** File paths in the script are hardcoded to the specific C2 IP from the article's analysis.
> Modify the paths to match your exported objects directory.

## Dependencies

- Python 3 (standard library only)
