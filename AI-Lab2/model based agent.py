# model based agent(023-352)

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

current_location = "A"
# agent's memory
model = {
    "A": None,
    "B": None
}

def display_rooms():
    print("Room Status:", rooms)
    print("Agent Model :", model)
    print("Agent at    :", current_location)
    print("------------352-----------------")

while True:
    display_rooms()

    model[current_location] = rooms[current_location]

    if rooms[current_location] == "Dirty":
        print("Cleaning Room", current_location)
        rooms[current_location] = "Clean"
        model[current_location] = "Clean"

    else:
        if model["A"] == "Dirty":
            current_location = "A"
            print("Moving to Room A")
        elif model["B"] == "Dirty":
            current_location = "B"
            print("Moving to Room B")
        else:
            print("All rooms are clean. Stopping.")
            break

#ARGUMENTS (WHY is it better than Reflex based?)

#A model-based agent is better because it can remember things.
#It knows which room is clean and which one is dirty.
#So, it does not waste time moving again and again.
#Because of this, the agent works more efficiently and gives better performance, especially in complex situations.