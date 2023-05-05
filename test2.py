import pandas as pd
import os
import Utilities
"""
abc = pd.read_csv('resources/DEScipher.csv')
cols = abc.columns
print(abc.head(10))
print(abc.shape)
print(abc.columns)
#print(abc.dtypes)

print(abc.memory_usage(deep=True))

icols = abc.select_dtypes('integer').columns
abc[icols] = abc[icols].apply(pd.to_numeric, downcast='integer')
cols2 = abc.columns
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print (abc.dtypes)
print(abc.memory_usage(deep=True))

"""
main_directory = "resources/"

df_file = list()
for classnum, item in enumerate(Utilities.iterateoverfiles(main_directory)):


    # CSV to dataframe
    mydf = pd.read_csv(item)
    print(classnum)
    print(mydf.shape)

    mydf = mydf.drop(columns=['Unnamed: 0', 'Cipher'])
    icols = mydf.select_dtypes('integer').columns
    mydf[icols] = mydf[icols].apply(pd.to_numeric, downcast='integer')
    df_file.append(mydf)


maindf = 'resources/main.csv'

df_file[0].to_csv(maindf)
df_file.pop(0)
for k, dfx in enumerate(df_file):
    print(k)
    dfx.to_csv(maindf, mode='a', header=False)

print("starting read")
del df_file
df_master = pd.read_csv(maindf)

print(df_master.shape)
print(df_master.head(10))