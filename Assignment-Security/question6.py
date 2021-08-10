import sys
import hashlib

value  = str(sys.argv[1])
salt  = 'Km5d5ivMy8iexuHcZrsD'
hash_val = hashlib.pbkdf2_hmac('sha512', value.encode(), salt.encode(), 200000)
print(hash_val.hex())
