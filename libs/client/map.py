def mapRenderer(map: list):
    for line in map:
        print(" ", end="")
        print("- " * len(line))

        print("|", end='')

        for tile in line:
            tileDisplay = ' '

            if tile == -1:
                tileDisplay = 'X'

            print(tileDisplay, end='|')

        print()

    print(" ", end="")
    print("- " * len(map[0]))