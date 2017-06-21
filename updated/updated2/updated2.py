import zbar
from Crypto.Cipher import AES
import hashlib
from PIL import Image
import cv2
import base64
from pyDes import *
#from updated import encrypted
import updated
import sys, qrcode
import qrtools
from qrtools import QR
from Crypto import Random 

def main():
   
    picture = cv2.imread("encqr5.png")
  
    printed=False

    while True:
       
        # Converts image to grayscale.
        gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        image = Image.fromarray(gray)
        width, height = image.size
        zbar_image = zbar.Image(width, height, 'Y800', image.tobytes())

        # Scans the zbar image.
        scanner = zbar.ImageScanner()
        scanner.scan(zbar_image)
        # Prints data from image.

        for decoded in zbar_image:
            if not printed:
                #print(decoded.data)
                printed=True
        
        newdata = decoded.data
      
        passphrase = "thisisakeyforenc"
        #message="adham   20132040"
        BLOCK_SIZE=16
        IV = Random.new().read(BLOCK_SIZE)
        #aes = AES.new(passphrase, AES.MODE_CFB, IV)
        aes = AES.new(passphrase, AES.MODE_ECB, IV)
        decrypted = aes.decrypt(base64.b64decode(newdata))
       
        print "Decrypted: %r" % decrypted
        break








      #d = qrcode.Decoder(picture)
    #if d.decode(picture):
    #       print 'result: ' + d.result
    #else:
    #       print 'error: ' + d.error
    #print(newdata)
    #qr = qrtools.QR()
        #qr.decode("new1.png")
        #True
        #print qr.data
        #break
      #IV = 16 * '\x00'          
        #mode = AES.MODE_CBC
        #password = 'password12345678'
        #key = hashlib.sha256(password).digest()
        #decryptor = AES.new(key, mode, IV=IV)
        #plain = decryptor.decrypt(newdata)
     #k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        #k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        #decrypted =  k.decrypt(newdata)
        #pic = QR(cv2.imread("new3.png"))
        #pic.data
        #pic.data_type
        #decrypted= pic.data_to_string()
        #print(newdata)
              #IV = 16 * '\x00'          
              #mode = AES.MODE_CBC
              #password = 'ibra123456789123'
              #key = hashlib.sha256(password).digest()
              #decryptor = AES.new(key, mode, IV=IV)
              #plain = decryptor.decrypt(decoded.data)
              #print(plain)
              #k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
              #decrypted =  k.decrypt(decoded.data)
              #assert k.decrypt(decoded.data,padmode=PAD_PKCS5,pad=None) == decoded.data
              #assert k.decrypt(decoded.data , "\0\0\0\0\0\0\0\0" , padmode=PAD_PKCS5) == decoded.data
              #print "Decrypted: %r" % decrypted
             #assert k.decrypt(encrypted, padmode=PAD_PKCS5) == data 
              
              #assert k.decrypt(de,padmode=PAD_PKCS5
               

                         
if __name__ == "__main__":
    main()