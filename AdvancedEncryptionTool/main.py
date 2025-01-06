import os
from cryptography.fernet import Fernet

# Create folder structure
os.makedirs("encrypted_files", exist_ok=True)
os.makedirs("decrypted_files", exist_ok=True)

# Header for the tool
def print_header():
    print("===================================================================")
    print("||                  ADVANCED ENCRYPTION TOOL                     ||")
    print("||              Secure Your Files with AES-256!                 ||")
    print("===================================================================")

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'key.key'.")

# Load an existing key
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Error: Key file not found. Generate a key first.")
        return None

# Encrypt a file
def encrypt_file(file_path):
    key = load_key()
    if key is None:
        return

    try:
        with open(file_path, "rb") as file:
            data = file.read()
        
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        # Save encrypted file in the "encrypted_files" folder
        file_name = os.path.basename(file_path)
        encrypted_path = os.path.join("encrypted_files", file_name + ".enc")
        with open(encrypted_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        print(f"File encrypted and saved to '{encrypted_path}'.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

# Decrypt a file
def decrypt_file(file_path):
    key = load_key()
    if key is None:
        return

    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        # Save decrypted file in the "decrypted_files" folder
        file_name = os.path.basename(file_path).replace(".enc", "")
        decrypted_path = os.path.join("decrypted_files", file_name)
        with open(decrypted_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        print(f"File decrypted and saved to '{decrypted_path}'.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

# Menu to navigate the tool
def main_menu():
    while True:
        print_header()
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        print("===================================================================")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_path = input("Enter the path of the file to encrypt: ").strip()
            encrypt_file(file_path)
        elif choice == "3":
            file_path = input("Enter the path of the file to decrypt: ").strip()
            decrypt_file(file_path)
        elif choice == "4":
            print("Exiting the Advanced Encryption Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
