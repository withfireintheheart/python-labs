def encode_morze(x):
    morse_code = {
        "A": "^_^^^",
        "B": "^^^_^_^_^",
        "C": "^^^_^_^^^_^",
        "D": "^^^_^_^",
        "E": "^",
        "F": "^_^_^^^_^",
        "G": "^^^_^^^_^",
        "H": "^_^_^_^",
        "I": "^_^",
        "J": "^_^^^_^^^_^^^",
        "K": "^^^_^_^^^",
        "L": "^_^^^_^_^",
        "M": "^^^_^^^",
        "N": "^^^_^",
        "O": "^^^_^^^_^^^",
        "P": "^_^^^_^^^_^",
        "Q": "^^^_^^^_^_^^^",
        "R": "^_^^^_^",
        "S": "^_^_^",
        "T": "^^^",
        "U": "^_^_^^^",
        "V": "^_^_^_^^^",
        "W": "^_^^^_^^^",
        "X": "^^^_^_^_^^^",
        "Y": "^^^_^_^^^_^^^",
        "Z": "^^^_^^^_^_^"
    }

    x = x.upper().strip()
    l = []
    s = ''
    for c in x:
        if c == " ":
            l.append("_")
        elif c in morse_code:
            l.append(morse_code.get(c))
    s = "___".join(l)
    return (s)


if __name__ == '__main__':
    print(encode_morze('Morze code'))
    print(encode_morze('Prometheus'))
    print(encode_morze('SOS'))
    print(encode_morze('1'))