pb = 6
jelly = 6
slices = 11

#First Goal
if pb >= 1 and jelly >= 1 and slices >=2:
    print "You can make a sandwich!"
else:
    print "No PB&J for you :("

#Second Goal
if pb == 0 or jelly == 0 or slices == 0:  #  if pb or jelly or slices == 0:
    print "No PB&J for you :("
elif jelly <= pb and jelly <= slices/2:
    print "You can make {0} sandwiches!".format(jelly)
elif pb <= jelly and pb <= slices/2:
    print "You can make {0} sandwiches!".format(pb)
elif slices/2 <= pb and slices/2 <= jelly:
    print "You can make {0} sandwiches!".format(slices/2)
else:
    print "No PB&J for you :("
    
#Third Goal
#If you have an odd number of bread slices, you can only make an open faced sandwich if you have enough pb & j for the extra slice of bread jelly = (slices/2)+1
if pb == 0 or jelly == 0 or slices == 0:
    print "No PB&J for you :("
elif jelly <= pb and jelly <= slices/2 and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(jelly)
elif jelly <= pb and jelly <= slices/2 and slices % 2 == 1:
    print "You can make {0} sandwiches!".format(jelly)
elif pb <= jelly and pb <= slices/2 and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(pb)
elif pb <= jelly and pb <= slices/2 and slices % 2 == 1:
    print "You can make {0} sandwiches!".format(pb)
elif slices/2 <= pb and slices/2 <= jelly and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(slices/2)
elif slices/2 <= pb and slices/2 <= jelly and slices % 2 == 1:
    print "You can make {0} full sandwiches and an open faced one!".format(slices/2)
else:
    print "No PB&J for you :("

    """
Another way to approach Third Goal
if pb or jelly or slices == 0:
    print "No PB&J for you :("
elif jelly or pb or slices/2 >= 1:
    print "You can make {0} sandwiches!".formt(min(jelly,pb,slices/2))"""

#Fourth Goal
if pb == 0:
    print "You need some peanut butter."
elif jelly == 0:
    print "You need some jelly."
elif slices == 0:
    print "You need some bread!"
elif jelly <= pb and jelly <= slices/2 and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(jelly)
elif jelly <= pb and jelly <= slices/2 and slices % 2 == 1:
    print "You can make {0} sandwiches!".format(jelly)
elif pb <= jelly and pb <= slices/2 and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(pb)
elif pb <= jelly and pb <= slices/2 and slices % 2 == 1:
    print "You can make {0} sandwiches!".format(pb)
elif slices/2 <= pb and slices/2 <= jelly and slices % 2 == 0:
    print "You can make {0} sandwiches!".format(slices/2)
elif slices/2 <= pb and slices/2 <= jelly and slices % 2 == 1:
    print "You can make {0} full sandwiches and an open faced one!".format(slices/2)
else:
    print "No PB&J for you :("
