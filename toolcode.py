import base64
print(str)
#str = b'c2loYW93YW5nNDE5'
str = input("String to code:")
encodeStr = base64.b64encode(str.encode('utf-8'))
print(encodeStr)
print(base64.b64decode(b'dXRmLTg=').decode('utf-8'))

