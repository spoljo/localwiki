newentry = """
<input type="text" name="genlink" value="">
<input type="button" value="Create new entry"
onclick="window.location.href=document.getElementsByName('genlink')[0].value">
"""

content_form = """
<form method="POST"><textarea name="content" type="text"
rows="40" cols="120"> {content} </textarea><br><input 
type="submit" value="submit" /></form>
"""

