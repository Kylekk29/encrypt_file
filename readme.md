Here are more detailed insights into the `encrypt.py` script:

### Overview
The script uses the `cryptography` library's `Fernet` symmetric encryption to secure files. It provides a GUI for ease of use, allowing users to manage file encryption and decryption without needing to write code.

### Components

1. **Imports**:
   - `Fernet` from `cryptography.fernet`: For encryption and decryption.
   - `tkinter`: For building the GUI.
   - `filedialog` and `messagebox`: For file selection dialogs and message displays.
   - `os`: For file path manipulations.

2. **Global Variables**:
   - `opened_file_path`: Stores the path of the file to be encrypted or decrypted.
   - `opened_file_type`: Stores the file type (extension).
   - `key`: Stores the encryption key.
   - `opened_key_path`: Stores the path to the loaded key.

3. **Functions**:
   - **`load_file()`**: Opens a file dialog to select a file, displays the name in the GUI, and saves its path and type.
   - **`load_key()`**: Loads an encryption key from a specified file and displays the key's name in the GUI.
   - **`generate_key()`**: Generates a new encryption key, saves it to a user-specified location, and shows the path via a message box.
   - **`encrypt_file()`**: Encrypts the selected file using the loaded key and prompts the user to save the encrypted file.
   - **`decrypt_file()`**: Decrypts the selected file and prompts the user to save the decrypted version.

4. **GUI Setup**:
   - A `tkinter` window is created with buttons for each action (load file, load key, generate key, encrypt, decrypt).
   - Each button is linked to its corresponding function, providing a straightforward interface.

5. **Error Handling**:
   - Basic error handling in the `decrypt_file()` function to catch exceptions during the decryption process.

### Workflow
1. **Load a File**: User clicks "Load File" to select the file to encrypt or decrypt.
2. **Load or Generate Key**: User can either load an existing key or generate a new one.
3. **Encrypt/Decrypt**: Depending on the action chosen, the user can encrypt or decrypt the selected file, saving the output to a specified location.

### Requirements
- Python environment with `tkinter` and `cryptography` libraries installed.

### Use Cases
- Protecting sensitive documents.
- Securing files before sharing them.
- Learning about file encryption and GUI development in Python.

This script serves as a practical tool for anyone needing basic file encryption capabilities while also providing an educational resource for understanding Python programming and GUI design.