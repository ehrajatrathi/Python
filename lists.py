a = '{\"Åland Island\"}' 
\
print(str("A"+a[3:14]))



R1 = ["Greta", 102, "USA"]
R2 = ["NYC", "CA", "LA"]
print("The citites in usa:",len(R2))
print(type(R1))
print(R1[0:3])


ice_creams = ["Vanilla", "Chocolate", "Blackcurrent", "Dryfriuts"]
a = 1
b = 3
if (a < 1):
     ice_creams.append("Nuts")
     print(ice_creams)
else:
    ice_creams.append("Red Chocolate")
    print(ice_creams)

ice_creams.insert(1,"ButterScotch")
print(ice_creams)

ice_creams.insert(2, 'Blueberry')
print(ice_creams)

ice_creams.insert(3, 'mixfruits')
print(ice_creams)


shakes = ["strawberry", "apple", "pineapple", "orange"]
print(shakes)

items = shakes + ice_creams
print(items)


print(len(items))

golo = "bread" in items
print(golo)

people = "orange" in items
print(people)