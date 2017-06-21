import base64
from Crypto import Random 
from Crypto.Cipher import AES 
from qrtools import QR
from qrcode import * 
import qrcode
import updated2
BLOCK_SIZE=16

passphrase = "thisisakeyforenc"
message="123456789123456D"
IV = Random.new().read(BLOCK_SIZE)
aes = AES.new(passphrase, AES.MODE_ECB, IV)
encrypted = base64.b64encode(aes.encrypt(message))
print(encrypted)

aes = AES.new(passphrase, AES.MODE_ECB, IV)
decrypted = aes.decrypt(base64.b64decode(encrypted))
print(decrypted)


#length = 16 - (len(message) % 16)

#print(length)
#length2 = 16 - (len(decrypted) % 16)
#print(length2)

#######################################################################
qr = QRCode(version=2, error_correction=ERROR_CORRECT_H)
qr.add_data(encrypted)
qr.make(fit=True) # Generate the QRCode itself
#length3 = 16 - (len(encrypted) % 16)
#print(length3)
 #im contains a PIL.Image.Image object
im = qr.make_image()


im.save("encqr5.png")






#password = '1234567891234567'
#key = hashlib.sha256(password).digest()
#IV = 16 * '\x00'           # Initialization vector: discussed later
#mode = AES.MODE_CBC
#encryptor = AES.new(key[:16], mode, IV=IV)

#text = 'adham   20132040' 
#ciphertext = encryptor.encrypt(text)
#print(ciphertext)
#length5 = 16 - (len(ciphertext) % 16)
#print(length5)
#decryptor = AES.new(key[:16], mode, IV=IV)
#plain = decryptor.decrypt(ciphertext)
#print(plain)
#im = qr.make(ciphertext, image_factory=PymagingImage)
# To save it
#qr = qrcode.QRCode(version=3,error_correction=qrcode.constants.ERROR_CORRECT_H)
#qr.add_data(encrypted)
#im = qr.make_image(fit=True)

#im = qr.make_image(fill_color="black", back_color="white")