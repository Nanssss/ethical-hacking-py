
#!usr/bin/python3
# Disclaimer: Educational & authorized testing only, see DISCLAIMER.md

import hashlib #perform the hashing

hashvalue = input("Enter a string to hash: ")

hashobject1 = hashlib.md5() # md5 object
hashobject1.update(hashvalue.encode()) #add the string to the hash object qu'on va transformer en  md5 hash
print("[*] md5: " + hashobject1.hexdigest()) #fonction qui transforme l'object en md5 hash

hashobject2 = hashlib.sha1() # sha1 object
hashobject2.update(hashvalue.encode())
print("[*] sha1: " + hashobject2.hexdigest())

hashobject3 = hashlib.sha224() # sha224 object
hashobject3.update(hashvalue.encode())
print("[*] sha224: " + hashobject3.hexdigest())

hashobject4 = hashlib.sha256() # sha256 object
hashobject4.update(hashvalue.encode())
print("[*] sha256: " + hashobject4.hexdigest())

hashobject5 = hashlib.sha512() # sha512 object
hashobject5.update(hashvalue.encode())
print("[*] sha512: " + hashobject5.hexdigest())
