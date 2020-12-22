from flask import Flask, render_template, request
import socket  
from flask import request, abort, make_response
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

app = Flask(__name__)

mylist=[]
mylist.append("Welcome")
@app.route('/')
def chat1():
   return render_template('chat1.html')

@app.route('/chat2',methods = ['POST'])
def chat2():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('redirect.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/chat3',methods = ['POST', 'GET'])
def chat3():
   if request.method == 'POST':
        name = request.cookies.get('userID')
        mylist[0] = name
        #result = request.form
        mylist.append(name + " : " + request.form['msg'])
        #result = mylist 
        return render_template("chat3.html",result = mylist)

if __name__ == '__main__':
   app.run(debug = True)