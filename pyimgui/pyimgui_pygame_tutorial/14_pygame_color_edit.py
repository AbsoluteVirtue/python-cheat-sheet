# @Copyright: 2018 LuminousLizard
# @Project: Pyimgui-user-friendly
# @License: BSD-3

# -*- coding: utf-8 -*

# required packages
import sys # for close call

# render engine
import pygame
import OpenGL.GL as gl

# GUI library
from imgui.integrations.pygame import PygameRenderer
import imgui


# Main function
# It creates the instance and the program loop, and holds the
# frames and individual windows.
# It's called at the bottom of this file to start the application.
def main():
    # Initialize a pygame instance
    pygame.init()

    imgui.create_context()

    # Size of the main screen
    size = 1024, 768

    # Initialize the screen for display
    pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
    # Set screen title
    pygame.display.set_caption("Pyimgui: 14_color_edit")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()


    # Important: the variables storing the state of elements
    # (e.g. color_edits) must be inserted BEFORE the main loop
    color_1 = (1.0, 0.0, 0.5)
    color_2 = (0.0, 0.8, 0.3)
    color_3 = (1.0, 0.0, 0.5, 0.5)
    other_color = False


    # Main loop
    # This keeps the application running until the "exit" command is called
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            render_engine.process_event(event)

        # creates a new imgui frame for individual windows in the main screen
        imgui.new_frame()


        # ------------------------
        # GUI code

        # Create a window
        imgui.begin("Window 1")

        change_1, color_1 = imgui.color_edit3("Color 1", *color_1)

        change_2, color_2 = imgui.color_edit3("Color 2", *color_2)

        change_3, color_3 = imgui.color_edit4("Color with alpha value", *color_3, show_alpha = True)

        if change_1 or change_2 or change_3 == True:
            other_color = True

        imgui.text("Has one of the three colours been changed ? " + str(other_color))


        # Close window 1
        imgui.end()

        # ------------------------


        # note: cannot use screen.fill((1, 1, 1)) because pygame's screen
        #       does not support fill() on OpenGL sufraces
        gl.glClearColor(0.1, 0.1, 0.1, 1) # Background color of the main screen
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.render()
        render_engine.render(imgui.get_draw_data())

        # Update the full display surface to the screen
        pygame.display.flip()

# Application call for start
if __name__ == "__main__":
    main()
