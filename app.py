from flask import Flask
from flask import g, render_template
import db as MySQL
import functions

#kekq = MySQL.fetch()


#print(kekq[0])
#print(kekq[0][0])
#print(kekq[0][1])
#print(kekq[0][2])


#q1 = MySQL.fetchOne("select * from user where id = %s", (7,))

#print(q1)


#functions.escape("ahaha \\ ")
#print(functions.escape("ahaha \\ "))



app = Flask(__name__)


@app.before_request
def check_authentication():
	g.xzzz = "klekz"


@app.route("/", methods=['GET'])
def mmai2n():
	return render_template("home.html")
	
	
	
@app.route("/login", methods=['GET'])
def login():
	return render_template("login.html")
		
	

@app.route("/q21")
def Mainq():
	return f'test  {g.xzzz}'


@app.route("/xz")
def Main2():
	return render_template("main.html")



#allowing only integers
@app.route("/user/<int:id>")
def user_id(id):
    return f"{id}"


##url doesn't matter 
@app.route("/user_id/<id>")
def user_with_jstid(id):
    return f"{id}"


#print(__name__)

#if __name__ == '__main__':
    #app.run(debug=True)

