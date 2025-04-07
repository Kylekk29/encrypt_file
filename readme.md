Here are more detailed insights and a user guide for the `encrypt.py` script:

### Detailed Overview

The `encrypt.py` script is a Python application that provides an intuitive way to encrypt and decrypt files using symmetric encryption. It uses the `cryptography` library's `Fernet` module for secure encryption. The GUI is built with `tkinter`, making it accessible for users without programming experience.

### Key Features Explained

1. **Load Multiple Files**:
- Users can select multiple files for encryption or decryption using a file dialog. The names of the selected files are displayed in the GUI.

2. **Load Key**:
- Users can load a previously saved encryption key from a `.key` file. This key is essential for encrypting and decrypting files.

3. **Generate Key**:
- Users can generate a new encryption key, which is securely stored in a specified location. The key is crucial for encrypting and decrypting files.

4. **Encrypt Files**:
- Selected files are encrypted with the loaded key, and users can specify the name and location for the encrypted output files.

5. **Decrypt Files**:
- Encrypted files can be decrypted back to their original form, with users choosing the names and locations for the decrypted files.

### User Guide

#### Requirements
- **Python**: Ensure you have Python installed (preferably version 3.x).
- **Libraries**: Install the required libraries using pip:
```bash
pip install cryptography
```

#### Running the Script
1. **Launch the Application**:
- Run the script by executing `python encrypt.py` in your terminal or command prompt.

2. **Load Files**:
- Click the "Load File" button to open a file dialog. Select one or more files you wish to encrypt or decrypt.
- The names of the selected files will appear in the GUI.

3. **Load or Generate Key**:
- Click "Load Key" to select an existing key file.
- Alternatively, click "Generate Key" to create a new key. Choose a location to save the key file.

4. **Encrypt Files**:
- Click the "Encrypt File" button. For each selected file, specify where to save the encrypted version and the filename. The files will be encrypted using the loaded key.

5. **Decrypt Files**:
- Click the "Decrypt File" button. For each encrypted file, specify where to save the decrypted version and the filename. The files will be decrypted using the same key.

6. **Error Handling**:
- If an error occurs during decryption (e.g., incorrect key), an error message will be printed in the console.

### Example Use Case
- **Personal Security**: Individuals can use this tool to encrypt personal documents before sharing them, ensuring that only intended recipients can access the information.
- **Business Applications**: Companies can secure sensitive data files, such as contracts and financial reports, to prevent unauthorized access.

### Additional Notes
- Ensure you keep your encryption key secure. Losing the key means you won't be able to decrypt your files.
- Always test the encryption and decryption process with non-sensitive files before using it on important documents to familiarize yourself with the application.

This script is a practical solution for file security, combining ease of use with robust encryption methods.
