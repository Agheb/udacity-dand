"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
## Turn into sets

distinct_texts = set()
for row in texts:
    for elem in row[0:2]:
        distinct_texts.add(elem)


distinct_calls = set()
for row in calls:
    for elem in row[0:2]:
        distinct_calls.add(elem)


res = distinct_calls.union(distinct_texts)


print(f"""There are {len(res)} different telephone numbers in the records""")
