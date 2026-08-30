# Hash-Identifier
# HashTool – Identify & Generate Hashes (Beginner Cybersecurity Project)

A simple, multi-mode Python CLI tool for:

- Identifying possible hash types from a hash string (MD5, SHA-1, SHA-256, etc.)
- Generating hashes from text (MD5, SHA-1, SHA-256, SHA-512)
- Generating hashes from files for integrity verification (MD5, SHA-256, SHA-512)

Built as a beginner-friendly cybersecurity project to understand:

- How cryptographic hashes look (length, charset)
- How hashes are used for file integrity and verification
- Basic Python: functions, loops, file handling, and the `hashlib` module

## Features

- Interactive menu (no complex arguments needed)
- Hash identification with short explanations for each type
- Text hashing with multiple algorithms
- File hashing with streaming (works for large files)
- Easy to extend with more hash types or modes

## Requirements

- Python 3.x
- No external libraries (uses only standard library: `hashlib`, `re`, `os`)

## Usage

Run the tool:

```bash
python hash_tool.py
```

Then choose from the menu:

1. Identify hash type  
2. Generate hashes from text  
3. Generate hashes from file  
4. Exit  

### Example: Identify a hash

Input:

```text
5d41402abc4b2a76b9719d911017c592
```

Output (example):

```text
Possible hash type(s):
- MD5: Commonly used for file checksums; not secure for passwords.
- NTLM: Windows password hash; same format as MD5, context matters.
```

### Example: Hash a file

Useful for verifying downloads or checking if a file has been modified. [17][21]

```bash
python hash_tool.py
# Choose option 3, then enter path like:
C:\Users\You\Downloads\somefile.zip
```

## How to run

1. Clone or download this repository.
2. Open terminal in this folder.
3. Run: `python hash_tool.py`
4. Follow the interactive menu.

## Ideas for extension (future work)

- Add hash verification mode: compare a file’s hash with a known good hash. [19][24]
- Add more hash types (bcrypt, scrypt, WordPress, etc.). [16]
- Add a “batch” mode to hash all files in a directory. [18]

## License

MIT
