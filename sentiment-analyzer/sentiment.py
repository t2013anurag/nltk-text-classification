from textblob.classifiers import NaiveBayesClassifier

train = [
	("I don't love this match", 'neg'),
	("I love my dog", "pos"),
	("I hate that this doesn't work", "neg"),
	('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]

test = [
	("The drink is good", "pos"),
	("I do not enjoy anything about this movie", "neg"),
	("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

classifier = NaiveBayesClassifier(train)

print classifier.classify("I love my aunt")
print classifier.classify("You should not go there again")
print classifier.classify("Their burgers are amazing")

for sentence, type_of in test:
	print sentence
	print classifier.classify(sentence)
	
print classifier.accuracy(test)
classifier.show_informative_features(5)