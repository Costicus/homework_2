stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Quenn St")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(3, "Polmont")

#4. Print out the index position of "Linlithgow"
index = stops.index("Linlithgow")
print(stops)

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index
stops.pop(1)

#7. Print the number of stops there are in the list
number_of_items = len(stops)
print(number_of_items)

#8. Sort the list alphabetically
sorted_stops = sorted(stops,key=str.lower)
stops.sort()

#9. Reverse the positions of the stops in the list
stops.reverse()

#10 Print out all the stops using a for loop
for station in stops:
    print(station)


stops[0]

      