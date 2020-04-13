# Let's create a list of VLANs configured on a swtich
# A list may contain different types of data (int, str, etc.,)
vlan_id_list = [10, 11, '12', '13', '14']

# print the first VLAN ID in the list
print("\nVLAN ID List is {}".format(vlan_id_list))
print("First VLAN ID in the list is {}".format(vlan_id_list[0]))
print("Last VLAN ID in the list is {}".format(vlan_id_list[-1]))

# list slicing
print("First three VLAN IDs in the list is {}".format(vlan_id_list[:3]))
print("VLAN IDs after third element in the list is {}".format(vlan_id_list[3:]))


# list of MTU of four interfaces in the device
mtu_list = [1500, 1400, 9100, 1300]
print("\nMTU List is {}".format(mtu_list))
print("Sorted MTU List (ascending) is {}".format(sorted(mtu_list)))
print("Lowest MTU among the four interfaces is {}".format(min(mtu_list)))
print("Highest MTU among the four interfaces is {}".format(max(mtu_list)))

# define an interface as a list [interface_name, mode, vlan]
access_port = ['GigabitEthernet0/1', 'ACCESS', 10]
print("\n{} is operating in {} mode and VLAN {} is allowed on this interface".format(access_port[0], access_port[1], access_port[2]))

# nested list - one of the element of your list can be an another list - "allowed vlans int the trun port"
trunk_port = ['GigabitEthernet1/1', 'TRUNK', [10,20,30]]
print("\n{} is operating in {} mode and VLANs {} is allowed on this interface".format(trunk_port[0], trunk_port[1], trunk_port[2]))