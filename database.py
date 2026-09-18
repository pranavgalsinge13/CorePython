# database connectivity

'''import sqlite3 as sq

# connect to SQLite database
con = sq.connect("mydata.db")
cur = con.cursor()

# create table in database
# cur.execute("create table emp(id int, name varchar(20))")

# insert records into the table
cur.execute("insert into emp values(1, 'Pranav')")
cur.execute("insert into emp(id, name) values(?, ?)", (2, 'Tanmay'))  # this query mainly used in flask

con.commit()
con.close()'''

# execute many records at once

'''import sqlite3 as sq
con= sq.connect("mydata.db")
cur= con.cursor()
I=[(3, 'Jay'), (4, 'Rohit'), (5, 'Hitesh')]
cur.executemany("insert into emp(id, name) values(?, ?)", I)
con.commit()
con.close()'''

# select records from the table

import sqlite3 as sq
con= sq.connect("mydata.db")
cur= con.cursor()

mydata=cur.execute("select * from emp")
#print(mydata)  # this will print the object reference of the data

for row in mydata:
    print(row[0], row[1])  # this will print the data in the table


# fetchall() method is used to fetch all the records from the table and return them as a list of tuples.



# fetchone() method is used to fetch the next record from the table and return it as a tuple.
# If there are no more records, it returns None.


# update records in the table

cur.execute("update emp set name='Pranavvv' where id=1")

# delete records from the table

cur.execute("delete from emp where id=5")
