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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Find all calls that make outgoing calls never receive incoming calls
outgoing_calls = set()
caller = set()

for row in calls:
    caller.add(row[0])
    outgoing_calls.add(row[1])


sender = set()
outgoing_texts = set()
for row in texts:
    sender.add(row[0])
    outgoing_texts.add(row[1])


result = caller - outgoing_calls - sender - outgoing_texts
print("These numbers could be telemarketers: ")
for t in sorted(result):
    print(t)
