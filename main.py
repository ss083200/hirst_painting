import random
import turtle as t

# import colorgram
# colorgram.extract returns Color objects(rgb, hsl, proportion). refer: https://pypi.org/project/colorgram.py/
# colors = colorgram.extract('spot_painting.jpg', 100)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# From the above commented code we extracted and printed the various colors and then stored them into colo_list which
# prevents us from executing the same piece of code again and again.
color_list = [
                (236, 225, 83), (202, 5, 72), (198, 164, 10), (235, 51, 129), (206, 76, 11), (108, 179, 218),
                (30, 188, 108), (23, 106, 173), (13, 23, 64), (17, 28, 175), (213, 135, 176), (9, 185, 214),
                (205, 29, 142), (229, 168, 197), (125, 189, 162), (8, 49, 28), (37, 132, 73), (125, 219, 233),
                (67, 22, 8), (61, 11, 26), (111, 89, 211), (142, 216, 201), (190, 15, 5), (238, 63, 31), (10, 97, 52),
                (167, 183, 232), (236, 171, 158), (8, 85, 102), (253, 5, 44), (25, 44, 244), (61, 95, 10), (250, 10, 8),
                (219, 162, 103), (234, 225, 6)
            ]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def draw_dots_in_line():
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


def make_turn(direction):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(direction)
    tim.forward(50)


def draw_art(num):
    for _ in range(num):
        draw_dots_in_line()
        make_turn(180)
        draw_dots_in_line()
        make_turn(0)


draw_art(5)
screen = t.Screen()
screen.exitonclick()

