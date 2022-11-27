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
    pygame.display.set_caption("Pyimgui: 17_columns")

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

        imgui.begin("Example: Columns")

        # Creates a table
        # Syntax:
        #   imgui.columns(int columns_count, string table_identifier, bool border)
        # border is by default "True"
        imgui.columns(4, "fileList", border = True)

        # Creates a simple line on top of the table
        imgui.separator()

        # Procedure to file the table:
        # The table starts in the first column and first row. Now you can
        # build in unlimited elements in the first field ... for e.g. a text ...
        imgui.text("ID")
        # ... after that, the program jumps to the next field (second column,
        # first row) with the statement "imgui.next_column()".
        imgui.next_column()
        # After that you can build in any element in this field.
        imgui.text("File")
        # Jump to the next field (nr. 3)... and so on ...
        imgui.next_column()
        imgui.text("Size")
        # Field nr. 4
        imgui.next_column()
        imgui.text("Last Modified")

        # After the last column, with the "next_column" statement the program
        # jumps back to the first column but the second row.
        imgui.next_column()
        imgui.separator()
        imgui.text("1")
        imgui.next_column()
        imgui.text("FileA.txt")
        imgui.next_column()
        imgui.text("57 Kb")
        imgui.next_column()
        imgui.text("12th Feb, 2016 12:19:01")
        imgui.next_column()

        # Jump back to the first column and the third row.
        imgui.text("2")
        imgui.next_column()
        imgui.text("ImageQ.png")
        imgui.next_column()
        imgui.text("349 Kb")
        imgui.next_column()
        imgui.text("1st Mar, 2016 06:38:22")
        imgui.next_column()

        # You can create as many rows as you want, since only the number
        # of columns was defined at the beginning.

        # With following statement, you can specify the offset of each column
        # Syntax:
        #   imgui.set_column_offset(int column_nr, float offset)
        imgui.set_column_offset(1, 100)

        # With the following statement the table is closed.
        # Every element following this statement, isn't included
        # in the table any more.
        imgui.columns(1)

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
