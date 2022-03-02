import sqlite3

from click import option

db=sqlite3.connect("quiz.db")
cursor= db.cursor()

def execute_query(sql_query):
    with sqlite3.connect('quiz.db') as db:
        csr=db.cursor()
        result=csr.execute(sql_query)
        db.commit()
    return result


'''query="""DELETE FROM quiz_table WHERE crtop='option 1' or crtop='option 2'"""
execute_query(query)'''



sql_query="""select * from quiz_table"""
RESULT=execute_query(sql_query)
print(RESULT.fetchall())



'''sql_query="""create table quiz_table(question text unique,op1 text,op2 text,op3 text,crtop text)"""
execute_query(sql_query)
sql_query="""INSERT INTO quiz_table VALUES('this is which question','1st','2nd','3rd','3')"""
execute_query(sql_query)'''

'''sql_query="""select * from quiz_table"""
RESULT=execute_query(sql_query)
l=RESULT.fetchall()
questions_list=[]
option1_list=[]
option2_list=[]
option3_list=[]
crt_option=[]

for i in l:   
    questions_list.append(i[0])
    option1_list.append(i[1])
    option2_list.append(i[2])
    option3_list.append(i[3])
    crt_option.append(i[4])

print(questions_list)
print(option1_list)
print(option2_list)
print(option3_list)'''