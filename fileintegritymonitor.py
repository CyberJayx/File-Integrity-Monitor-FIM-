import hashlib
import os

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def monitor_file(file_to_watch):
    # Create a dummy file if it doesn't exist
    if not os.path.exists(file_to_watch):
        with open(file_to_watch, "w") as f: f.write("Initial Secure Content")

    # Store the original hash
    original_hash = calculate_sha256(file_to_watch)
    print(f"Monitoring: {file_to_watch}")
    print(f"Original Hash: {original_hash}")

    # In a real tool, this would run in a loop. Here we check once.
    current_hash = calculate_sha256(file_to_watch)
    if current_hash == original_hash:
        print("Integrity Check: PASSED (No changes detected)")
    else:
        print("ALARM: File has been modified!")

if __name__ == "__main__":
    monitor_file("secure_config.txt")
