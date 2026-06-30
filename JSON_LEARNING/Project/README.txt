⭐ What JSON really is (in the simplest possible way)
JSON = JavaScript Object Notation  
It is just a text format for storing structured data.

It looks like Python dictionaries, but with stricter rules.

⭐ Why JSON is important as a Verification Engineer
Because JSON is the easiest way to exchange data between:

Python scripts

UVM/SystemVerilog

RTL tools

Reference models

CI/CD systems

JSON is the glue between all these worlds.

Storing data in a JSON file has several powerful advantages -
working in Python automation and SoC/Verification workflows. JSON is popular because it is simple, universal, and extremely flexible.

⭐ Advantages of storing data in JSON 

Summary Table

Advantage	   	Why it matters
*********************************************************
Human‑readable		Easy to debug and edit
Lightweight		Minimal syntax, fast to parse
Language‑independent	Works with Python, UVM, C, etc.
Structured		Perfect for configs and test data
Built‑in Python support	No installation needed
Great for automation	Used in CI/CD, dashboards
Nested data		Ideal for registers, sequences
Portable		Works everywhere
Industry standard	Used in APIs, cloud, verification

*Terminology used for JSON

Action				Meaning
*****************************************************************
Validate JSON			Check if JSON syntax is correct
Parse JSON			Convert JSON → Python dict
Pretty‑print JSON		Display JSON nicely
Use JSON in verification	Pass configs, stimulus, registers

*Differences between 'r+' and 'a' in JSON

1. with open("info.json", "r+") — READ + WRITE (overwrite from the beginning)
✔ What it does
Opens the file for reading and writing

Does NOT clear the file

File pointer starts at position 0

When you write, it overwrites existing content from the beginning

❗ Danger
If you do:
with open("info.json", "r+") as f1:
    json.dump(data, f1, indent=4)

You overwrite the beginning of the file, but old leftover content remains at the end unless you truncate.

So you MUST do:
f1.seek(0)
json.dump(data, f1, indent=4)
f1.truncate()
Otherwise your JSON becomes corrupted.

⭐ 2. with open("info.json", "a") — APPEND mode
✔ What it does
Opens the file for writing only

File pointer moves to the end of the file

Does NOT erase or overwrite anything

New content is added after existing content

❗ Why this is wrong for JSON
Appending JSON creates invalid JSON:

Example:

Original file:
{"name": "Sam"}
Append:
{"Designation": "SOC Verification Engineer"}
Final file then becomes:
{"name": "Sam"}{"Designation": "SOC Verification Engineer"}
This is not a valid JSON, so "a" mode should never be used for updating JSON files.

⭐ Summary Table

Mode	Meaning		Clears file?	Good for JSON?
******************************************************
r+	Read + Write	❌ No		✔ Yes (with truncate)
a	Append		❌ No		❌ No (breaks JSON)
w	Write		✔ Yes		✔ Yes (safe overwrite)

⭐ Best way to update JSON safely
with open("info.json", "r+") as f:
    data = json.load(f)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

