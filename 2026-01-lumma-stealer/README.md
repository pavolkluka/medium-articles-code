# Network Traffic Analysis: Lumma Stealer & Payload Reconstruction

**Published:** Jan 12, 2026
**Medium:** [Read article](https://themalwarefiles.com/network-traffic-analysis-lumma-stealer-payload-reconstruction-6907a3daa1e9)
**Domain:** Network Traffic Analysis
**Malware family:** Lumma Stealer

## Script(s)

| File | Purpose |
|------|---------|
| `batch_deobfuscator.py` | Strips obfuscation from a batch file by extracting SET variable definitions and recursively expanding %var% references |
| `payload_reconstructor.py` | Reassembles fragmented malware payloads (Mounted.exe loader and k.a3x stage2) from extracted binary chunks |

## Usage

```bash
# Deobfuscate batch script
python3 batch_deobfuscator.py
# Input: Mn.bin (in current directory)

# Reconstruct payloads
python3 payload_reconstructor.py
# Input: Impacts, Belfast, Entities, Hyundai, Sexo.bin, System.bin, Announce.bin, Modern.bin
# Output: 692529/Mounted.exe, 692529/k.a3x
```

## Dependencies

- Python 3 (standard library only)
