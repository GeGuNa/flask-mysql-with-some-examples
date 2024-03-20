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
	


#escape("test '   \" ")
