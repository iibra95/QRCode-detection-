from pyDes import *
import base64
import hashlib
from Crypto import Random 
from Crypto.Cipher import AES 
from qrtools import QR
from qrcode import * 
import qrcode
import updated2


data = "adham   20132040"
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
encrypted = k.encrypt(data)
print "Encrypted: %r" % encrypted
decrypted =  k.decrypt(encrypted)
print "Decrypted: %r" % decrypted
assert k.decrypt(encrypted, padmode=PAD_PKCS5) == data

qr = QRCode(version=2, error_correction=ERROR_CORRECT_H)
qr.add_data(encrypted)
qr.make(fit=True) # Generate the QRCode itself
im = qr.make_image()
im.save("enc.png")

