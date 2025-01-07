# ADVANCED ENCRYPTION TOOL

**COMPANY**: CODTECH IT SOLUTIONS PVT. LTD  
**NAME**: DEVANG AVINASH KENI  
**INTERN ID**: CT08FRA  
**DOMAIN**: Cyber Security & Ethical Hacking  
**BATCH DURATION**: December 25th, 2024 to January 25th, 2025  
**MENTOR NAME**: NEELA SANTOSH  

---

## DESCRIPTION

The Advanced Encryption Tool is a cutting-edge application designed to ensure the highest level of file security by employing the AES-256 encryption standard. Developed with both functionality and user convenience in mind, this tool is ideal for encrypting sensitive information, whether it's personal documents, corporate data, or confidential files. By combining robust security algorithms with a simple interface, the tool caters to users of all technical levels, ensuring accessibility without compromising on security.

### **Key Features**

- **Advanced Encryption with AES-256**  
  At the core of the tool is the AES-256 encryption algorithm, widely recognized as the gold standard in cryptography. This ensures that your data remains secure against brute force and other cryptographic attacks.

- **Seamless File Decryption**  
  The tool provides an intuitive way to decrypt encrypted files. By entering the correct passphrase, users can restore their files to their original form without any data corruption or loss.

- **Passphrase Protection**  
  Instead of requiring users to manage complex keys, the tool generates cryptographic keys based on a user-defined passphrase. This approach balances security with user-friendliness, ensuring that only the correct passphrase can unlock the encrypted data.

- **Key Generation**  
  The tool employs an advanced key generation mechanism that converts the user-provided passphrase into a secure cryptographic key using a hashing algorithm (PBKDF2 with SHA-256). This ensures that even weak or short passphrases are strengthened into robust keys. The generated key is then used for both encryption and decryption, eliminating the need for manual key management.

- **Batch File Support for Ease of Use**  
  To simplify the process, a custom batch file (`encryption_tool.bat`) has been included. With this, users can launch the tool directly as an application, eliminating the need to manually execute terminal commands.

- **Error Handling**  
  The tool includes robust error handling mechanisms. It gracefully handles scenarios such as invalid file paths, incorrect passphrases, or corrupted files, ensuring a smooth and frustration-free experience for users.

---

### How it works 

The Advanced Encryption Tool operates in two primary modes: encryption and decryption.

#### **Encryption**
- The user selects a file to encrypt and provides a secure passphrase.
- The tool encrypts the file, generating a new `.enc` file while leaving the original file untouched.
- The `.enc` file is fully encrypted and cannot be accessed without the correct passphrase.

#### **Decryption**
- The user selects an encrypted `.enc` file and inputs the correct passphrase.
- The tool decrypts the file and restores it to its original format.
- If an incorrect passphrase is provided, the tool notifies the user without making any modifications to the file.

---

### Setup and Installation 

#### 1. Install Python 3.8+
- Ensure Python is installed on your system. You can download it from the official [Python website](https://www.python.org/).

#### 2. Install Required Libraries
- The tool relies on the `pycryptodome` library for its cryptographic functions. Install it using the following command:
  ```bash
  pip install pycryptodome
  ```

#### 3. Run the Tool
- Use the included batch file (`encryption_tool.bat`) to launch the tool with a double-click. This batch file has been specifically designed to provide a smooth user experience, avoiding the need for terminal commands like `python tool.py`.

#### Encrypt and Decrypt

- **Encrypt**: Select the file you wish to secure and provide a passphrase. The encrypted file will be saved in the same directory with a `.enc` extension.
- **Decrypt**: Choose the `.enc` file and provide the corresponding passphrase to restore the original file.

---

### TESTING THE TOOL

1. For testing purposes, you can try encrypting a sample text file.  
2. Use a secure passphrase and observe how the `.enc` file is generated.  
3. Then attempt to decrypt it using the same passphrase to ensure the tool works as intended.

---

### PRECAUTIONS

- **Passphrase Security:** Always remember the passphrase you set. The encrypted files cannot be decrypted without it.
- **Backup Your Data:** Before encrypting critical files, create a backup to avoid accidental loss.
- **Test the Tool First:** Use non-critical files to familiarize yourself with the tool’s functions before using it on sensitive data.
- **Avoid Shared Systems:** For maximum security, use the tool on a private, secure system.

---

## OUTPUT

When the tool is running, you will observe:

- A clear and simple menu offering encryption and decryption options.
- Status messages indicating successful encryption or decryption, or errors in case of incorrect inputs.
- The creation of encrypted `.enc` files and their seamless restoration to the original format.

### **Example Output Screens**

- Encryption Success Screen  
- Decryption Success Screen  
- Error Handling Screen  

This Advanced Encryption Tool demonstrates how secure data management can be both powerful and user-friendly. By combining robust cryptographic methods with intuitive usability, it serves as a reliable solution for safeguarding sensitive information.
