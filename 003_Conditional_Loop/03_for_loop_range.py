# let's look at an examples of for loop
#   - using range()

# create a list of even numbered VLAN IDs from 1 - 10
# create an empty list
vlan_id_list = list()
last_vlan_id = 10

# range of 1 - 100 is considered with step value of 2
for item in range(0, 100, 2):
    print("Value of item:", item)
    if item == 0:
        print("\tZero is not a valid VLAN ID. Skipping this iteration..")
        continue
    elif item > last_vlan_id:
        print("\tVLAN ID is greater than", last_vlan_id, ". Exiting the for loop...")
        break
    else:
        print("\tappending this to the list...")
        vlan_id_list.append(item)
    print("\tVLAN ID List:", vlan_id_list)

# vlan_id list created using for loop
print("\nFinal VLAN ID List:", vlan_id_list)
