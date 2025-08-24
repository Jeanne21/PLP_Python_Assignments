# File Handling & Exception Handling Assignment 📝

## 📌 Overview
This project demonstrates how to **read and write files in Python** while using **exception handling** to make the program more robust.  
It covers:
- Reading files safely.  
- Writing modified content to a new file.  
- Handling common errors like missing files or permission issues.  

---

## 🚀 Features
1. **Read a File**  
   - Prompts the user for a filename.  
   - Displays the contents of the file.  
   - Handles errors if the file does not exist.  

2. **Modify and Write to a New File**  
   - Prompts the user for an input filename and an output filename.  
   - Reads the original content.  
   - Modifies the text (converts it to **uppercase** in this example).  
   - Saves the modified content into a new file.  

3. **Error Handling**  
   - `FileNotFoundError` → when the file doesn’t exist.  
   - `PermissionError` → when the file can’t be accessed.  
   - Generic `Exception` → catches unexpected errors.  

---

## 📂 How to Run
1. Make sure you have Python 3 installed.  
2. Save the program file (e.g., `file_handling.py`).  
3. Run it in the terminal:  
   ```bash
   python file_handling.py
4. Choose one of the options from the menu:
- 1 → Read a file.
- 2 → Modify a file and write to a new file.

## 🧪 Example  

### Input (`sample.txt`)  
Hello world!
This is a test file.

### Running Option 2  
- **Input file:** `sample.txt`  
- **Output file:** `modified.txt`  

### Output (`modified.txt`)  
```bash
HELLO WORLD!  
THIS IS A TEST FILE.  

