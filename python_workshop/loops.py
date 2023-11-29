#!/Users/himat.varsani/.pyenv/shims/python

# While Loops - execute until condition has been met
#i = 1
#while i < 5:
 #   print(i)
  #  i = i + 1

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
#print(planets[2])

#planets[2] = "Terra"
#print(planets)

#print(planets[0:2])

#planets.append("Jupiter")
#print(planets)

#planets.insert(3, "Moon")
#print(planets)

#planets.remove("Moon")
#print(planets)

#print("Mars" in planets)

for p in planets:
    print(p)

#Dictionaries - key value pair - it's unique - like a dictionaries - no word is the same
# "" - Keys, after the : is the value
#left side from colon = key
#right side from colon = value
distance_from_sun = {
    #left in "" is they key
    #right after the : is the value
    #you can
    # 1: "Adam",
    # 2: "Dave",
    # 3: "Chris", - 1, 2, 3 is the the key, anything after colon is the value
    
    "Mercury": 0.4,
    "Venus": 0.7,
    "Earth": 1,
    "Mars": 1.5,
}
print(distance_from_sun)
print(distance_from_sun["Mercury"])
print(distance_from_sun["Earth"])

# p is the key - the item after the distance_from_sun is a value
for p in distance_from_sun:
    print(p + " ---> " + str(distance_from_sun[p]))
    
#or
    
for key, value in distance_from_sun.items():
    print(key + " ---> " + str(value))