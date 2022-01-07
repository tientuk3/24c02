import smbus2
from tabulate import tabulate

bus = smbus2.SMBus(1)

chip_address = 0x50
chip_size = 256 # bytes

def read_EEPROM(address, size):
    data = []
    for i in range(size):
        read = bus.read_byte(address)
        data.append(read)
    
    return data

result = read_EEPROM(chip_address, chip_size)

print('read %d bytes from EEPROM!!' % chip_size)

headers = list(range(0, 16))
headers = list(map(lambda x: hex(x), headers))
#result = list(map(lambda x: hex(x).upper()[2:], result))

headers.insert(0, "Offset")

data = []

for i in range(int(256/16)):
    index = i * 16
    row = [hex(index)]
    row.extend(result[index:index+16])
    data.append(row)

print(tabulate(data, headers, tablefmt="plain"))
print('write to file result')

f = open("result", "wb")
binarydata = bytearray(result)
f.write(binarydata)
f.close()
