pb = 1
jelly = 0
slices = 11

#First Goal
if pb and jelly and slices/2 >= 1:
    print "You can make a sandwich!"
else:
    print "No PB&J for you :("

#Second Goal
if pb and jelly and slices/2 >= 1:
    print "You can make {0} sandwiches!".format(min(pb,jelly,slices/2))
else:
    print "No PB&J for you :("

#Third Goal
if pb and jelly and slices/2 >= 1 and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(min(pb,jelly,slices/2))
elif slices % 2 == 1 and jelly > slices/2 and pb > slices/2:
    print "You can make {0} sandwiches and an open faced one.".format(min(pb,jelly,slices/2))
elif slices % 2 == 1 and jelly and pb >= 1:
    print "You can make {0} sandwiches.".format(min(pb,jelly,slices/2))
else:
    print "No PB&J for you :("

#Fourth Goal
if pb and jelly and slices/2 >= 1 and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(min(pb,jelly,slices/2))
elif slices % 2 == 1 and jelly > slices/2 and pb > slices/2:
    print "You can make {0} sandwiches and an open faced one.".format(min(pb,jelly,slices/2))
elif slices % 2 == 1 and jelly and pb >= 1:
    print "You can make {0} sandwiches.".format(min(pb,jelly,slices/2))
else:
    if pb == 0:
        print "You need peanut butter."
    if jelly == 0:
        print "You need jelly."
    if slices == 0:
        print "You need bread."

#Fifth Goal
if pb and jelly and slices/2 >= 1 and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(min(pb,jelly,slices/2))
elif slices % 2 == 1 and jelly > slices/2 and pb > slices/2:
    print "You can make {0} sandwiches and an open faced one.".format(min(pb,jelly,slices/2))
elif slices % 2 == 1 and jelly and pb >= 1:
    print "You can make {0} sandwiches.".format(min(pb,jelly,slices/2))
elif pb and slices/2 >=1 and jelly == 0:
    print "You can make a peanut butter sandwich, but what kind of person would do that? Gross."
else:
    if pb == 0:
        print "You need peanut butter."
    if slices == 0:
        print "You need bread."
