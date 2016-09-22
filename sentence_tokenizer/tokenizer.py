import nltk
sentence = "I love you! NLTK don't you love me. The answer may seem a bit weird but who cares!"
tokens = nltk.word_tokenize(sentence)
print tokens

print "Parts of speech :\n"
tagged = nltk.pos_tag(tokens)
print tagged