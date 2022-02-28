import sqlite3

db=sqlite3.connect('quiz.db')
cursor=db.cursor()

query="select crtop from quiz_table where sno=1"
cursor.execute(query)
result = cursor.fetchall()
crt_op=int(result[0][0])
sel_op=int(input("enter the option :"))

if sel_op==crt_op:
    print("Successful....")
else: 
    print("Fail!!!")





