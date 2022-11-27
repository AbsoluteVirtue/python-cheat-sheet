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
    pygame.display.set_caption("Pyimgui: 3_proup")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    # Custom variables used by elements in the UI
    # must be defined before the while-loop
    value = 10

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

        # Construction window 1
        imgui.set_next_window_size(500, 400, imgui.ONCE)
        imgui.begin("Window 1")

        # Create group
        imgui.begin_group()  # element has no parameters

        # Add elements to group
        imgui.text("First group")
        imgui.button("Button 1")
        imgui.button("Button 2")

        # Close group
        imgui.end_group()

        # The previous group and the next element/group are displayed on the same line
        imgui.same_line(spacing = 20.0)

        # Creating new group
        imgui.begin_group()

        imgui.text("Second group")
        imgui.bullet_text("Checkbox 1")
        imgui.bullet_text("Checkbox 2")

        imgui.end_group()

        # A dummy creates an empty space
        # Syntax: imgui.dummy(float x, float y)
        imgui.dummy(20, 50)

        imgui.same_line()

        imgui.text("Text besides the dummy")

        imgui.text("Text after the dummy")
        imgui.bullet_text("Bullet A")

        # The "indent" keyword indents the next element
        imgui.indent()
        imgui.bullet_text("Bullet B (first indented)")

        # The indent width can be specified with a value
        imgui.indent(100)
        imgui.bullet_text("Bullet C (second indented with large width)")

        # The "unindent" keyword unindents the next element in relation to the previous element
        imgui.unindent(100)
        imgui.bullet_text("Bullet D (second indent cleared)")

        imgui.unindent()
        imgui.bullet_text("Bullet E (first indent cleared)")

        # New line
        imgui.new_line()

        # Spacing (vertical space)
        imgui.spacing()

        # Element width
        # 1) custom
        # Specify the item width for a following element
        imgui.push_item_width(imgui.get_window_width() * 0.33)
        # the item which should get the width
        imgui.text("Custom width")
        changed, value = imgui.slider_float("float slider 1", value, 0.0, 20.0)
        # Handing over the width to the previous element
        imgui.pop_item_width()

        # 2) default
        imgui.text("Default width")
        changed, value = imgui.slider_float("float slider 2", value, 0.0, 20.0)

        # Closure for window 1
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
