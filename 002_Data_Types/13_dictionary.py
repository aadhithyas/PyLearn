# dictionaries or hash
# key:value pairs
# vlaue - can be any data type [integer, float, string, list or another dictionary]
# enclosed within curly braces

# initialize a dictionary
interface_1 = {}
# another way: interface_1 = dict()

print(type(interface_1))


# load values to interface_1 dictionary
interface_1['name'] = "GigabitEthernet0/1"
interface_1['mode'] = "access"
interface_1['vlan'] = 10
interface_1['portfast_enabled'] = True
print(interface_1)

# load values to interface_2 dictionary
interface_2 = {'name': 'GigabitEthernet0/2', 'mode': 'trunk', 'vlan': [10, 20, 30], 'portfast_enabled': False}
print(interface_2)

# Access the values from dictionary - use key name to access its value
print("Interface", interface_1['name'], "operates in", interface_1['mode'], "mode.")
print("Interface", interface_2['name'], "operates in", interface_2['mode'], "mode.")