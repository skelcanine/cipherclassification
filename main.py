import pandas as pd
import RSAencryption
import Blowfish
import Caesar
import DES
import MD5
import Monoalphabetic
import Utilities
import csv

ciphertextlist = list()
"""         RSA    
RSA = RSAencryption.RSA()

for i, password in enumerate(Utilities.top10000pass()):
    ciphertext = RSA.encrypt(password)
    ciphertextlist.append(ciphertext)
"""
"""      Blowfish
for i, password in enumerate(Utilities.top10000pass()):
    ciphertext = Blowfish.encrypt(password)
    ciphertextlist.append(ciphertext)


"""
"""         DES
for i, password in enumerate(Utilities.top10000pass()):
    ciphertext = DES.encrypt(password)
    ciphertextlist.append(ciphertext)

"""
"""
Caesar
for i, password in enumerate(Utilities.top10000pass()):
    ciphertext = Caesar.encrypt(password)
    ciphertextlist.append(ciphertext)

"""

"""
Monoalphabetic
for i, password in enumerate(Utilities.top10000pass()):
    ciphertext = Monoalphabetic.encrypt(password)
    ciphertextlist.append(ciphertext)

"""
"""
MD5
for i, password in enumerate(Utilities.top10000pass()):
    ciphertext = MD5.encrypt(password)
    ciphertextlist.append(ciphertext)
"""
""" Write to csv
    
with open('MD5cipher.csv', 'w') as file:
    # Create a CSV writer object that will write to the file 'f'
    csv_writer = csv.writer(file)
    csv_writer.writerow(ciphertextlist)



print(len(ciphertextlist))

"""
directory = "ciphers"

maindict = Utilities.maindictionary
ngramkeylist = list(maindict.keys())
additionalfeatures = ['Cipher', 'Class', 'Length', 'Alphanumeric', 'Non-Alphanumeric',
                      'Alpha', 'Digit', 'Lowercase', 'Uppercase']
# print(ngramkeylist)
classnames = list()

for classnum, item in enumerate(Utilities.iterateoverfiles(directory)):
    if classnum == 0:
        print(item)
        classnames.append(item.split("\\")[1].split(".")[0])
        cipherdf = pd.read_csv(item, header=None)
        cipherdf = cipherdf.T.head(1)
        print(cipherdf)
        print("-------" * 10)
        for row in range(len(cipherdf)):
            # Initialize variables lists
            alphacount = 0
            nonalphanumcount = 0
            alphanumericcount = 0
            digitcount = 0
            lowercase = 0
            uppercase = 0
            featurelist = list()
            featuredict = dict()
            # Get cipher
            mystr = str(cipherdf.iloc[row, 0]) # df.iat[row,col]
            # Populate featurelist with knowns
            featurelist.append(mystr)
            featurelist.append(classnum)
            featurelist.append(len(mystr))
            # Calculate counts
            for char in mystr:
                if char.isalpha():
                    alphacount += 1
                if char.isalnum():
                    alphanumericcount += 1
                else:
                    nonalphanumcount += 1
                if char.isdigit():
                    digitcount += 1
                if char.islower():
                    lowercase += 1
                if char.isupper():
                    uppercase += 1

            """ Debugging additional features
            print(mystr)  
            print(classnum)
            print(len(mystr))
            print("alphanumericcount = ", alphanumericcount)
            print("nonalphanumcount = ", nonalphanumcount)
            print("alphacount = ", alphacount)
            print("digitcount = ", digitcount)
            print("lowercase = ", lowercase)
            print("uppercase = ", uppercase)
            print(featurelist)
            print(featuredict)
            """

            featurelist.append(alphanumericcount)
            featurelist.append(nonalphanumcount)
            featurelist.append(alphacount)
            featurelist.append(digitcount)
            featurelist.append(lowercase)
            featurelist.append(uppercase)

            # Generating additional feature dictionary for cipher
            for j, feature in enumerate(additionalfeatures):
                featuredict[feature] = featurelist[j]
            # Generating ngram dictionary of cipher
            ngramdict = Utilities.word2ngramdict(mystr)
            # Creating row for main dataframe

print(classnames)