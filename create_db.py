import mysql.connector
def create_db():
    con = mysql.connector.connect(host='localhost', user='root', password='', db='ims')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY,employee_name TEXT,email TEXT,gender TEXT,contact TEXT,dob TEXT,doj TEXT,pass TEXT,utype TEXT,address TEXT);")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY,name text,contact text,description text);")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY,name text);")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY,Category text,Supplier text,name text,price text,qty text,status text);")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS pending(eid INTEGER PRIMARY KEY,employee_name TEXT,email TEXT,gender TEXT,contact TEXT,dob TEXT,doj TEXT,pass TEXT,utype TEXT,address TEXT);")
    con.commit()
    #After creating tables make sure to put Auto Increment on pid,cid,eid,invoice
create_db()