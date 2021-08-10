import sys
import hashlib
import string
import secrets


value = str(sys.argv[1])

alphabet = string.ascii_letters + string.digits
salt = ''.join(secrets.choice(alphabet) for i in range(8))
hash_val = hashlib.sha512(value.encode()+salt.encode())
print(hash_val.hexdigest())
