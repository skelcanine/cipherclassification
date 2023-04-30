import string

# A list containing all characters
all_letters = string.ascii_letters

"""
create a dictionary to store the substitution
for the given alphabet in the plain text
based on the key
"""

dict1 = {}
key = 7

for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]


def encrypt(plaintext):
    cipher_txt = []
    for char in plaintext:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp = char
            cipher_txt.append(temp)

    cipher_txt = "".join(cipher_txt)
    return cipher_txt


# print(encrypt("of"))


"""
create a dictionary to store the substitution
for the given alphabet in the cipher
text based on the key


dict2 = {}
for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i - key) % (len(all_letters))]

# loop to recover plain text
decrypt_txt = []

for char in cipher_txt:
    if char in all_letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)

decrypt_txt = "".join(decrypt_txt)
print("Recovered plain text :", decrypt_txt)
"""
