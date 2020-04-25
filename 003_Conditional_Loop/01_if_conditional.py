# let's look at an example for 'if' conditional

# single = is used for assigning value to a variable
interface = {"name": "GigabitEthernet0/1", "vlanId": 10}

# add "mode" to interface_1 dictionary
# change this value to check the variation of code output
#   - access
#   - trunk
#   - any random string
#   - comment out the mode
interface['mode'] = 'access'

# check if interface dict has a key named - mod
# check if the mode's value is "access"
#   if it is access mode, enable STP portfast
# check if the mode's value is "trunk"
#   if it is trunk mode, disable STP portfast
# if the mode is neither access nor trunk, report error

if 'mode' in interface:
    if interface['mode'] == "access":
        interface['portfast'] = 'enabled'
    elif interface['mode'] == "trunk":
        interface['portfast'] = 'disabled'
    else:
        print("\nError: Unknown port mode. Exiting program...")
        exit()
else:
    print("\nInterface mode is not defined in the dictionary", interface)
    exit()

# print the modified interface dictionary
print("\nInterface dictionary:", interface)


# following operators can be used as conditions in 'if' statement
"""
Relational Operators
--------------------
    ==      equals to
    !=      not equal to
    >       greater than
    <       less than
    >=      greater than or equal to
    <=      less than or equal to
    in      Membership
    is      Identity
"""