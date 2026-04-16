import re

def strip_noise(line):
    return re.sub(r'[A-Za-z0-9_]+\(', '', line)

def extract_vars(lines):
    vars = {}
    for line in lines:
        m = re.match(r'\s*set\s+(\w+)=([^\r\n]+)', line, re.I)
        if m:
            vars[m.group(1)] = m.group(2)
    return vars

def expand_vars(text, vars):
    prev = None
    while prev != text:
        prev = text
        for k, v in vars.items():
            text = text.replace(f"%{k}%", v)
    return text

def deobfuscate(path):
    with open(path, "r", errors="ignore") as f:
        raw = f.readlines()

    cleaned = [strip_noise(l) for l in raw]
    vars = extract_vars(cleaned)

    print("[+] Extracted variables:")
    for k, v in vars.items():
        print(f"    {k} = {v}")

    print("\n[+] Deobfuscated commands:\n")

    for line in cleaned:
        expanded = expand_vars(line, vars)
        if expanded.strip():
            print(expanded.strip())

if __name__ == "__main__":
    deobfuscate("Mn.bin")
