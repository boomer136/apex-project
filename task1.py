import jwt 
import datetime


# Given Credentials Dictionary for the JWT payload and the secret key used for signing 
credentials = {
    'username': 'jws-test',
    'entity': 'apex',
    'sharedSecret': '1234567890'
}

# Create a payload. Note (isoformat() converts the datetime to a string in ISO 8601 format)
payload = {
    'username':credentials['username'],
    'entity':credentials['entity'],
    'datetime':datetime.datetime.now(datetime.timezone.utc).isoformat()
}

# Encode the payload with the shared secret using HS512 algorithm
encoded_jws = jwt.encode(payload, credentials['sharedSecret'], algorithm='HS512')

print("Encoded JWS:\n", encoded_jws)

