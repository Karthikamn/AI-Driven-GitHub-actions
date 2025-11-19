# insecure_example.py
# 🚨 This file is intentionally insecure for testing security scanning workflows.

import os
import sqlite3
import ssl

# Hardcoded AWS keys (fake)
AWS_ACCESS_KEY_ID = "AKIA1234567890ABCDE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Hardcoded password (fake)
db_password = "SuperSecretP@ssword1234"

# Insecure eval usage
user_input = "os.system('rm -rf /')"
eval(user_input)  # 🔥 DO NOT USE IN PRODUCTION

# Insecure SQL query (SQL injection risk)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
username = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + username + "'"  # 🚨 Injection possible
cursor.execute(query)

# Insecure TLS (skip certificate verification)
ssl_context = ssl._create_unverified_context()

print("Done with insecure stuff...")


Why this file will get flagged:
Regex rules will catch:
AWS key format
AWS secret format
Hardcoded password string
eval() usage

SQL concatenation pattern
verify=False / unverified TLS (if in string form, but here AI should still catch it)

AI model will catch:
eval(user_input) as unsafe
SQL injection risk in string concatenation

Use of unverified TLS context
Presence of secrets
