hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

test2 = [
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08"
]


def literal_packet(pack):
    i = 0
    packet = 0
    while True:
        label = pack[i]
        i += 1
        packet = packet << 4 | (int(pack[i:i + 4], 2))
        i += 4
        if label == "0":
            break
    return i, packet


versions = []
version_sum = 0


def find_packets(message):
    global version_sum
    packet = 0
    idx = 0
    v = int(message[idx:3], 2)
    version_sum += v
    idx += 3
    t = int(message[idx:idx + 3], 2)
    idx += 3
    if t == 4:  # literal packet
        i, packet = literal_packet(message[idx:])
        idx += i
    else:
        l = message[idx]
        idx += 1
        packs = []
        if l == "0":
            sub_length = int(message[idx:idx + 15], 2)
            idx += 15
            k = idx + sub_length
            while idx < k - 6:
                j, p = find_packets(message[idx:idx + k])
                idx += j
                packs.append(p)

        else:
            sub_length = int(message[idx:idx + 11], 2)
            idx += 11
            for p in range(sub_length):
                j, p = find_packets(message[idx:])
                idx += j
                packs.append(p)

        if t == 0:
            packet = sum(packs)

        elif t == 1:
            packet = 1
            for p in packs:
                packet *= p

        elif t == 2:
            packet = min(packs)

        elif t == 3:
            packet = max(packs)
        elif t == 5:
            packet = int(packs[0] > packs[1])
        elif t == 6:
            packet = int(packs[0] < packs[1])
        elif t == 7:
            packet = int(packs[0] == packs[1])

    return idx, packet


def solve(file, test=False):
    hex = [x for x in open(file).readline().strip()]
    in_binary = "".join([hex_to_bin[l] for l in hex])
    if test:
        for t in test2:
            in_binary = "".join([hex_to_bin[l] for l in t])
            v, packets = find_packets(in_binary)
            print("p1", sum(versions))
            print("p2", t, packets)
    else:
        v, packets = find_packets(in_binary)
        print("p1", version_sum)
        print("p2", packets)


if __name__ == '__main__':
    # solve("ex.txt")
    # solve("ex2.txt")
    # solve("ex3.txt")
    # solve("ex4.txt") #8A004A801A8002F478  16
    # solve("ex5.txt") #620080001611562C8802118E34  12
    solve("in.txt")
