'''
#
##
###
####
#####

print above pattern using while loop
'''

i = 0
#while loop
while i < 5:
    j = 0
    print("#",end="")
    while j < i:
        print("#",end="")
        j+=1
    i+=1
    print()
