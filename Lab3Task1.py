key_string = "aaaaabbbbbabbbaabbababbaaababaab"

def generate_dict():
    baconDict = {}

    for i in range(0, 26):
        tmp = key_string[i:i + 5]
        baconDict[tmp] = chr(97 + i)

    return baconDict


if __name__ == '__main__':
    msg = "Hot sUn BEATIng dOWN bURNINg mY FEet JuSt WalKIng arOUnD HOt suN mAkiNG me SWeat"

    msg = msg.replace(" ", "")

    msg = [msg[i:i + 5] for i in range(0, len(msg), 5)]

    msg = list(filter(lambda x: len(x) == 5, msg))

    print(msg)

    ciphered = []
    for w in msg:
        a = ""

        for c in w:
            if c.islower():
                a += "a"
            else:
                a += "b"

        ciphered.append(a)

    dict = generate_dict()

    result = "".join(map(lambda x: dict[x], ciphered))

    print(result)