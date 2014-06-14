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


editme = """<br>
<a href="javascript:void(0)" 
onclick='document.location=document.location+"/edit";'> 
    Edit article
</a> """
delme =""" 
<br><a href="javascript:void(0)"
onclick="if (confirm('Are you sure you want to delete this thing from the database?')) {
        document.location=document.location+'/del';
} else {
        // Do nothing!
}">Delete entry</a>
"""
