import struct

hexnum = 0xffffabcd
little_endian = struct.pack("<I", hexnum)

print(little_endian)

little_endian = hexnum.to_bytes(4, 'little')

print(little_endian)