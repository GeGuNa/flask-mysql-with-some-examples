from flask import Blueprint, render_template, abort, make_response
from jinja2 import TemplateNotFound


app23z = Blueprint("q_contact", __name__, template_folder="templates")


@app23z.route("/page/contact/", methods=["GET"])
def ForContactPage():
	try:
		return render_template("contact/main.html2")
	except TemplateNotFound:
		#abort(404)
		qp123 = make_response("some problems kiddo")
		return qp123
