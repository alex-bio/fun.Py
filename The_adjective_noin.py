## Restaurants frequently use the title model "The [adjective] [noun]". Write a script that picks a new name for you! Uses weighted probabilities of words by popularity.

## Weighted by popularity
## can download COCA corpus first 5000 hits for free
## downloaded from https://www.wordfrequency.info/samples.asp
## parts of speech can be seen here: https://ucrel.lancs.ac.uk/claws7tags.html
## selected d, j, m for adjectives and n for nouns, saved as the .csv file imported below

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
