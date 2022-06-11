import csv


with open('/mnt/c/Users/Andrew Franco/personalcode/musicdatabase/data/smallmusic.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    x = {}
    for row in reader:
        x[row[0]] = row[1]
        #print(row[1])
    print(x)