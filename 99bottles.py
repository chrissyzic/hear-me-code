for bottle in range(100, 1, -1):
    if bottle > 2:
        plural = "s"
    else:
        plural = ""
    print "{0} bottles of beer on the wall. {0} bottles of beer.\nTake one down, pass it around. {1} bottle{2} of beer on the wall.".format(bottle,bottle-1,plural)

print "Last bottle of beer on the wall. The last bottle of beer.\nTake it down, pass it around. No more bottles of beer on the wall."
