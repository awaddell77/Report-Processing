#transform_functions

def remove_unicode(text):

	#removes all non-ascii characters
	#also removes extended ascii characters
	clean_text = ''
	for i in range(0, len(text)):
		val = ord(text[i])
		if val <= 127: clean_text += text[i]
	return clean_text

