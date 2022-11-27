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
    pygame.display.set_caption("Pyimgui: 10_tooltip")

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

        # A tooltip is an info box for any desired element,
        # which is shown if the mouse cursor is hovering if the element.
        # The info box itself can contain many different elements.

        # Create a window
        imgui.begin("Window 1")

        # A button ...
        imgui.button("Hover over me !")
        # ... to which a simple tooltip only with text is attached
        if imgui.is_item_hovered():
            # The following function can only take text
            imgui.set_tooltip("Please ?")

        # For a complex tooltip with additional elements
        # e.g. a bullet_text
        imgui.button("Button with tooltip")
        if imgui.is_item_hovered():
            # Begin of the tooltip definition
            imgui.begin_tooltip()

            # Elements included in the tooltip e.g. text ...
            imgui.text("This tooltip has text ...")

            # ... bullet text ...
            imgui.bullet_text("... bullet text ...")

            # ... a separator ...
            imgui.separator()

            # ... and a table.
            imgui.columns(2, "Table")  # Start: Number of columns / table title
            imgui.text("Column 1")
            imgui.next_column()
            imgui.text("Column 2")
            imgui.next_column()
            imgui.text("... and a ...")
            imgui.next_column()
            imgui.text("... table.")
            imgui.columns(1)  # Closure of the table

            # Closure of the complex tooltip
            imgui.end_tooltip()

        # Closure of the window
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
