import csv
marks = [('Seema', 22, 45), ('Anil', 21, 56), ('Mike', 20, 60)]
csvfile = open('12_module\marks.csv', 'w', newline='')
obj = csv.writer(csvfile)
for row in marks:
    obj.writerow(row)
csvfile.close()

csvfile = open('12_module\marks.csv', 'r', newline='')
obj = csv.DictReader(csvfile)
for row in obj:
    print(row)
