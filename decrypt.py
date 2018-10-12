import socket
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

host = '0.0.0.0'
port = 60001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
c, addr = s.accept()
ciphertext = c.recv(2048)

#private key
mykey_file = open('/home/vikram/vikram.pem', 'rb')
private_key = serialization.load_pem_private_key(
mykey_file.read(),
password=None,
backend=default_backend())

#decryption
decryption = private_key.decrypt(
			ciphertext,
			padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA1()),
				algorithm=hashes.SHA1(),
				label=None))
print decryption

c.close()
