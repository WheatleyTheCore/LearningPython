import csv 

file = open('data.csv', 'w', newline='')

writer = csv.writer(file)

writer.writerow(['hello', 'world'])
