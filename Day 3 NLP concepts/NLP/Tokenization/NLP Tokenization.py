#!/usr/bin/env python
# coding: utf-8

# In[20]:


#tokenization
from nltk.tokenize import sent_tokenize,word_tokenize
text="Hi John , how are you doing ? I will be travelling to your city. Lets Catchup"
#Paragraph containing multiple sentences 
sent_tokenize(text) # will get list of setences from the paragraph


# In[22]:


word_tokenize(text) #will get each word from the paragraph or sentence


# In[27]:


#Stemming
from nltk.stem import PorterStemmer 
stemmer=PorterStemmer()
print(stemmer.stem("playing")) #word playing inflectional form removed (changes the word into its root form)
print(stemmer.stem("plays")) #So output is play(root form)
print(stemmer.stem("played"))
# Stemming is not a very good normalization sometimes it produces words in dictionary
print(stemmer.stem("increases"))


# In[13]:


#Lemmetization
from nltk.stem import WordNetLemmatizer
lemm = WordNetLemmatizer()
print(lemm.lemmatize("increases"))
print(lemm.lemmatize("running",pos="a")) #a for adverb for more info press shift + tab


# In[23]:


#Part Of Speech Tags
from nltk.tokenize import word_tokenize
from nltk import pos_tag
text = "Hi John , how are you doing ? I will be travelling to your city. Lets Catchup"
tokens = word_tokenize(text)
pos_tag(tokens)#annotate all of the tokens with their corresponding POST


# In[32]:


#Getting synonyms and antonyms
from nltk.corpus import wordnet #Very comprehensive vocabulary of all possible words
wordnet.synsets('good') # get a list of all synonyms  


# In[35]:


from nltk import ngrams 
s="I love to play football" #sentence
n=2 #obtaining bigram combinations from the sentence
for gram in ngrams(word_tokenize(s),n):
    print(gram)

