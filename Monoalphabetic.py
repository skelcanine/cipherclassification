keys = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p',
        'l': 'o', 'm': 'n', '1': '9', '9': '1', '4': '7', '7': '4', '8': '6', '6': '8'}

reverse_keys = {}

for key, value in keys.items():
    reverse_keys[value] = key


def encrypt(text):
    text = str(text)
    encrypting = []
    for l in text:
        encrypting.append(keys.get(l, l))
    return ''.join(encrypting)


def decipher(text):
    text = str(text)
    decrypted = []
    for l in text:
        decrypted.append(reverse_keys.get(l, l))
    print(''.join(decrypted))


#encrypt("hej")
#decipher("svq")
