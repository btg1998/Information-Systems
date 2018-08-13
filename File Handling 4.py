import csv
with open('Ws.csv', "w", newline='') as csv_file:
    Word_Score ="App" + "," + str(234.5)
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(Word_Score.split(","))
with open('Ws.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(row)
