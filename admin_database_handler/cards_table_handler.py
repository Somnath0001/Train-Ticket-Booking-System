# cards_table_handler.py

import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('ticket_booking.db')
cur = con.cursor()

# cur.execute('''DROP TABLE cards''')

# Create Cards table
cur.execute('''CREATE TABLE IF NOT EXISTS cards
            (user_id TEXT,
            card_type TEXT,
            card_no INT,
            valid_from TEXT,
            valid_to TEXT,
            cvv INT)''')

# Insert values to the Cards table
cur.execute('''INSERT INTO cards VALUES('som1', 'CREDIT', 1234123412341234, '07/22', '07/25', 123)''')

# View everything from Cards table
for row in cur.execute('''SELECT * FROM cards'''):
    print(row)

# Commit and close the database connection
# con.commit()
con.close()