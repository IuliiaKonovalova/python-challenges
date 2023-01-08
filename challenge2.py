import os
import sys

path = "just_text.txt"

try:

    size = os.path.getsize(path)

except FileNotFoundError:

    print("File not found")
    sys.exit()

print("File size is", size, "bytes")