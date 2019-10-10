import csv 

file = open('data.csv', 'r', newline='')

#writer = csv.writer(file)


#for i in range(30):
#    writer.writerow(['hello', 'world'])

reader = csv.reader(file)
stuff = list(reader)

print(stuff[3])
