eight_bit_code = [0, 1]
hack = []

while eight_bit_code != hack:
    for bit_0 in range(2):
        hack.append(bit_0)
    for bit_1 in range(2):
        hack.append(bit_1)
        print(hack)
        hack.clear()

if eight_bit_code == hack:
    print(hack)
    print("Victory")
