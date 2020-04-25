# let's look at an examples of for loop
#   - using a list

# define an interfaces list - items: interface names
interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2", "GigabitEthernet0/3", "GigabitEthernet1/1", "GigabitEthernet1/2"]

# loop through items in the list
for item in interfaces:
    if item.startswith("GigabitEthernet1/"):
        print(item, ": Uplink port")
    else:
        print(item, ":Host port")
