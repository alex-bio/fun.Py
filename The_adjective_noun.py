## Restaurants frequently use the title model "The [adjective] [noun]".
## Unweighted 
## set working directory
import os
os.chdir('C:\\Users\\user\\OneDrive - 6pine.com\\python\\VScode_python')
os.getcwd()

import pandas as pd
df = pd.read_csv("dict.csv")
## what are columns?
list(df)
## ['adj', 'noun']

## now assign categories/clean up
adj = df["adj"].tolist()
## what are values in adj?
from collections import Counter
Counter(adj)
## nan: 64008
## kind of cool it sorts it for you from high to low values
len(adj) - 64008
## should expect to see 18184 in cleaned list
cleanedAdj = [x for x in adj if str(x) != 'nan']
len(cleanedAdj)
## nice
adj = cleanedAdj
len(adj)

noun = df['noun'].tolist()
Counter(noun)
## No NaN values so we're good
len(noun)

## now can you choose randomly with replacement? 
import random

def word():
  a = (random.choices(adj,k=1))
  b = (random.choices(noun,k=1))
  ## the join function produces a string, not a list, then can add two strings together
  print("The " + ' '.join(a+b))

## now make this a function

## Weighted
## Weighted by popularity
## can only download COCA corpus first 5000 hits :( 
## downloaded from https://www.wordfrequency.info/samples.asp
## parts of speech can be seen here: https://ucrel.lancs.ac.uk/claws7tags.html
## selected d, j, m for adjectives and n for nouns
import os
os.chdir('C:\\Users\\user\\OneDrive - 6pine.com\\python\\VScode_python')
os.getcwd()

import pandas as pd
## read in the 6200 total words and their rankings
df = pd.read_csv("dict_lemmas_60k.csv")
list(df)
## pull out the appropriate adjectives and nouns by parts of speech 'PoS'
adj = df[df['PoS'].isin(['d','j','m'])]
noun = df[df['PoS'].isin(['n'])]
## normalize the frequency by assigning a ratio (these will be probabilities later)
adj = adj.assign(ratio = adj['freq']/sum(adj['freq']))
noun = noun.assign(ratio = noun['freq']/sum(noun['freq']))
## sanity check ratio column adds to 1
sum(adj['ratio'])
sum(noun['ratio'])

## now sample your function!
import random
def word():
  x = random.choices(population = adj['lemma'].tolist(), k=1, weights=adj['ratio'])
  ## replace is True here, part of choices, but does not matter since we are only drawing one thing
  y = random.choices(population = noun['lemma'].tolist(),k=1, weights=noun['ratio'])
  print("The " + ' '.join(x+y))

word()
