#program to obtain the first characters of each string in a list of strings

def firstCharacters(stringlist):
    i = 0
    #a list is created to contain the result
    starting_letters = []
    for name in stringlist:
        if i <= len(stringlist):
            #for the string at every index, the first character is obtained
            # and added to the results list.
            starting_letters.append(stringlist[i][0])
            i = i + 1
    return starting_letters

#a little demonstration using a sample list is shown
foods = ['Corn chaff', 'Egusi Soup', 'Eru']
r = firstCharacters(foods)
print(r)


#alternatively, list comprehension can be used as such
stringlist = ['Kumba', 'Buea', 'Bamenda']
firsts = [stringlist[i][0] for i in range(len(stringlist))]
#stringlist represents the list of strings provided. it is an arbitrary name.
print(firsts)


#using numpy will greatly increase the efficiency of the code
import numpy as np
stringlist_np = np.array(stringlist)
firstThings = {}
for i,name in enumerate(stringlist):
    firstThings[name] = stringlist_np[i][0]
result = list(firstThings.values())
print(result)

stringlist = input("enter a list of lists:  ")