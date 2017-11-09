import json, sqlite3

# Create DB
conn = sqlite3.connect('log.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE logs
             (timestamp text, IP text, level text, user text, worker text)''')



file = open("nodio-2016-11-23-0-json.txt")

records = [(dict_entry["timestamp"],dict_entry["IP"],dict_entry["level"],dict_entry["user"],dict_entry["worker_uuid"] )
           for dict_entry in [ json.loads(line) for line in file]]
print records[:5]

c.executemany("INSERT INTO logs VALUES (?,?,?,?,?)", records)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()