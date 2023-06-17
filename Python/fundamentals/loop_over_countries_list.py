"""

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries)):
    print("Index:", integer)

    # Challenge 2: print the index here
    print("Country:", countries[integer])

    # Challenge 3: print the country here
 
# Looping over values only...
for i in range(0, len(countries)):
    print(i, "Country:", countries[i])
    # Challenge 4: print the country here

"""

countries2 = ["Canada", "Iceland", "Chile", "Egypt", "Greenland", "Belgium", "Germany"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries2)):
    print(f"Index: {integer}")

    # Challenge 2: print the index here
    print(f"Country: {integer}")

    # Challenge 3: print the country here
    print(f"Country: " + countries2[integer])
 
# Looping over values only...
for country in countries2:
    print(f"Country: {country}")

    # Challenge 4: print the country here
for country in countries2:
    print(f"{country}")


