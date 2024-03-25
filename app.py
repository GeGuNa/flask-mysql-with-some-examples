from flask import Flask, request, redirect
from flask import g, render_template
import db as MySQL
import functions
import sec
from aww import awwqw
from blog.main import app2Blg2
from contact.main import app23z

#kekq = MySQL.fetch()


print(awwqw())

#print(kekq[0])
#print(kekq[0][0])
#print(kekq[0][1])
#print(kekq[0][2])


#q1 = MySQL.fetchOne("select * from user where id = %s", (7,))

#print(q1)


#functions.escape("ahaha \\ ")
#print(functions.escape("ahaha \\ "))



app = Flask(__name__)
app.register_blueprint(sec.app)
app.register_blueprint(app2Blg2)
app.register_blueprint(app23z)





@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404



@app.before_request
def check_authentication():
	g.xzzz = "klekz"
	print(request.endpoint)
	
	

@app.route("/", methods=['GET'])
def mmai2n():
	return render_template("home.html")
	
	
	
@app.route("/login", methods=['GET'])
def login():
	return render_template("login.html")

@app.route("/register", methods=['GET'])
def registration_2():
	return render_template("register.html")


@app.route("/apartment/<int:uid>", methods=['GET'])
def apartment_id(uid):
	
	tabl = "blog"
	col = "uid"
	uid2 = (uid)

	data = MySQL.fetchOneFromSpecific(tabl, col, uid2)
	
	if data is None:
		return redirect("/")
	
	return f" {data}"
	#return render_template("register.html")		

@app.route("/about")
def About_m():
	return render_template("about/main.html")



@app.route("/faq")
def Faq_main():
	return "faq"

	
@app.route("/services")
def Services_main():
	return "services"


@app.route("/partners_2/")
def Partners_main():
	return "Partners"	


@app.route("/pass_recovery/")
def Pass_rec_main():
	return render_template("user/recovery/main.html")	



	

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

