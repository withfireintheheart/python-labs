def create_verse(x: int, y: int):
    words: str = '-'.join(["la" for i in range(x)])
    verse = ' '.join(([words] * y))

    return verse

if __name__ == '__main__':
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    verse = create_verse(x, y)

    if z == 1:
        end_sign = "!"
    else:
        end_sign = "."

    if y > 0:
        white_space = ' '
    else:
        white_space = ''

    result = "Everybody sing a song:" + white_space + verse + end_sign
    print(result)