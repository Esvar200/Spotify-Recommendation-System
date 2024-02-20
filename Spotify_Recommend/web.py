from flask import Flask, request, \
    render_template
app = Flask(__name__)

import pandas as pd


@app.route("/")
def main():
    return render_template("index0.html")


@app.route("/user")
def Login():
    user_login = [str(i) for i in (request.form.values())]

    import pymysql as pms
    conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="Esvar#2040",
                   db="ml")
    cur = conn.cursor()
    cur.execute("select * from login")
    output = cur.fetchall()

    d="Invalid Login credentials"
    if ("esvar","abcd") in output :
        return render_template("index.html")
    else:
        return render_template("index0.html",data=d)


@app.route("/predict", methods=['post'])
def pred():
    features = [str(i) 
                for i in 
                (request.form.values())]
    df= pd.read_csv("out.csv")
    df = pd.DataFrame(df.nlargest(6,features))
    a=df.iloc[:,0].values
    return render_template("success.html", data=a)
    
if __name__=='__main__':
    app.run(host='localhost',port=5000)



    
    
    
    
    
    