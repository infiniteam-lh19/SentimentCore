import colorsys
import math

def red_white_green(t):
    angry_color = (255, 0, 0)
    neutral_color = (255, 255, 0)
    happy_color = (0, 255, 0)

    if t < 0.5:
        return calculate_color(angry_color, neutral_color, 2 * t)
    else:
        return calculate_color(neutral_color, happy_color, 2 * (t - 0.5))

def calculate_color(start, end, position):

    start_hsv = colorsys.rgb_to_hsv(start[0] / 255.0, start[1] / 255.0, start[2] / 255.0)
    end_hsv = colorsys.rgb_to_hsv(end[0] / 255.0, end[1] / 255.0, end[2] / 255.0)

    h = angle_lerp(start_hsv[0], end_hsv[0], 1, position)
    s = lerp(start_hsv[1], end_hsv[1], position)
    v = lerp(start_hsv[2], end_hsv[2], position)

    rgb = colorsys.hsv_to_rgb(h, s, v)

    return int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)

def normalize_angle(a, max):
    return a % max

def angle_distance(a0, a1, max):
    return ((a1 - a0) + max / 2) % max - max / 2

def lerp(a, b, t):
    return (b - a) * t + a

def angle_lerp(a0, a1, max, t):
    return normalize_angle(a0 + angle_distance(a0, a1, max) * t, max)


if __name__ == '__main__':
    #print(calculate_color((255,0,0), (0,255,0), 0.5))

    a0 = 50
    a1 = 350

    n = 10
    for i in range(n):
        print(normalize_angle(angle_lerp(a0, a1, 360, i / (n - 1)), 360))

