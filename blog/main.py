from flask import Blueprint


app2Blg2 = Blueprint("hop_hip_bux", __name__, template_folder = "template")



@app2Blg2.route("/yoo_blog/", methods=["GET"])
def FromTheBlog():
	return "Xz  from the blogpage"
