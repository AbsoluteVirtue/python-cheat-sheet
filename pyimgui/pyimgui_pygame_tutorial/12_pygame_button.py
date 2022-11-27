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
    pygame.display.set_caption("Pyimgui: 12_button")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    button_clicked = ""

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

        # Create buttons
        # Syntax:
        #   imgui.button(string label, float width, float height)
        imgui.button("Button 1")
        imgui.button("Button 2", width = 100, height = 50)
        if imgui.button("Button with function", 200.0, 100.0):
            button_clicked = "The button was clicked."

        imgui.text(button_clicked)

        # Color Button
        # To give a button a color, the color must be "pushed" on the stack,
        # the the button must be created, and the the color must be "popped"
        # from the stack.

        # 1) Push color (r, g, b, a) and desired element (button) on the stack
        imgui.push_style_color(imgui.COLOR_BUTTON, 0.0, 0.0, 1.0, 1.0)
        # 2) Create the button (optional with desired size)
        imgui.button("Colored button", 50, 50)
        # 3) Pop the color from stack
        imgui.pop_style_color()

        # Small buttons
        imgui.small_button("Small button 1")
        imgui.small_button("Small button 2")

        # Invisible button
        imgui.invisible_button("Invisible button", 200, 200)
        imgui.small_button("Small button below invisible button")

        imgui.text(button_clicked)

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
