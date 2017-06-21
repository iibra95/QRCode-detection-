import zbar
from Crypto.Cipher import AES
import hashlib
from PIL import Image
import cv2
from pyDes import *
import updated

def main():
   
    picture = cv2.imread("agdadhaga.png")
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
              #IV = 16 * '\x00'          
              #mode = AES.MODE_CBC
              #password = 'ibra123456789123'
              #key = hashlib.sha256(password).digest()
              #decryptor = AES.new(key, mode, IV=IV)
              #plain = decryptor.decrypt(decoded.data)
              #print(plain)
              k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
              decrypted =  k.decrypt(decoded.data)
              print "Decrypted: %r" % decrypted
              assert k.decrypt(encrypted, padmode=PAD_PKCS5) == data
              printed=True

                         
if __name__ == "__main__":
    main()