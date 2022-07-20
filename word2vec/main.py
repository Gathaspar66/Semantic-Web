import gensim
from gensim.models import Word2Vec, KeyedVectors
from pyemd import emd

model = gensim.models.KeyedVectors.load_word2vec_format('D:\\GoogleNews-vectors-negative300.bin', binary=True)

temp=[]
with open('wyniczek.txt') as file:
    for line in file:
        temp.append(line.split(' ', 1)[0].rstrip())
file.close()

file = open('wynikLab10.txt', 'w')

for i in range(len(temp)):
    a = temp[i]
    for i in range(len(temp)):
        b = temp[i]
        if a == b:
            continue
        distance = model.wmdistance(a, b)
        file.write(a + ',' + b + ',' + '%.3f' % distance +' ' '\n')

file.close()

fn = 'wynikLab10.txt'
sorted_fn = 'sorted_filename.txt'

with open(fn,'r', encoding='windows-1250') as first_file:
    rows = first_file.readlines()

    sorted_rows = sorted(rows, key=lambda x: float(x.split(',')[2]), reverse=True)

    with open(sorted_fn,'w') as second_file:
        for row in sorted_rows:
            if float(row.split(',')[2]) <= 1:
                second_file.write(row)