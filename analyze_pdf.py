
import sys
import re

try:
    from pypdf import PdfReader
    reader = PdfReader(r"D:\Code\Automation\New folder\Asset\Master's Thesis.pdf")
    print(f"PDF Pages: {len(reader.pages)}")
    # Extract first few pages to understand style/tone
    text = ""
    for i in range(min(3, len(reader.pages))):
        text += reader.pages[i].extract_text() + "\n"
    print("--- TEXT EXTRACT START ---")
    print(text[:1000]) # Print first 1000 chars
    print("--- TEXT EXTRACT END ---")
except ImportError:
    print("pypdf not installed. Trying basic file reading to see if it works...")
except Exception as e:
    print(f"Error: {e}")
