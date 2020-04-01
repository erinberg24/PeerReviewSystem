import sqlite3
import random

conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Users(email TEXT, password TEXT, fname TEXT, lname TEXT, eagleid INTEGER)')
        
def data_entry():
    c.execute("INSERT INTO Users VALUES('bergec@bc.edu', '12345', 'Erin', 'Berg', 57282704)")
    c.execute("INSERT INTO Users VALUES('nugentb@bc.edu', '12345', 'Brennan', 'Nugent', 14362408)")
    c.execute("INSERT INTO Users VALUES('nadeaudy@bc.edu', '12345', 'Dylan', 'Nadeau', 86753097)")
    c.execute("INSERT INTO Users VALUES('wukt@bc.edu', '12345', 'Cecilia', 'Wu', 25094592)")
    conn.commit()
    c.close()
    conn.close()

def generate_password():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    password =  "".join(random.sample(s,passlen))
    print(password)
    return password


create_table()
data_entry()

generate_password()
