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
    pygame.display.set_caption("Pyimgui: 11_text")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

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

        # Create a bullet/point
        imgui.bullet()
        # The first following text after the bullet is displayed after the bullet
        imgui.text("Text after a bullet.")
        # Another text element is displayed in a new line, without a bullet
        imgui.text("A following text element is displayed in a new line.")

        # The short form (bullet + text) is:
        # Syntax: imgui.bullet_text("Text")
        imgui.bullet_text("Bullet text 1")
        imgui.bullet_text("Bullet text 2")

        # Bullets can also be created via a loop.
        # This creates a row of 10 bullets.
        for i in range(10):
            imgui.bullet()

        imgui.separator()

        # Label
        imgui.label_text("my label", "my text")

        imgui.spacing()

        # Unformatted text
        # Big text area, the size is defined by it's container
        imgui.text_unformatted("Really ... long .. text")

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
