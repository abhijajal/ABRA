#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
import spacy
from nltk.stem import WordNetLemmatizer  
from spacy import displacy
from pathlib import Path
import chardet 
import nltk.tokenize as tokenizer
import os
from nltk.corpus import wordnet as wn

def getLemmas(synset,lemmaSet):
        for lemma in synset.lemmas():
            lemmaSet.add(lemma.name())
        return lemmaSet

def getWordNet(word):
    syn=wn.synsets(word)
    synonyms=set()
    hypernyms=set()
    hyponyms=set()
    holonyms=set()
    meronyms=set()
    allSet=[]
    for synset in syn:

        synonyms=getLemmas(synset,synonyms)
        for hypernym in synset.hypernyms():
            hypernyms=getLemmas(hypernym,hypernyms)
        for hyponym in synset.hyponyms():
            hyponyms=getLemmas(hyponym,hyponyms)
        for meronym in synset.part_meronyms():
            meronyms=getLemmas(meronym,meronyms)
        for holonym in synset.part_holonyms():
            holonyms=getLemmas(holonym,holonyms)
    allSet.append(synonyms)
    allSet.append(hypernyms)
    allSet.append(hyponyms)
    allSet.append(meronyms)
    allSet.append(holonyms)
    return allSet

files=[]
entries = os.listdir('WikipediaArticles/')
fileNo=0
for entry in entries:    
    fileNo+=1
    files.append(open('WikipediaArticles/'+entry, 'rb'))
    
sp = spacy.load('en_core_web_sm')
fileNo=0
for file in files:
    fileNo+=1
    sFile=open(str(fileNo)+'sentences.txt','w',encoding="utf-8")
    lFile=open(str(fileNo)+'wordsLemmaPOS.txt','w',encoding="utf-8")
    print("Working on File"+str(fileNo))
    count=0
    eachLine = file.readline().decode('utf-8','ignore')
    while(eachLine):
        sentences = tokenizer.sent_tokenize(eachLine)
        for sentence in sentences: 
            sFile.write(sentence+"\n")
            spacySentence = sp(sentence)
            options = {"compact": True}
            count=count+1
            svg = displacy.render(spacySentence, style="dep", jupyter=False,options=options)
            file_name = str(fileNo)+"_"+str(count)+".svg"
            output_path = Path("dependencyGraph/" + file_name)

            output_path.open("w", encoding="utf-8").write(svg)
            for word in spacySentence:
                lFile.write(word.text+":"+word.lemma_+":"+word.pos_+":"+str(getWordNet(word.text))+"\n")
        eachLine = file.readline().decode('utf-8','ignore')

    sFile.close()
    lFile.close()
print("Done!")

