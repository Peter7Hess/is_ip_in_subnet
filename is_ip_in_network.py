def dot_decimal_to_binary(address):
    octets=[int(x) for x in address.split(".")]
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8)  + octets[3]

def cidr_mask_to_binary(mask):
    bits = 0
    for i in range(32-mask,32):
        bits |= (1 << i)
    return bits

def is_ip_in_subnet(address, network, mask):
    baddr = dot_decimal_to_binary(address)
    bnetw = dot_decimal_to_binary(network)
    bmask = cidr_mask_to_binary(mask)
    return (baddr & bmask) == bnetw

print(is_ip_in_subnet("10.10.10.1", "10.0.0.0", 8))
print(is_ip_in_subnet("10.10.10.1", "10.0.0.0", 16))
print(is_ip_in_subnet("10.10.10.128", "10.10.10.0", 23))
print(is_ip_in_subnet("10.10.10.128", "10.10.10.0", 24))
print(is_ip_in_subnet("10.10.10.128", "10.10.10.0", 25))
