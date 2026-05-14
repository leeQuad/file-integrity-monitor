import hashlib
import os
import json

FOLDER_TO_MONITOR = "monitored_files"
HASH_FILE = "hashes.json"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def scan_files():
    file_hashes = {}

    for filename in os.listdir(FOLDER_TO_MONITOR):
        filepath = os.path.join(FOLDER_TO_MONITOR, filename)

        if os.path.isfile(filepath):
            file_hashes[filename] = calculate_hash(filepath)

    return file_hashes

def load_old_hashes():
    if not os.path.exists(HASH_FILE):
        return {}

    with open(HASH_FILE, "r") as file:
        return json.load(file)

def save_hashes(hashes):
    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

old_hashes = load_old_hashes()
new_hashes = scan_files()

for file, hash_value in new_hashes.items():
    if file not in old_hashes:
        print(f"[NEW FILE] {file}")

    elif old_hashes[file] != hash_value:
        print(f"[CHANGED] {file}")

for file in old_hashes:
    if file not in new_hashes:
        print(f"[DELETED] {file}")

save_hashes(new_hashes)
