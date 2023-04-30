import rsa
import base64
from Utilities import remove_ws_equal


class RSA:
    def __init__(self):
        self.publicKey, self.privateKey = rsa.newkeys(512)

    def encrypt(self, plaintext):
        bytetext = plaintext.encode("utf-8")
        cipher = rsa.encrypt(bytetext, self.publicKey)
        encoded_string = base64.b64encode(cipher)
        utf8text = encoded_string.decode("utf8")
        return remove_ws_equal(utf8text)

# print(encrypt("asd"))
