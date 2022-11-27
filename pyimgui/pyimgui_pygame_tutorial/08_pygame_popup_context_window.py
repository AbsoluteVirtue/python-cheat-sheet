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
    pygame.display.set_caption("Pyimgui: 8_popup_context_window")

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

        # Create a window
        imgui.begin("Window 1")

        # A "popup context window" is the same as the "popup context item",
        # but can only be attached on windows and is activated via a
        # specific mouse button:
        if imgui.begin_popup_context_window(label = "Window 1",  # for which window the popup should be available
                                            also_over_items = True,  # default: True
                                            # 0 = left mouse button
                                            # 1 = right mouse button
                                            # 2 = middle mouse button
                                            mouse_button = 1):
            # Items included in the popup
            imgui.selectable("Close")
            # Closure of the popup
            imgui.end_popup()

        imgui.text("Click with the right mouse button on any point in the window")

        # Closure of window 1
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
