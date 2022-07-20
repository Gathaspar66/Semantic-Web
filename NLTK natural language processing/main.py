import nltk
from nltk.chunk import conlltags2tree, tree2conlltags
import re


def special_characters(string):
    regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(string) is None:
        return False
    else:
        return True


file = open('example.txt', 'r')
text = file.read()
file.close()
sent = nltk.word_tokenize(text)
sent = nltk.pos_tag(sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
iob_tagged = tree2conlltags(cs)

file = open('wynik.txt', 'w')
for entity in iob_tagged:
    if entity[1] == 'NNP' or entity[1] == 'NN' and special_characters(entity[0]):
        print(entity)
        file.write(entity[0] + '  ' + entity[1] + '\n')

file.close()