from flask import Blueprint


app2Blg2 = Blueprint("hop_hip_bux", __name__, template_folder = "templates")



@app2Blg2.route("/blog/", methods=["GET"])
def FromTheBlog():
	return "main blogs"


@app2Blg2.route("/blog/post/<int:uid>", methods=["GET"])
def FromTheBlogPost(uid):
	return f"blog id {uid}"
	
