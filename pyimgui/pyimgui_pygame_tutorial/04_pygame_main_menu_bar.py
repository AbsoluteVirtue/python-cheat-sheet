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
    pygame.display.set_caption("Pyimgui: 4_main_menu_bar")

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

        # Create main menu bar
        # The "if" statement is required for user actions
        if imgui.begin_main_menu_bar():

            # create first dropdown menu
            # Syntax: imgui.begin_menu(string label, bool enabled)
            if imgui.begin_menu(label = "File",
                                enabled = True):

                # Create menu items included in the previous defined dropdown menu
                # Syntax: imgui.menu_item(string name,
                #                         string shortcut,
                #                         bool selected,
                #                         bool enabled)
                imgui.menu_item(label = "New",
                                shortcut = "Ctrl+N",
                                selected = True,
                                enabled = False)

                imgui.menu_item(label = "Open",
                                shortcut = "Ctrl+O",
                                selected = False,
                                enabled = True)

                # Create menu item with submenu
                if imgui.begin_menu(label= "Save as",
                                    enabled = True):

                    imgui.menu_item(label = "*.txt",
                                    shortcut = None,
                                    selected = False,
                                    enabled = True)

                    # Closure for the submenu
                    imgui.end_menu()

                # Closure for the first dropdown menu
                imgui.end_menu()

        # Create second dropdown menu with new "if" statement
        # As the first dropdown menu, the second is also included in the
        # "imgui.begin_main_menu_bar" block.
        if imgui.begin_menu(label = "About", enabled = True):

            imgui.menu_item(label = "Info", shortcut = "Ctrl+I", selected = True, enabled = True)

            # Closure for the second dropdown menu
            imgui.end_menu()

        # Closure for the main menu bar
        imgui.end_main_menu_bar()

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
