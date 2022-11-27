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
    pygame.display.set_caption("Pyimgui: 18_window_manipulation")

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
        # Adding code to create individual windows and functions.

        # Manipulate the next created window
        # The next window is collapsed, and the condition implies
        # "only after the execution of the program"
        imgui.set_next_window_collapsed(True, condition = imgui.ONCE)
        # Create window
        imgui.begin("Example: Collapsed Window")
        imgui.text("This window is collapsed at the beginning.")
        imgui.end()

        # Determine the position of the next window in the main frame
        # Syntax:
        #   imgui.set_next_window_position(float x, float y, condition)
        # The default condition is "ALWAYS" and causes that the window
        # always on this position and not movable.
        # For a movable window use "ONCE" as condition.
        imgui.set_next_window_position(50, 50, condition = imgui.ONCE)
        imgui.begin("Example: Start position")
        imgui.end()

        imgui.set_next_window_position(200, 50, condition = imgui.ONCE)
        # The next window is alwys focused and in front of every other window,
        # with the exception of windows that are created subsequently and
        # have the same property.
        imgui.set_next_window_focus()
        imgui.begin("Example: Focused windows")
        imgui.end()

        imgui.set_next_window_position(350, 50, condition = imgui.ONCE)
        # Determine the size of the next window
        # Syntax:
        #   imgui.set_next_window_size(float width, float height, condition)
        # With the default condition "ALWAYS" the window cannot be resized
        imgui.set_next_window_size(200, 200, condition = imgui.ONCE)
        imgui.begin("Example: Focus window function")
        imgui.text("Predefined window size")
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
