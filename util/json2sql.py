import json
import sqlite3

# sql first
con = sqlite3.connect("triva.db")
cur = con.cursor()

# mAke the table
cur.execute(''' 
CREATE TABLE IF NOT EXISTS trivia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    choices TEXT NOT NULL,
    UNIQUE(category, question)
)
''')

# json import
with open('grouped_questions.json', 'r', encoding='utf-8') as trivia_json:
    data = json.load(trivia_json)

counter = 0

# make some gd data, iterate that shit into the table
for category, questions in data.items():
    for q in questions:
        q['category'] = category # To ensure unique tag not triggered
        
        if not all(k in q for k in ("question", "answer", "choices")):
            print(f"\n!!! Skipping malformed question in category '{category}': {q}\n")
            counter+=1
            continue
    
        question = q["question"]
        answer = q["answer"]
        choices = json.dumps(q["choices"])  # store list as JSON text

        con.execute(
            "INSERT OR IGNORE INTO trivia (category, question, answer, choices) VALUES (?, ?, ?, ?)",
            (category, question, answer, choices)
        )

print(counter)
print(counter)
print(counter)

# safety
con.commit()
con.close()