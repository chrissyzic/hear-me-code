# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

def dedupe(file1, file2):
    with open(file1, "r") as first_file:
        first_file = first_file.read().split("\n")

    with open(file2, "r") as second_file:
        second_file = second_file.read().split("\n")

    combined_file = first_file + second_file
    combined_list = list(set(combined_file))
    return combined_list

print dedupe('film_screening_attendees.txt','happy_hour_attendees.txt')


# Goal 2: Who came to *both* your Film Screening and your Happy hour?


