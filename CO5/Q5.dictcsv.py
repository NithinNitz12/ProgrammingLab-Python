import csv

f = open("fruits.csv","w",newline='')
writer = csv.DictWriter(f, fieldnames = ["fruit","count"])
writer.writeheader()
writer.writerow({"fruit":"apple", "count": "1"})
writer.writerow({"fruit": "banana", "count": "2"})
f.close()
c = 0
f = open("fruits.csv")
reader = csv.DictReader(f)
# for row in reader:
    # print(row)
for row in reader:
    if c==0:
        print(f'{"".join(row)}')
        c+=1
    print(f'{row["fruit"]},{row["count"]}')
    c+=1
print(c-1)
f.close()