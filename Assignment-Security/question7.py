import sys
import hashlib
import string
import secrets


value = str(sys.argv[1])

alphabet = string.ascii_letters + string.digits
salt = ''.join(secrets.choice(alphabet) for i in range(8))
hash_val = hashlib.pbkdf2_hmac('sha512', value.encode(), salt.encode(), 200000)
print(hash_val.hex())
