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
    pygame.display.set_caption("Pyimgui: 5_menu_bar")

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

        # ---------------
        # GUI code start
        # ---------------

        # Create window
        # A window must be explicitly allowed to have a menu bar.
        # This is done by using flags. There are 2 possible ways to do this.

        # 1)
        imgui.begin("Window 1", flags = imgui.WINDOW_MENU_BAR)

        imgui.end()

        # 2)
        imgui.begin("Window 2", flags = 1024)  # 1024 = imgui.WINDOW_MENU_BAR

        # Create a menu bar which is anchored in a window.
        # The internal structure is the same as for the main menu bar.
        # The function has no parameters.
        if imgui.begin_menu_bar():
            # Create the first dropdown menu
            if imgui.begin_menu(label = "File"):
                imgui.menu_item(label = "Close")
                # Closure for the first dropdown menu
                imgui.end_menu()

            # Create a second dropdown menu
            if imgui.begin_menu(label = "About"):
                imgui.menu_item(label = "Info")
                # Closure for the second dropdown menu
                imgui.end_menu()

            # Closure for the menu bar
            imgui.end_menu_bar()

        imgui.end()

        # ---------------
        # GUI code end
        # ---------------

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
