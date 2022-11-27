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
    # (e.g. radio_button) must be inserted BEFORE the main loop
    radio_button_1 = True
    radio_button_2 = [True, False]

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

        imgui.begin("Example: radio buttons")

        # A single radio button who changes his state by a click
        if imgui.radio_button("Radio button 1", radio_button_1):
            radio_button_1 = not radio_button_1

        imgui.separator()

        # Two radio buttons which are linked to each other,
        # only one button can be activ
        # TODO: easier linking
        if imgui.radio_button("Radio button 2", radio_button_2[0]):
            radio_button_2[0] = True
            radio_button_2[1] = False

        if imgui.radio_button("Radio button 3", radio_button_2[1]):
            radio_button_2[0] = False
            radio_button_2[1] = True

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
