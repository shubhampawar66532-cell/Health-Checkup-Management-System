import sqlite3
import pandas as pd

# CSV वाचा
df = pd.read_csv("health.csv")

# Database तयार करा
conn = sqlite3.connect("health.db")

# Table तयार करून डेटा सेव्ह करा
df.to_sql("patients", conn, if_exists="replace", index=False)

conn.close()

print("Database Created Successfully!")