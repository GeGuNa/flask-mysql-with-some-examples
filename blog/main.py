from flask import Blueprint, abort
from flask import  render_template

app2Blg2 = Blueprint("hop_hip_bux", __name__, template_folder = "templates")


@app2Blg2.route("/blog/", methods=["GET"])
def FromTheBlog():
	
		FData = [
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
		]
	
		Fordinary = [
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
			{'name':'qweqwe',	'buh': 'kekz',	'num': '15','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe22','buh': 'kekz33',	'num': '16','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'}, 
			{'name':'qweqwe',	'buh': 'kekz',	'num': '17','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},  
			{'name':'qweqwe22','buh': 'kekz33',	'num': '18','pic':'/static/apartment/cbd17284cdabb02e39989c72aadba5fb4457984017.jpeg'},
		]
	
		#abort(404)
		return render_template("blog/main.html" ,Data=FData, Ford = Fordinary)


@app2Blg2.route("/blog/post/<int:uid>", methods=["GET"])
def FromTheBlogPost(uid):
	return f"blog id {uid}"
	
	
@app2Blg2.route("/blog/post/<int:uid>/edit", methods=["GET"])
def FromTheBlogPostEditing(uid):
	return f"blog editing {uid}"
	

@app2Blg2.route("/blog/post/<int:uid>/delete", methods=["GET"])
def FromTheBlogPostDelete(uid):
	return f"deleting the blog {uid}"
