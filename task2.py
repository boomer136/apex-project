import hashlib
import base64

# Specify the path to the form file and read its contents
form_file_path = 'test_form.json'

with open(form_file_path, 'r') as file:
    form_contents = file.read()

# Calculate the SHA-256 digest of the form contents 
sha256_digest = hashlib.sha256(form_contents.encode('utf-8')).digest()

# Base64 encode the SHA-256 digest 
form_hash = base64.b64encode(sha256_digest).decode('utf-8')

# Print the form hash
print("Form Hash:", form_hash)