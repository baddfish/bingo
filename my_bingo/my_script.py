# my_bingo/my_script.py

import pandas

from my_bingo.my_mod import enlarge

print("Hello World")

df = pandas.DataFrame({"state": ["CT", "CO", "AZ", "MT"]})
print(df.head())


print("------------")


X = 5
print("NUMBER", X)
print("ENLARGED NUMBER", enlarge(X)) # invoking our function