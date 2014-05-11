# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' }, 
    'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner 

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

#Two methods that get the same result!

#First method is the .items() method

for contact, info in contacts.items(): #creates another dictionary ("info") of the nested dictionaries, and you can all those items by key, e.g. info['phone']
    print "{0}'s contact information is:\nPhone: {1}\nTwitter: {2}\nGithub: {3}".format(contact,info['phone'],info['twitter'],info['github']) 

#The other method is the .keys() method, doesn't create the info variable, so you have to type more to call the list from the keys:
for contact in contacts.keys():
    print "{0}'s contact information is:".format(contact) #print the key
    print "Phone: {0}".format(contacts[contact]['phone']) #call the info tie to the 'phone' key in the dictionary nested within the 'contacts' dictionary
    print "Twitter: {0}".format(contacts[contact]['twitter'])
    print "Github: {0}".format(contacts[contact]['github']) 
    
# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

for contact, info in contacts.items():
    print """<table border="1">"""
    print "<tr>"
    print """<td colspan="2"> {0} </td>""".format(contact)
    print "</tr>"
    print "<tr>"
    print "<td> Phone: {0} </td>".format(info['phone'])
    print "<td> Twitter: {0} </td>".format(info['twitter'])
    print "<td> Github: {0} </td>".format(info['github'])
    print "</tr>"
    print "</table>"

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

with open ("contacts.html", "w") as contacts_html:
    for contact, info in contacts.items():
        contacts_html.write("""<table border="1">""")
        contacts_html.write("<tr>")
        contacts_html.write("""<td colspan="2"> {0} </td>""".format(contact))
        contacts_html.write("</tr>")
        contacts_html.write("<tr>")
        contacts_html.write("<td> Phone: {0} </td>".format(info['phone']))
        contacts_html.write("<td> Twitter: {0} </td>".format(info['twitter']))
        contacts_html.write("<td> Github: {0} </td>".format(info['github']))
        contacts_html.write("</tr>")
        contacts_html.write("</table>")

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).

with open ('contacts.csv', 'r') as contacts_csv:
    contacts = contacts_csv.read().split("\n")

for index, information in enumerate(contacts):
    contacts[index] = information.split(",")
    print """<table border="1">"""
    print "<tr>"
    print """<td colspan="2"> {0} </td>""".format(contacts[index][0])
    print "</tr>"
    print "<tr>"
    print "<td> Phone: {0} </td>".format(contacts[index][1])
    print "<td> Twitter: {0} </td>".format(contacts[index][3])
    print "<td> Github: {0} </td>".format(contacts[index][2])
    print "</tr>"
    print "</table>"
