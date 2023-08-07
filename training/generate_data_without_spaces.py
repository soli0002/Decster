import random
import hashlib
import codecs
import string
import nltk
import urllib
import base64
import csv

nltk.download('words')
from nltk.corpus import words

# List of encoding types
encoding_types = ["SHA256", "MD5", "SHA1", "SHA224", "SHA384", "SHA512",
                  "Base16", "Base32", "Base64", "Binary", "ASCII", "Rot13"]

# Get a list of real dictionary words

def generate_random_alphanumeric(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

dictionary_words = words.words()


# Function to generate SHA1 hash
def generate_sha1(text):
    return hashlib.sha1(text.encode('utf-8')).hexdigest()

# Function to generate SHA224 hash
def generate_sha224(text):
    return hashlib.sha224(text.encode('utf-8')).hexdigest()

# Function to generate SHA256 hash
def generate_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

# Function to generate SHA384 hash
def generate_sha384(text):
    return hashlib.sha384(text.encode('utf-8')).hexdigest()

# Function to generate SHA512 hash
def generate_sha512(text):
    return hashlib.sha512(text.encode('utf-8')).hexdigest()

# Function to generate MD5 hash
def generate_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Function to generate Base16 (hexadecimal) encoding
def generate_base16(text):
    return codecs.encode(text.encode(), 'hex').decode()

# Function to generate Base32 encoding
def generate_base32(text):
    return base64.b32encode(text.encode()).decode()

# Function to generate Base64 encoding
def generate_base64(text):
    return base64.b64encode(text.encode()).decode()

# Function to generate Binary encoding
def generate_binary(text):
    encoded = ''.join(format(ord(char), '08b') for char in text)
    # Remove spaces from binary encoding
    encoded = encoded.replace(" ", "")
    return encoded

# Function to generate ASCII encoding
def generate_ascii(text):
    encoded = ' '.join(str(ord(char)) for char in text)
    # Remove spaces from ascii encoding
    encoded = encoded.replace(" ", "")
    return encoded


# Function to generate Rot13 encoding
def generate_rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)



def generate_synthetic_data_with_dictionary_words_and_alphanumeric_strings(filename, num_samples_per_type=1000):
    with open(filename, 'a', newline='') as csvfile:  # Use 'a' for append mode
        csv_writer = csv.writer(csvfile)

        for _ in range(num_samples_per_type):
            for encoding_type in encoding_types:
                original_text = '_'.join(random.sample(dictionary_words, random.randint(2, 4)))

                if encoding_type == "SHA256":
                    encoded_text = generate_sha256(original_text)
                elif encoding_type == "MD5":
                    encoded_text = generate_md5(original_text)
                elif encoding_type == "SHA1":
                    encoded_text = generate_sha1(original_text)
                elif encoding_type == "SHA224":
                    encoded_text = generate_sha224(original_text)
                elif encoding_type == "SHA384":
                    encoded_text = generate_sha384(original_text)
                elif encoding_type == "SHA512":
                    encoded_text = generate_sha512(original_text)
                elif encoding_type == "Base16":
                    encoded_text = generate_base16(original_text)
                elif encoding_type == "Base32":
                    encoded_text = generate_base32(original_text)
                elif encoding_type == "Base64":
                    encoded_text = generate_base64(original_text)
                elif encoding_type == "Binary":
                    encoded_text = generate_binary(original_text)
                elif encoding_type == "ASCII":
                    encoded_text = generate_ascii(original_text)
                elif encoding_type == "Rot13":
                    encoded_text = generate_rot13(original_text)

                csv_writer.writerow([encoded_text, encoding_type])


if __name__ == "__main__":
    synthetic_data = generate_synthetic_data_with_dictionary_words_and_alphanumeric_strings("training_data.csv", num_samples_per_type=50000)
    print("Appended to training_data.csv")