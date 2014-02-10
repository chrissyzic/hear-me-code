pb = 1
jelly = 0
slices = 5

#First Goal
if pb and jelly and slices/2 >= 1:
    print "You can make a sandwich!"
else:
    print "No PB&J for you :("

#Second Goal
if pb and jelly and slices/2 >= 1:
    if pb > 1 and jelly > 1 and slices/2 > 1:
        plural = "es"
    else:
        plural = ""
    print "You can make {0} sandwich{1}!".format(min(pb,jelly,slices/2),plural)
else:
    print "No PB&J for you :("

#Third Goal
if pb and jelly and slices/2 >= 1 and slices % 2 == 0:
    if pb > 1 and jelly > 1 and slices/2 > 1:
        plural = "es"
    else:
        plural = ""
    print "You can make {0} sandwich{1}!".format(min(pb,jelly,slices/2),plural)
elif slices % 2 == 1 and jelly > slices/2 and pb > slices/2:
    print "You can make {0} sandwich{1} and an open faced one.".format(min(pb,jelly,slices/2),plural)
elif slices % 2 == 1 and jelly and pb >= 1:
    print "You can make {0} sandwich{1}.".format(min(pb,jelly,slices/2),plural)
else:
    print "No PB&J for you :("

#Fourth Goal
if pb and jelly and slices/2 >= 1 and slices % 2 == 0:
    if pb > 1 and jelly > 1 and slices/2 > 1:
        plural = "es"
    else:
        plural = ""
    print "You can make {0} sandwich{1}!".format(min(pb,jelly,slices/2),plural)
elif slices % 2 == 1 and jelly > slices/2 and pb > slices/2:
    print "You can make {0} sandwich{1} and an open faced one.".format(min(pb,jelly,slices/2),plural)
elif slices % 2 == 1 and jelly and pb >= 1:
    print "You can make {0} sandwich{1}.".format(min(pb,jelly,slices/2),plural)
else:
    if pb == 0:
        print "You need peanut butter."
    if jelly == 0:
        print "You need jelly."
    if slices == 0:
        print "You need bread."

#Fifth Goal
if pb and jelly and slices/2 >= 1 and slices % 2 == 0:
    if pb > 1 and jelly > 1 and slices >2:
        plural = "es"
    else:
        plural = ""
    print "You can make {0} sandwich{1}!".format(min(pb,jelly,slices/2),plural)
elif slices % 2 == 1 and jelly > slices/2 and pb > slices/2:
    print "You can make {0} sandwich{1} and an open faced one.".format(min(pb,jelly,slices/2),plural)
elif slices % 2 == 1 and jelly and pb >= 1:
    print "You can make {0} sandwich{1}.".format(min(pb,jelly,slices/2),plural)
elif jelly == 0:
    if pb > 1 and slices >2: #Why do I have to put this here? Why is "plural" not defined by the nested if statement on line 56?
        plural = "es"
    else:
        plural = ""    
    print "You can make {0} peanut butter sandwich{1}, but what kind of person would do that? Gross.".format(min(pb,slices/2),plural)
else:
    if pb == 0:
        print "You need peanut butter."
    if slices == 0:
        print "You need bread."
