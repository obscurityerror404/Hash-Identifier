import hashlib
import os
import re
import sys

# ---------- Hash identification patterns ----------
# (name, regex, length or None, short note)
HASH_PATTERNS = [
    ("MD5", r"^[a-fA-F0-9]{32}$", 32, "Commonly used for file checksums; not secure for passwords."),
    ("SHA-1", r"^[a-fA-F0-9]{40}$", 40, "Older secure hash; deprecated for security-critical uses."),
    ("SHA-224", r"^[a-fA-F0-9]{56}$", 56, "Truncated version of SHA-256."),
    ("SHA-256", r"^[a-fA-F0-9]{64}$", 64, "Widely used for file integrity and cryptocurrencies."),
    ("SHA-384", r"^[a-fA-F0-9]{96}$", 96, "Truncated version of SHA-512."),
    ("SHA-512", r"^[a-fA-F0-9]{128}$", 128, "Strong hash, longer output."),
    ("NTLM", r"^[a-fA-F0-9]{32}$", 32, "Windows password hash; same format as MD5, context matters."),
    ("MySQL5", r"^\*[a-fA-F0-9]{40}$", 41, "MySQL password hash (SHA-1 based with '*' prefix)."),
    ("bcrypt", r"^\$2[aby]?\$\d+\$[./A-Za-z0-9]{53}$", None, "Secure password hash; includes salt and cost factor."),
]

def identify_hash(hash_str: str):
    """Return list of (name, note) for possible hash types."""
    hash_str = hash_str.strip()
    results = []

    for name, pattern, length, note in HASH_PATTERNS:
        if length is not None and len(hash_str) != length:
            continue
        if re.match(pattern, hash_str):
            results.append((name, note))

    return results


# ---------- Hash generation helpers ----------
def hash_text(text: str, algorithm: str) -> str:
    """Return hex hash of text using given algorithm."""
    data = text.encode("utf-8")
    h = hashlib.new(algorithm)
    h.update(data)
    return h.hexdigest()


def hash_file(file_path: str, algorithm: str) -> str:
    """Return hex hash of a file using given algorithm (streamed)."""
    h = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        # Read in chunks to handle large files
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------- Interactive modes ----------
def mode_identify():
    print("\n=== Hash Identification Mode ===")
    h = input("Enter hash string: ").strip()
    if not h:
        print("No hash provided.")
        return

    matches = identify_hash(h)
    if not matches:
        print("No known hash type matched.")
    else:
        print("\nPossible hash type(s):")
        for name, note in matches:
            print(f"- {name}: {note}")


def mode_generate_text():
    print("\n=== Hash Generation (Text) Mode ===")
    text = input("Enter text to hash: ")
    if not text:
        print("No text provided.")
        return

    algorithms = ["md5", "sha1", "sha256", "sha512"]
    print("\nGenerated hashes:")
    for alg in algorithms:
        print(f"{alg.upper()}: {hash_text(text, alg)}")


def mode_generate_file():
    print("\n=== Hash Generation (File) Mode ===")
    path = input("Enter file path: ").strip()
    if not os.path.isfile(path):
        print("File not found or invalid path.")
        return

    algorithms = ["md5", "sha256", "sha512"]
    print("\nGenerated file hashes:")
    for alg in algorithms:
        try:
            value = hash_file(path, alg)
            print(f"{alg.upper()}: {value}")
        except Exception as e:
            print(f"{alg.upper()}: Error - {e}")


def show_menu():
    print("\n=== HashTool (Beginner Cybersecurity Project) ===")
    print("1. Identify hash type")
    print("2. Generate hashes from text")
    print("3. Generate hashes from file")
    print("4. Exit")


def main():
    # If user passes --help or -h
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print("Usage: python hash_tool.py")
        print("Run and follow the interactive menu.")
        print("Modes:")
        print("  1 – Identify hash type from a hash string")
        print("  2 – Generate MD5/SHA-1/SHA-256/SHA-512 for text")
        print("  3 – Generate MD5/SHA-256/SHA-512 for a file")
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            mode_identify()
        elif choice == "2":
            mode_generate_text()
        elif choice == "3":
            mode_generate_file()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option, choose 1-4.")


if __name__ == "__main__":
    main()