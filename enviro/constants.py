#!/usr/bin/env python3


class Constants:

    x_offset = 2
    y_offset = 2
    font_size_small = 10
    font_size_large = 20

    # The position of the top bar
    top_pos = 25

    # Create a values dict to store the data
    variables = [
        "temperature",
        "pressure",
        "humidity",
        "light",
        "oxidised",
        "reduced",
        "nh3",
        "pm1",
        "pm25",
        "pm10",
    ]

    units = ["C", "hPa", "%", "Lux", "kO", "kO", "kO", "ug_m3", "ug_m3", "ug_m3"]

    # Define your own warning limits
    # The limits definition follows the order of the variables array
    # Example limits explanation for temperature:
    # [4,18,28,35] means
    # [-273.15 .. 4] -> Dangerously Low
    # (4 .. 18]      -> Low
    # (18 .. 28]     -> Normal
    # (28 .. 35]     -> High
    # (35 .. MAX]    -> Dangerously High
    # DISCLAIMER: The limits provided here are just examples and come
    # with NO WARRANTY. The authors of this example code claim
    # NO RESPONSIBILITY if reliance on the following values or this
    # code in general leads to ANY DAMAGES or DEATH.
    limits = [
        [4, 18, 28, 35],
        [250, 650, 1013.25, 1015],
        [20, 30, 60, 70],
        [-1, -1, 30000, 100000],
        [-1, -1, 40, 50],
        [-1, -1, 450, 550],
        [-1, -1, 200, 300],
        [-1, -1, 50, 100],
        [-1, -1, 50, 100],
        [-1, -1, 50, 100],
    ]

    # RGB palette for values on the combined screen
    palette = [
        (0, 0, 255),  # Dangerously Low
        (0, 255, 255),  # Low
        (0, 255, 0),  # Normal
        (255, 255, 0),  # High
        (255, 0, 0),
    ]  # Dangerously High
