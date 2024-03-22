from flask import Blueprint

app = Blueprint("BBB", __name__, template_folder="templates")

@app.route("/bbb")
def BBB_q():
	return "test"


@app.route("/bbb2")
def BBB_q2():
	return "test2"


@app.route("/bbb2/<int:page>")
def BBB_q23(page):
	return f"test3 {page}"
