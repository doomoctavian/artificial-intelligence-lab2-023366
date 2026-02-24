# Implement automated vacuum cleaner reflex agent(023-352)

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

current_location = "A"

def display_rooms():
    print("Room Status:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("---------352---------")

while True:
    display_rooms()
    
    if rooms[current_location] == "Dirty":
        print("Cleaning Room", current_location)
        rooms[current_location] = "Clean"
    else:
        
        if current_location == "A":
            current_location = "B"
        else:
            current_location = "A"
        print("Moving to Room", current_location)
    
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("Both rooms are clean. Stopping.")
        display_rooms()
        break
