from pathlib import Path

WORKDIR = Path("692529")
LOADER_NAME = "Mounted.exe"

IMPACTS_FILE = Path("Impacts")
IMPACTS_FILTER = b"REBOUND"

LOADER_PARTS = [
    "Belfast",
    "Entities",
    "Hyundai"
]

STAGE2_PARTS = [
    "Sexo.bin",
    "System.bin",
    "Announce.bin",
    "Modern.bin"
]

STAGE2_NAME = "k.a3x"

def ensure_workdir():
    WORKDIR.mkdir(exist_ok=True)
    print(f"Working directory: {WORKDIR}")

def write_mz_stub():
    path = WORKDIR / LOADER_NAME
    with open(path, "wb") as f:
        f.write(b"MZ")
    print("MZ stub written")

def append_impacts():
    out = WORKDIR / LOADER_NAME

    with open(IMPACTS_FILE, "rb") as src, open(out, "ab") as dst:
        for line in src:
            if IMPACTS_FILTER not in line:
                dst.write(line)

    print("Impacts appended (REBOUND filtered)")

def append_binary_parts(parts, target):
    with open(target, "ab") as dst:
        for part in parts:
            part_path = Path(part)
            with open(part_path, "rb") as p:
                dst.write(p.read())
            print(f"Appended {part}")

def build_loader():
    print("Building loader...")
    write_mz_stub()
    append_impacts()
    append_binary_parts(LOADER_PARTS, WORKDIR / LOADER_NAME)

def build_stage2():
    print("Building stage2 (k.a3x)...")
    out = WORKDIR / STAGE2_NAME

    with open(out, "wb") as dst:
        for part in STAGE2_PARTS:
            with open(part, "rb") as p:
                dst.write(p.read())
            print(f"Appended {part}")

    print("Stage2 built")

def main():
    ensure_workdir()
    build_loader()
    build_stage2()

    print("\nReconstruction complete")
    print(f"  Loader : {WORKDIR / LOADER_NAME}")
    print(f"  Stage2 : {WORKDIR / STAGE2_NAME}")

if __name__ == "__main__":
    main()
