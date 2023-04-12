def mapRenderer(map: list):
    for line in map:
        print(" ", end="")
        print("- " * len(line))

        print("|", end='')

        for tile in line:
            tileDisplay = ' '

            if tile < 0:
                tileDisplay = str(tile)

            print(tileDisplay, end='|')

        print()

    print(" ", end="")
    print("- " * len(map[0]))