
#!usr/bin/python3

import hashlib #perform the hashing

hashvalue = input("Enter a string to hash: ")

hashobject1 = hashlib.md5() ## md5
hashobject1.update(hashvalue.encode()) #add the string to the hash object qu'on va transformer en  md5 hash
print(hashobject1.hexdigest()) #fonction qui transforme l'object en md5 hash

hashobject2 = hashlib.sha1() # sha1
hashobject2.update(hashvalue.encode())
print(hashobject2.hexdigest())

hashobject3 = hashlib.sha224() # sha224
hashobject3.update(hashvalue.encode())
print(hashobject3.hexdigest())

hashobject4 = hashlib.sha256() # sha256
hashobject4.update(hashvalue.encode())
print(hashobject4.hexdigest())

hashobject5 = hashlib.sha512() # sha512
hashobject5.update(hashvalue.encode())
print(hashobject5.hexdigest())
