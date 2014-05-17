# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py

with open ("states.csv","r") as states_file: #opens .csv file as read only
    something = states_file.read().split("\n") #creates a list ("something") where each item is a row in the .csv file, saved as a string - e.g. "AL,Alabama"
    
print "<select>"
for index, state in enumerate(something): #generate the index along with each item of the list that is being looped over:
    something[index] = state.split(",") #splits each item/string (state) in the list at a comma
    print """<option value="{0}">{1}</option>""".format(something[index][0],something[index][1]) #could also define a variable above this line: abbrevs = something[index][0]
print "</select>"

#the way to call these values outside of the for loop is like this
print something[3][1] #will return "Arkansas"
print something[13][0] #will return "IL'
print something[1] #will return ['AK', 'Alaska']


# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

with open ("states.csv", "r") as states_file:
    states = states_file.read().split("\n")
    
with open ("lesson03_playtime_states.html","w") as states_html: #open and create HTML file, tell python you want to write to it as a...list?
    states_html.write("<select>\n") #basically, instead of printing, add that string to the HTML file just created
    for index, state in enumerate(states): #same dealio as challenge 1
        states[index] = state.split(",")
        states_html.write("""<option value="{0}">"{1}"</option>\n""".format(states[index][0],states[index][1]))
    states_html.write("</select>")


# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>

# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>

with open ("states_info.csv", "r") as states_info_file:
    states_demographics = states_info_file.read().split("\n")
    states_demographics.pop(0) #remove the header row from the states_demographics list
    print states_demographics

with open ("states_info.html", "w") as states_info_html:
    for index, state in enumerate(states_demographics):
        states_demographics[index] = state.split(",")
        states_info_html.write("""<table border="1">\n<tr>\n<td colspan="2"> {0} </td>\n</tr>""".format(states_demographics[index][1]))
        states_info_html.write("""<tr>\n<td> Rank: {0} </td>\n<td> Percent: {1} </td>\n</tr>""".format(states_demographics[index][0], states_demographics[index][4]))
        states_info_html.write("""<tr>\n<td> US House Members: {0} </td>\n<td>Population: {1} </td>\n</tr>\n</table>""".format(states_demographics[index][3], states_demographics[index][2]))

#how can I remove the quotation marks from around the state name and percentage?

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.

#I am still working on this one, but here are random snippets of code that look like they might address this challenge.
<select id="select1" size="1" style="background-color:#FFFFD7">
<option>Choose a Position</option>
<option value="1">Job!</option>
<option value="2">Job!</option>
<option value="3">Job!</option>
<option value="4">Job!</option>
<option value="5">Job!</option>
<option value="6">Job!</option>
<option value="7">Job!</option>
<option value="8">Job!</option>
<option value="9">Job!</option>
</select>    
And I have a jquery script that I tried to hack together.

    <script type="text/javascript">
    jQuery(document).ready(function() {
        jQuery("#select1").change(function(){
            var jump = jQuery("#select1").val();
            var new_position = jQuery('#job'+jump).offset();
            window.scrollTo(new_position.left,new_position.top);
            return false;
        });​
    }
    </script>

# http://stackoverflow.com/questions/11147258/using-jquery-to-link-dropdown-to-anchor-text    

#And here is smore code from another site:
<script>
function favBrowser()
{
var mylist=document.getElementById("myList");
document.getElementById("favorite").value=mylist.options[mylist.selectedIndex].text;
}
</script>
</head>

<body>
<form>
Select your favorite browser:
<select id="myList" onchange="favBrowser()">
for index, state in enumerate(states):
    print """<option>Google Chrome</option>""".format()
  <option>Firefox</option>  
  <option>Internet Explorer</option>
  <option>Safari</option>
  <option>Opera</option>
</select>
<p>Your favorite browser is: <input type="text" id="favorite" size="20"></p>
</form>
</body>
