import hashlib


def encrypt(plaintext):
    utf8text = plaintext.encode("utf-8")
    md5obj = hashlib.md5(utf8text)
    return md5obj.hexdigest()


# print(encrypt("password"))
