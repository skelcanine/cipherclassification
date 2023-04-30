import base64
from Crypto.Cipher import DES
from Utilities import pad, remove_ws_equal

key = b"password"
crypter = DES.new(key, DES.MODE_ECB)


def encrypt(plaintext):
    bytetext = plaintext.encode("utf-8")
    padded = pad(bytetext)
    ciphertext = crypter.encrypt(padded)
    encoded_string = base64.b64encode(ciphertext)
    utf8text = encoded_string.decode("utf-8")

    return remove_ws_equal(utf8text)


# print(encrypt("password"))
