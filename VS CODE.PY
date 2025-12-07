import hashlib
import sys

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python checker.py <file_path> <expected_hash>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    expected_hash = sys.argv[2]
    
    current_hash = calculate_sha256(file_path)
    if current_hash == expected_hash:
        print("File integrity verified: OK")
    else:
        print(f"Integrity check failed. Expected: {expected_hash}, Got: {current_hash}")
