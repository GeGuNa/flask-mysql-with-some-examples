#from db import mydb
#from db import execute_One_query 
from db import improved_mysql_query
from flask import session


def escape(text: str):

	"""

		<: &lt;
		>: &gt;
		\: &#92;
		/: &#47;
		': &apos; or &#39;
		": &quot; or &#34;

	"""
		
	REPLACEMENTS = [
		("\\", "&#92;"),
		("/", "&#47;"),
		("'", "&#39;"),
		("\"", "&#34;"),
		("<", "&lt;"),
		(">", "&gt;"),
	]
	
	
	for x,y in REPLACEMENTS:
		text = text.replace(x,y)
	
	return text
	#print(text)
	
	
def FforCheckuSerCredentials(username, password, type_1="no_return"):
	
	


		dd_si1 = (session['uid_nm'], session['pswd'])
		
		dd_si1 = (username, password)
		
		
		query = "select * from `user` where `username` = %s and `password` = %s"
		result = improved_mysql_query(query, dd_si1, fetchall=False)
	
	
		if type_1 == "no_return":
			""" """
		else:
			return result
	


#escape("test '   \" ")
