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

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.
