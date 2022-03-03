from distutils.log import debug
from flask import Flask, render_template,request
import datetime
import sqlite3


app = Flask(__name__, template_folder='template', static_folder='static')

score=0
sel_option=[]
def execute_query(sql_query):
    with sqlite3.connect('quiz.db') as db:
        csr=db.cursor()
        result=csr.execute(sql_query)
        db.commit()
    return result

def get_table_details(options):
    sql_query="""select * from quiz_table"""
    RESULT=execute_query(sql_query)
    l=RESULT.fetchall()
    questions_list=[]
    sub_topic_list=[]
    option1_list=[]
    option2_list=[]
    option3_list=[]
    crt_option=[]
    
    for i in l:   
        questions_list.append(i[0])
        sub_topic_list.append(i[1])
        option1_list.append(i[2])
        option2_list.append(i[3])
        option3_list.append(i[4])
        crt_option.append(i[5])
        length=len(questions_list)
    if options=='get_length':
        return length
    if options=='get_questions':
        return questions_list
    elif options=='get_details':
        return questions_list,sub_topic_list,option1_list,option2_list,option3_list,crt_option,length 


@app.route("/",methods=["POST", "GET"])
def login():
    if request.method == "GET":
        print("a")
        return render_template("login.html", utc_dt=datetime.datetime.utcnow())
    else:
        print("b")
        global regno
        regno=request.form['regno']
        password=request.form['psw']
        print(regno)
        query="select * from login where regno='"+regno+"' and password = '"+password+"'"
        l=execute_query(query)
        l=l.fetchall()

        if len(l)==0:
            print("sorry,Incorrect details")
        else:
            return render_template("gen details.html")
            
        return render_template("login.html", utc_dt=datetime.datetime.utcnow())
        

@app.route("/general")
def gen_details():
    return render_template("gen details.html")


@app.route("/student")
def student():
    print(regno)
    return render_template("student.html",regno=regno)

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/teacher")
def teacher():
    return render_template("teacher.html")


@app.route("/result")
def result():
    out_off=get_table_details("get_length")
    return render_template("result.html",score=score,out_off=out_off,regno=regno)

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")

@app.route("/question",methods=["POST", "GET"]) 
def question():
    if request.method == "GET":
        print("a")
        return render_template("question.html")
    else:
        question = request.form['Add question']
        sub_topic=request.form['sub topic']
        op1= request.form['Type option 1']
        op2= request.form['Type option 2']
        op3= request.form['Type option 3']
        crt_op= request.form['Answer']
        print(sub_topic)
        sql_query="insert into quiz_table values('"+question+"','"+sub_topic+"','"+op1+"','"+op2+"','"+op3+"','"+crt_op+"')"
        execute_query(sql_query)
        return render_template("question.html")


@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/view")
def view():
    questions=get_table_details("get_questions")[::-1]
    length=len(questions)
    
    return render_template("view question.html",length=length,questions=questions)


@app.route("/mcq",methods=["POST", "GET"])
def mcq():
    print("g")
    global sel_option
    q,st,op1,op2,op3,crtop,l=get_table_details("get_details")
    

    if request.method == "GET":
        print("a_mcq")
        return render_template("mcq.html",
        questions_list=q,
        sub_topic_list=st,
        option1_list=op1,
        option2_list=op2,
        option3_list=op3,
        length=l
        )
    else:
        print("b_mcq")
        global score
        score=0
        for i in range(l):
            selected_option= request.form[''+str(i)+'']
            sel_option.append(selected_option)

        for i in range(l):
            if sel_option[i]==crtop[i]:
                score+=1

        print(sel_option)
        print(crtop)
        print("YOUR SCORE :",score,"/",len(q))
        sel_option=[]
        out_off=get_table_details("get_length")
        return render_template("result.html",score=score,out_off=out_off)


if __name__ == "__main__":
    app.run(debug=True)
