import colorsys


def calculate_color(start, end, position):

    rdelta, gdelta, bdelta = (end[0] - start[0]) * position, (end[1] - start[1]) * position, (end[2] - start[2]) * position
    r, g, b = start[0] + rdelta, start[1] + gdelta, start[2] + bdelta
    return int(r), int(g), int(b)

if __name__ == '__main__':
    print(calculate_color((255,0,0), (0,255,0), 0.5))


