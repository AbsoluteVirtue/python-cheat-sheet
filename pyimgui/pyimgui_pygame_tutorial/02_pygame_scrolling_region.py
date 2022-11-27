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
    pygame.display.set_caption("Pyimgui: 2_scrolling_region")

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

        # Window 1
        imgui.begin("Window 1") # Construction

        # A child functioned as scroll region which contains further elements (e.g. text).
        # If more elements are included as the region is large, a scrollbar is displayed.
        imgui.begin_child("Scroll region",  # identifier
                          150,  # width
                          100,  # height
                          # 0.0 => uses remaining window size
                          # >0.0 => fixed size
                          # <0.0 => uses remaining window size - size
                          border = True)

        # following elements are included in the scroll region
        imgui.text("1")
        imgui.text("2")
        imgui.text("3")
        imgui.text("4")
        imgui.text("5")
        imgui.text("6")
        imgui.text("7")
        imgui.text("8")
        imgui.text("9")
        imgui.text("10")
        imgui.text("11")

        # Scroll region closure
        imgui.end_child()

        imgui.end() # Closure of window 1

        # Window 2
        imgui.begin("Example 2", # window title
                    closable = True, # additional parameter
                    flags = 4) # flags for special properties (4 = not movable)
            # Elements in window 2

        imgui.end() # Closure

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
