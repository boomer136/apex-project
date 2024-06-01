import base64
import hmac
import hashlib
import json
import datetime
import jwt

# Credentials
credentials = {
    'username': 'jws-test',
    'entity': 'apex',
    'sharedSecret': '1234567890'
}

# Create a payload 
payload = {
    'username':credentials['username'],
    'entity':credentials['entity'],
    'datetime':datetime.datetime.now(datetime.timezone.utc).isoformat()
}

# Encode the payload with the shared secret using HS512 algorithm
encoded_jws = jwt.encode(payload, credentials['sharedSecret'], algorithm='HS512')

print("Encoded JWS:\n", encoded_jws)

