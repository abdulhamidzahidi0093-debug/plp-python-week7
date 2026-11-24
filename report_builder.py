# Week 7 Assignment - The Report Builder

import csv

# Read learner information from the CSV file.
try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))

except FileNotFoundError:
    print("hubs.csv not found")
    rows = []

# Initialize the total score and pass count.
total = 0
passed = 0

# Calculate scores and count learners who passed.
for row in rows:
    score = int(row["score"])
    total += score

    if score >= 50:
        passed += 1

# Calculate the average safely.
if rows:
    average = round(total / len(rows), 1)
else:
    average = 0.0

failed = len(rows) - passed

# Write the results into a report file.
with open("report.txt", "w") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    f.write("Failed: " + str(failed) + "\n")
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")
