# General Integration

## Task 1 - JWS Generation 

This script generates a JSON Web Signature (JWS) using the SHA-512 algorithm. It encodes a payload containing user credentials and the current datetime, signed with a shared secret. 

Using these credentials, write a script that generates a SHA-512 encoded JWS, with a payload that contains the username, entity, and datetime.

{
  'username': jws-test,
  'entity': apex,
  'sharedSecret':1234567890
}


## Task 2 - Form Hash 

For task 2, imagine you have been provided the following instructions:
"For our purposes, form hash is calculated exactly as it is downloaded from the API which does not include any user data. The hash value is calculated by base64 encoding the SHA-256 digest of the form contents. This value is then included along with the account holder's input data when making an account request. "

Using the instructions above, write a script that generates the form hash for the form you were provided. 

## Task 3 - Form Completion Schema 

As mentioned in Task 2, in the attached files, you should have a JSON form, which shows various fields as required or optional, and shows the required datatypes for each field. Complete the form as if you were answering it for a generic Individual Cash Account and fill out only the fields required to do so (i.e. try not to have any optional fields). 
