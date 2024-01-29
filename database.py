import sqlite3

def create_cashin_table_if_not_exists():
    conn = sqlite3.connect('inventory.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS CASH_IN 
                (amount INTEGER, fee INTEGER, date TEXT)''')
    
    conn.close()

def create_cashout_table_if_not_exists():
    conn = sqlite3.connect('inventory.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS CASH_OUT 
                (amount INTEGER, fee INTEGER, date TEXT)''')
    
    conn.close()

def fetch_cashin_data():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT amount, fee, date FROM CASH_IN")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_cashout_data():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT amount, fee, date FROM CASH_OUT")
    rows = cursor.fetchall()
    conn.close()
    return rows