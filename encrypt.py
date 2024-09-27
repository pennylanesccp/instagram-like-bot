from cryptography.fernet import Fernet

# Step 1: Generate a key and write it to a file (done once, securely stored)
def generate_key(full_key_path):
    key = Fernet.generate_key()
    with open(full_key_path, "wb") as key_file:
        key_file.write(key)
    print(f"Key generated and saved to '{full_key_path}'.")

# Step 2: Load the key from the file (job-specific; should be protected)
def load_key(full_key_path):
    try:
        print(f"Reading key in {full_key_path}.")
        return open(full_key_path, "rb").read()
    except:
        print("Key not found.")
        generate_key(full_key_path)
        return open(full_key_path, "rb").read()

# Step 3: Encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File '{file_path}' encrypted successfully.")

# Step 4: Decrypt a file (done by the job/process)
def decrypt_file(encrypted_file_path, key):
    fernet = Fernet(key)
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    print(f"File '{encrypted_file_path}' decrypted successfully.")

    return str(fernet.decrypt(encrypted_data).decode('ascii'))

# Main flow: generate key, encrypt, and decrypt a file
def main():
    # Creating key parameters
    key_path = "/home/felipeproenca/Documentos/Personal/"
    key_name = "madruga.key"
    full_key_path = key_path + key_name

    file_to_encrypt = "encrypt_me.txt"
    path_to_encrypt = key_path + "encrypt_me.txt"

    path_encrypted = path_to_encrypt + ".enc"

    # Load the key (ensure this is done securely in the job)
    key = load_key(full_key_path)

    # Encrypt a file (replace 'test.txt' with your target file)
    encrypt_file(path_to_encrypt, key)

    # Decrypt the file when needed (this should only be accessible by the job)
    return decrypt_file(path_encrypted, key)
