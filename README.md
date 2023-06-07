# hirst_painting
This Python program uses turtle graphics to create a Hirst painting, featuring a series of colorful dots arranged in a zigzag pattern. Each dot is randomly selected from a predefined palette of colors.

This Python program generates a Hirst painting using the turtle graphics library. The program utilizes a predefined list of colors to create a visually appealing artwork. The turtle starts at the bottom left corner of the canvas and moves in a zigzag pattern, drawing a series of dots in each line. After completing a line, it turns around and repeats the process in the opposite direction. This continues for a specified number of iterations, resulting in a unique Hirst painting.

The program imports the necessary modules, including random for color selection and turtle for drawing. It sets up the turtle's initial configuration, such as speed and appearance. The RGB color values are stored in the color_list, representing the palette used for the painting.

The draw_dots_in_line() function is responsible for drawing a line of dots using random colors from the color_list. The turtle moves forward by a fixed distance and selects a color at random for each dot.

The make_turn() function adjusts the turtle's heading and moves it forward to prepare for the next line.

The draw_art() function controls the overall drawing process. It iterates a specified number of times, calling draw_dots_in_line() and make_turn() alternately to create the desired pattern.

Finally, the program sets up the turtle screen and waits for a click to exit.

By running this program, you can generate your own Hirst painting with colorful dots arranged in an aesthetically pleasing pattern.

Hirst painting screenshot : https://drive.google.com/file/d/16s6OYmWbXbELvk8SoLa3Q0ksbjAWGJ-h/view?usp=drive_link
