'''with open('input1.csv', 'r') as csvfile:
    input_reader = csv.reader(csvfile, delimiter= ',')
    word_count= {}
    for row in input_reader:
        for word in row:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    for key,value in word_count.items():
        print('{} {}'.format(key,value))
    csvfile.close()'''
import csv

import csv

with open('input1.csv', 'r') as csvfile:
    input_reader = csv.reader(csvfile)
    word_count = {}
    for row in input_reader:
        count1 = 0
        for word in row:
            rows = list(input_reader)
            limit1 = len(rows)
            print(limit1)
            if word not in word_count:
                word_count[word] = 1
                count1 += 1
            else:
                word_count[word] += 1
                count1 += 1
    for key, value in word_count.items():
        print('{} {}'.format(key, value))
