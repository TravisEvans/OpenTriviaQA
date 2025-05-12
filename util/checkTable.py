import sqlite3
import json

con = sqlite3.connect("triva.db")
cur = con.cursor()

# Count total questions
cur.execute("SELECT COUNT(*) FROM trivia")
total = cur.fetchone()[0]
print(f"Total questions: {total}")

# one row / q
# cur.execute("""SELECT category, question, answer, choices
# FROM trivia
# ORDER BY RANDOM()
# LIMIT 1;""") # Peek at one question
# row = cur.fetchone()

# whole table
cur.execute("""SELECT category, question, answer, choices
FROM trivia""")
rows = cur.fetchall()


for idx, row in enumerate(rows, 1):
    category, question, answer, choices_json = row
    try:
        choices = json.loads(choices_json)
    except json.JSONDecodeError:
        choices = ["[Invalid JSON]"]

    print(f"Question {idx}:", end=" ")
    print(f"{question}", end=" ")
    # print(f"Category: {category}", end=" ")
    for i, choice in enumerate(choices, 1):
        print(f"  {chr(64+i)}. {choice}", end=" ")
    print(f"Answer: {answer}")

con.close()
