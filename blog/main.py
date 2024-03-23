from flask import Blueprint, abort
from flask import  render_template

app2Blg2 = Blueprint("hop_hip_bux", __name__, template_folder = "templates")


@app2Blg2.route("/blog/", methods=["GET"])
def FromTheBlog():
	#abort(404)
	return render_template("blog/main.html")


@app2Blg2.route("/blog/post/<int:uid>", methods=["GET"])
def FromTheBlogPost(uid):
	return f"blog id {uid}"
	
	
@app2Blg2.route("/blog/post/<int:uid>/edit", methods=["GET"])
def FromTheBlogPostEditing(uid):
	return f"blog editing {uid}"
	

@app2Blg2.route("/blog/post/<int:uid>/delete", methods=["GET"])
def FromTheBlogPostDelete(uid):
	return f"deleting the blog {uid}"
