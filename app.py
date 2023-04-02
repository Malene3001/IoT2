from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure

app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/statistics", methods=['POST','GET'])
def statistics():
    con = sql.connect("db_statistics.db", check_same_thread=False)
    cur = con.cursor()
    cur.execute("SELECT * FROM TemperatureANDHumidity ORDER BY Time DESC LIMIT ")
    data = cur.fetchall()
    dates = []
    temps = []
    hums = []
    for row in reversed(data):
        dates.append(row[0])
        temps.append(row[1])
        hums.append(row[2])
    return dates, temps, hums

def plotTemp():
    times, temps, hums = statistics(4)
    print("times:", times)
    ys = temps
    xs = times
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis="x", which="both", rotation=30)
    ax = fig.subplots()
    ax.set_facecolor("#000") # inner plot background color HTML black
    fig.patch.set_facecolor('#000') # outer plot background color HTML black
    ax.plot(xs, ys, linestyle = 'dashed', c = '#11f', linewidth = '1.5',
     marker = 'o', mec = 'hotpink', ms = 10, mfc = 'hotpink' )
    ax.set_xlabel('X-axis ')
    ax.set_ylabel('Y-axis ')
    ax.xaxis.label.set_color('hotpink') #setting up X-axis label color to hotpink
    ax.yaxis.label.set_color('hotpink') #setting up Y-axis label color to hotpink
    ax.tick_params(axis='x', colors='white') #setting up X-axis tick color to white
    ax.tick_params(axis='y', colors='white') #setting up Y-axis tick color to white
    ax.spines['left'].set_color('blue') # setting up Y-axis tick color to blue
    ax.spines['top'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['bottom'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['right'].set_color('blue') #setting up above X-axis tick color to blue
    fig.subplots_adjust(bottom=0.3) 
    ax.tick_params(axis="x", which="both", rotation=30) 
    buf = BytesIO()
    fig.savefig(buf, format=("png"))
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("statistics.html", data=data)

def plotHum():
    times, temps, hums = statistics(4)
    ys = hums
    xs = times
    fig = Figure()
    ax = fig.subplots()
    ax.set_facecolor("#000")
    fig.patch.set_facecolor('#000') # outer plot background color HTML black
    ax.plot(xs, ys, linestyle = 'dashed', c = '#11f', linewidth = '1.5',
     marker = 'o', mec = 'hotpink', ms = 10, mfc = 'hotpink' )
    ax.set_xlabel('X-axis ')
    ax.set_ylabel('Y-axis ')
    ax.xaxis.label.set_color('hotpink') #setting up X-axis label color to hotpink
    ax.yaxis.label.set_color('hotpink') #setting up Y-axis label color to hotpink
    ax.tick_params(axis='x', colors='white') #setting up X-axis tick color to white
    ax.tick_params(axis='y', colors='white') #setting up Y-axis tick color to white
    ax.spines['left'].set_color('blue') # setting up Y-axis tick color to blue
    ax.spines['top'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['bottom'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['right'].set_color('blue') #setting up above X-axis tick color to blue
    fig.subplots_adjust(bottom=0.3) 
    ax.tick_params(axis="x", which="both", rotation=30) 
   
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    #print(data)
    return data

@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        uname=request.form['Product']
        contact=request.form['udløbsdato']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("insert into users(Product,udløbsdato) values (?,?)",(uname,contact))
        con.commit()
        flash('Product Added','success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:uid>",methods=['POST','GET'])
def edit_user(uid):
    if request.method=='POST':
        uname=request.form['Product']
        contact=request.form['udløbsdato']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("update users set Product=?,udløbsdato=? where UID=?",(uname,contact,uid))
        con.commit()
        flash('Product Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)
    
@app.route("/delete_user/<string:uid>",methods=['GET'])
def delete_user(uid):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("delete from users where UID=?",(uid,))
    con.commit()
    flash('Product Deleted','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)