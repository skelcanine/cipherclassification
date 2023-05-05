import pandas as pd
import os
import Utilities

Caesarc = "resources/DEScipher.csv"
Blowfishc = "resources/RSAcipher.csv"
"""
Blowfishcipher
Caesarcipher
DEScipher
MD5cipher
Monoalphabeticcipher
RSAcipher
"""
cdf = pd.read_csv(Caesarc)
cdb = pd.read_csv(Blowfishc)
cols1 = set(cdb.columns)
cols2 = set(cdf.columns)

print(len(cols1))
print(cdb.shape)
print(len(cols2))
print(cdf.shape)
print(cols2.difference(cols1))
print(cols1.difference(cols2))
