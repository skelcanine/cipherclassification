import pandas as pd
import RSAencryption
import Blowfish
import Caesar
import DES
import MD5
import Monoalphabetic
import Utilities
import csv

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
classnamesource = "resources/classnames.csv"
filepath = 'resources/'

ciphertextlist = list()
directory = "ciphers"

maindict = Utilities.maindictionary
ngramkeylist = list(maindict.keys())
additionalfeatures = ['Cipher', 'Class', 'Length', 'Alphanumeric', 'Non-Alphanumeric',
                      'Alpha', 'Digit', 'Lowercase', 'Uppercase']
allcolumns = additionalfeatures + ngramkeylist
print(len(allcolumns))
maindf = pd.DataFrame(columns=allcolumns)


# print(ngramkeylist)
classnames = dict()
resultdfdict = {}
start = 0
step = 1



for classnum, item in enumerate(Utilities.iterateoverfiles(directory)):
    print(item)
    if classnum == 4:
        #print(item)
        classname = item.split("\\")[1].split(".")[0]
        classnames[classname] = classnum
        filepath = filepath + classname+'.csv'
        cipherdf = pd.read_csv(item, header=None)
        # cipherdf = cipherdf.T.head(1)
        cipherdf = cipherdf.T
        #print(cipherdf)
        #print("-------" * 10)
        print(len(cipherdf))
        for row in range(len(cipherdf)):
            #print(row)
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
            finaldict = {**featuredict, **ngramdict}
            if len(finaldict) != 8939:
                continue
            resultdfdict[start] = finaldict
            start += step
            """ OTHER METHOD
            new_df = pd.DataFrame(finaldict, index=[0])
            maindf = pd.concat([maindf, new_df], ignore_index=True)
            """


            #print(finaldict)
maindf = pd.DataFrame.from_dict(resultdfdict, orient='index')
#classdf =pd.DataFrame.from_dict(classnames, orient='index')
#print(classnames)
print(maindf.shape)
maindf.to_csv(filepath)
#classdf.to_csv(classnamesource)

