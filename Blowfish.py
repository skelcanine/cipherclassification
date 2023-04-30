from Crypto.Cipher import Blowfish
import base64
from Utilities import pad, remove_ws_equal

bs = Blowfish.block_size
key = b"password"
blowfish = Blowfish.new(key, Blowfish.MODE_ECB)




def encrypt(plaintext):
    bytetext = plaintext.encode("utf-8")
    paddedtext = pad(bytetext)
    ciphertext = blowfish.encrypt(paddedtext)
    encoded_string = base64.b64encode(ciphertext)
    utf8text = encoded_string.decode("utf-8")
    return remove_ws_equal(utf8text)


# print(encrypt('password'))
