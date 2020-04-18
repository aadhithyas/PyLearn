"""
Challenge - 01                      

Given input:
    ip_address = "192.168.0.1"
    subnet_mask = "255.255.255.0"

Required output:                    
    ip_address_cidr = "192.168.0.1/24"

"""
# write down your code here and try to get the output required !!!
# Code Logic:
# convert Subnet mask to binary
# count the number of '1' from left - This is the prefix length

# ip address and mask variables
ip_address = "192.168.0.1"
subnet_mask = "255.255.255.0"

# create the octet list - split the string 'subnet_mask' into 4 octets : delimiter '.'
octets_list = subnet_mask.split('.')

# convert all the items in the list to integer - using built-in function map()
octets_list = list(map(int, octets_list))

# convert each item in the list to binary - Using list comprehension
binary_list = [bin(i)[2:].zfill(8) for i in octets_list]
print(binary_list)

# Join all the items in the list to form a string
binary_string = "".join(binary_list)
print(binary_string)

# prefix length - count the number of '1' in binary_string
prefix_length = binary_string.count('1')
print(prefix_length)

# IP address in CIDR format
print("IP address in CIDR format is {}/{}".format(ip_address, prefix_length))
