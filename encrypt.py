import socket
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

host = '0.0.0.0'
port = 60001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#Opening the text file and reading it
out = open('/home/vikram/asn1.txt', 'r+')
msg = out.read()

#private key
mykey_file = open('/home/vikram/vikram.pem', 'rb')
private_key = serialization.load_pem_private_key(
mykey_file.read(),
password=None,
backend=default_backend())

#extracting public key from private key
public_key = private_key.public_key()

#ciphertext generation
ciphertext = public_key.encrypt(
	msg,
		padding.OAEP(	
				mgf=padding.MGF1(algorithm=hashes.SHA1()),
				algorithm=hashes.SHA1(),
				label=None))
s.send(ciphertext)

print msg
print ciphertext

s.close()
