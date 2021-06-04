from struct import pack, unpack

pakHeader = pack("II",6476,0)
print(pakHeader)
pakSize, _ = unpack('II', pakHeader)
print(pakSize)