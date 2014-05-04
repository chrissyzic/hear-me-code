pb = 8
jelly = 7
slices = 13
sand_number = 1


#First Goal
while pb >= 1 and jelly >= 1 and slices >= 2:
    print "Making Sandwich #{0}".format(sand_number)
    pb = pb - 1
    jelly = jelly - 1
    slices = slices - 2
    sand_number = sand_number +1

if pb == 0: #Define first ingredient to run out.
    ingredient = "peanut butter"
elif jelly == 0:
    ingredient = "jelly"
else:
    ingredient = "bread"

if sand_number > 2: #Just making the sentence sound more human.
    plural = "es"
else:
    plural = ""

print "Only had enough {0} for {1} sandwich{2}.".format(ingredient,sand_number-1,plural)


#Second Goal
while pb >=1 and jelly >=1 and slices >=2:
    print "Making Sandwich #{0}".format(sand_number)
    slices = slices - 2
    pb = pb - 1
    jelly = jelly - 1
    sand_number = sand_number +1      
    if pb > 0 and jelly > 0 and slices/2 > 0:
        if pb > 1 and jelly > 1 and slices/2 > 1:
            plural = "es"
        else:
            plural = ""
        print "I have enough bread for {0} more sandwich{3}, enough peanut butter for {1} more, and enough jelly for {2} more.".format(slices/2,pb,jelly,plural)
    else:
        if jelly == 0:
            print "All done. I ran out of jelly."
        elif slices/2 == 0:
            print "All done, I ran out of bread."
        elif pb == 0:
            print "All done. I ran out of peanut butter."
        else:
            print"You're not done!"
