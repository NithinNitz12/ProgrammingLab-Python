import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Spider-Man: Far from Home", "Peter Parker"])
    writer.writerow([2, "Edge of Tomorrow", "Lt. Col. Bill Cage"])

with open('protagonist.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)