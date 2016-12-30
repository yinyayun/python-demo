#coding:utf-8
from nltk.corpus import wordnet as  wn

sets= wn.synsets("led")
for s in sets:
    # print wn.synset(str(s)).lemma_names