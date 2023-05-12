from flask import Flask,request,rendertemplate
app=Flask(__name__)
@app.route(1/1)
def hello():
	name="Ivan"
	number="+7 123 456 78 90"
	return render_template("hello.html",name=name,number=number)
