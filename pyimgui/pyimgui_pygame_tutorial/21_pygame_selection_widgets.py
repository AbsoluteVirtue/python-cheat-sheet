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
    pygame.display.set_caption("Pyimgui: 21_selection_widgets")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    selected = [False, False]

    current = 0
    item_list = ["first", "second", "third", "fourth", ""] # empty item at the end to prevent a bug

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

        imgui.set_next_window_size(300, 300, condition = imgui.ONCE)
        imgui.begin("Combo box")

        # Combobox
        clicked, current = imgui.combo("Combobox", current, item_list)

        imgui.text("Following item is selected: {}".format(item_list[current]))

        imgui.separator()

        # Listbox
        clicked, current = imgui.listbox("Listbox", current, item_list, 3)

        # Listbox header
        imgui.listbox_header("List", 200, 100)

        imgui.selectable("Selected", True)
        imgui.selectable("Not selected", False)

        imgui.listbox_footer()

        imgui.separator()

        opened, selected[0] = imgui.selectable(
            "I am selectable", selected[0]
        )

        opened, selected[1] = imgui.selectable(
            "I am selectable too", selected[1]
        )

        imgui.text("3. I am not selectable")




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