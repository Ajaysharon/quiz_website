from distutils.log import debug
from flask import Flask, render_template,request
import sqlite3


app = Flask(__name__, template_folder='template', static_folder='static')

def execute_query(sql_query):
    with sqlite3.connect('quiz.db') as db:
        csr=db.cursor()
        result=csr.execute(sql_query)
        db.commit()
    return result


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/general")
def gen_details():
    return render_template("gen details.html")


@app.route("/student")
def student():
    return render_template("student.html")


@app.route("/teacher")
def teacher():

    return render_template("teacher.html")


@app.route("/question",methods=["POST", "GET"])
def question():
    if request.method == "GET":
        print("a")
        return render_template("questions.html")
    else:
        question = request.form['Add question']
        op1= request.form['Type option 1']
        op2= request.form['Type option 2']
        op3= request.form['Type option 3']
        crt_op= request.form['Answer']
        sql_query="insert into quiz_table values('"+question+"','"+op1+"','"+op2+"','"+op3+"','"+crt_op+"')"
        execute_query(sql_query)
        return render_template("questions.html")


@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/mcq")
def mcq():
    sql_query="""select * from quiz_table"""
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
        length=len(questions_list)
    return render_template("mcq.html",
        questions_list=questions_list,
        option1_list=option1_list,
        option2_list=option2_list,
        option3_list=option3_list,
        length=length
        )


if __name__ == "__main__":
    app.run(debug=True)
