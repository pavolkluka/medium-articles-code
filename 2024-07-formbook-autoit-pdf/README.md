# I'm going to show you how Formbook is hidden in a PDF file using AutoIt

**Published:** Jul 10, 2024
**Medium:** [Read article](https://medium.com/@pavol.kluka/im-going-to-show-you-how-formbook-is-hidden-in-a-pdf-file-using-autoit-7da6f144b779)
**Domain:** File Analysis
**Malware family:** Formbook

## Script(s)

| File | Purpose |
|------|---------|
| `deobfuscate_autoit.py` | Reverses AutoIt string obfuscation by decrypting `S30AV8ECM` function calls in `.au3` scripts |
| `decode_schoolma.py` | XOR decrypts the binary file `schoolma` using a hardcoded key |

## Usage

```bash
# Deobfuscate AutoIt script
python3 deobfuscate_autoit.py
# Input: script.au3 (in current directory)
# Output: script.au3.deob

# Decode schoolma payload
python3 decode_schoolma.py
# Input: schoolma (in current directory)
# Output: schoolma.bin
```

## Dependencies

- Python 3 (standard library only)
