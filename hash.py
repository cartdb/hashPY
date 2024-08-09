import hashlib
import zlib
import os
file = input("Input File: ")
filetxt = file.replace(".", "")
filetxt = filetxt + ".txt"
filetxt = open(filetxt, "w")
if os.path.isfile(file):
    print("")
else:
    raise Exception("File not found!")
file = open(file, "rb")
file = file.read()
print(hex(zlib.adler32(file)).replace("0x", ""))
filetxt.write(hex(zlib.adler32(file)).replace("0x", ""))
print(hex(zlib.crc32(file)).replace("0x", ""))
filetxt.write("\n" + hex(zlib.crc32(file)).replace("0x", ""))
print(hashlib.md5(file).hexdigest())
filetxt.write("\n" + hashlib.md5(file).hexdigest())
print(hashlib.sha1(file).hexdigest())
filetxt.write("\n" + hashlib.sha1(file).hexdigest())
print(hashlib.sha224(file).hexdigest())
filetxt.write("\n" + hashlib.sha224(file).hexdigest())
print(hashlib.sha256(file).hexdigest())
filetxt.write("\n" + hashlib.sha256(file).hexdigest())
print(hashlib.sha384(file).hexdigest())
filetxt.write("\n" + hashlib.sha384(file).hexdigest())
print(hashlib.sha512(file).hexdigest())
filetxt.write("\n" + hashlib.sha512(file).hexdigest())
filetxt.close()