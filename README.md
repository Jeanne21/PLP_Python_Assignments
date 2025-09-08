# 🌍 Ubuntu Image Fetcher

A mindful Python tool for collecting images from the web while honoring Ubuntu principles of **connection** and **community**.  
This project demonstrates **file handling, error handling, and HTTP safety checks**.

---

## ✨ Features
- 📥 **Fetch multiple images** at once (enter URLs separated by spaces).
- ✅ **Precautions**:
  - Only saves valid image content (`Content-Type` check).
  - Skips files larger than **5 MB** (safety limit).
- 🔁 **Duplicate protection** using file content hashing.
- 📑 **HTTP headers validation** (`Content-Type`, `Content-Length`).
- 🌱 Inspired by Ubuntu: *"A person is a person through other persons."*

---

## 🛠️ Requirements
- Python 3.7+
- `requests` library

Install dependencies:
```bash
pip install requests
```

## 🚀 Usage
Run the program:

```bash
python fetch_images.py
```

Enter one or more image URLs separated by spaces, for example:
Please enter the image URLs: https://example.com/image1.jpg https://example.com/image2.png

The program will:

- Save images inside a folder called `Fetched_Images/`
- Prevent duplicates
- Log useful details (file type, size)

---

## 🧪 Example

### Input
https://via.placeholder.com/150

### Output
✓ Successfully fetched: 150
→ Saved to Fetched_Images/150
→ Type: image/png, Size: 1250 bytes

✓ Successfully fetched: 300
→ Saved to Fetched_Images/300
→ Type: image/png, Size: 1870 bytes

Connection strengthened. Community enriched.
A person is a person through other persons. – Ubuntu 🌱
