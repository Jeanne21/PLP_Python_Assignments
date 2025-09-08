import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url, downloaded_hashes):
    try:
        # Fetch the image with safe timeout
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # ✅ Check important headers
        content_type = response.headers.get("Content-Type", "")
        content_length = response.headers.get("Content-Length", "unknown")

        if "image" not in content_type:
            print(f"✗ Skipping {url} (not an image, got {content_type})")
            return

        if content_length != "unknown" and int(content_length) > 5_000_000:  # 5 MB safety limit
            print(f"✗ Skipping {url} (file too large: {content_length} bytes)")
            return

        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Save to directory
        filepath = os.path.join("Fetched_Images", filename)

        # ✅ Check for duplicates by hashing file content
        file_content = response.content
        file_hash = hashlib.md5(file_content).hexdigest()

        if file_hash in downloaded_hashes:
            print(f"⚠ Duplicate skipped: {filename}")
            return
        downloaded_hashes.add(file_hash)

        with open(filepath, "wb") as f:
            f.write(file_content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"   → Saved to {filepath}")
        print(f"   → Type: {content_type}, Size: {content_length} bytes")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error fetching {url}: {e}")
    except Exception as e:
        print(f"✗ Unexpected error with {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A mindful tool for collecting images from the web\n")

    # Get multiple URLs from user
    urls = input("Enter one or more image URLs (separated by spaces): ").split()

    # Create directory
    os.makedirs("Fetched_Images", exist_ok=True)

    # Track downloaded images (hash-based duplicate prevention)
    downloaded_hashes = set()

    # Fetch each image
    for url in urls:
        fetch_image(url, downloaded_hashes)

    print("\nConnection strengthened. Community enriched.")
    print("A person is a person through other persons. – Ubuntu 🌱")


if __name__ == "__main__":
    main()
