from flask import Flask
from flask import g
import db as MySQL

#kekq = MySQL.fetch()


#print(kekq[0])
#print(kekq[0][0])
#print(kekq[0][1])
#print(kekq[0][2])


#q1 = MySQL.fetchOne("select * from user where id = %s", (7,))

#print(q1)

app = Flask(__name__)


@app.before_request
def check_authentication():
	g.xzzz = "klekz"



@app.route("/")
def Main():
	return f'test  {g.xzzz}'


#print(__name__)

#if __name__ == '__main__':
    #app.run(debug=True)

