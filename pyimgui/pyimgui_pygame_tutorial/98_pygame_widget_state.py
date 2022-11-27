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
    size = 800, 600

    # Initialize the screen for display
    pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
    # Set screen title
    pygame.display.set_caption("Pyimgui: Widgets states")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    # IMPORTANT: the variables storing the state of elements
    # (e.g. checkbox) must be inserted BEFORE the main loop
    checkbox_clicked = None
    checkbox_activ = False

    state_radioButton = [True, False, False]

    color = (1.0, 0.0, 0.5)

    # MAIN LOOP
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
        # ------------------------
        imgui.set_next_window_size(
            width = 500,
            height = 200,
            condition = imgui.ONCE
        )
        # Create a window within the frame
        imgui.begin("Example: Widget states")

        # A few widgets have a state, that represents the current value.
        # E.g. checkboxes, radio buttons with bool values,
        # Sliders, drags and color edits with int and float values
        # These states can be assigned to variables parallel to the
        # definition of the widget.

        # IMPORTANT: The variables who take the state must be defined BEFORE
        # the main loop (see above line 48)

        # A checkbox has 2 return values
        # 1) "clicked" is a bool value and is "True" if the checkbox is clicked
        #   (the value is only for short time "True")
        # 2) "checkbox_enabled" is a bool value and is "True" if the
        #   checkbox is activated
        checkbox_clicked, checkbox_activ = imgui.checkbox(
            "Checkbox 1", # Label
            checkbox_activ # Input current state
        )
        # If the checkbox was clicked and activated, the value "True"
        # is assigned to the variable "checkbox_activ". In the next frame
        # of the main loop, the checkbox is reading this new value from the
        # variable and remains active.
        # The value can certainly be used by other elements or functions.

        imgui.text("If you click the checkbox, the state is changing.\n"
            "Also for a very short time the variable 'checkbox_clicked' is 'True'")

        imgui.text("State of the checkbox: {}".format(checkbox_activ))
        imgui.text("Checkbox clicked: {}".format(checkbox_clicked))

        imgui.separator()

        # Radio buttons have also a state, but these have only the
        # "clicked" return value (as with the checkbox).
        # The characteristic is that from a group only one radio button should
        # be active. To accomplish this, you must create an if-statement and
        # modify the states.
        if imgui.radio_button("Radio button 1", state_radioButton[0]):
            # Following statements handle the states of the radio buttons.
            # Only one radio button can always be active.
            state_radioButton[0] = True
            state_radioButton[1] = False
            state_radioButton[2] = False

        imgui.same_line()

        if imgui.radio_button("Radio button 2", state_radioButton[1]):
            state_radioButton[0] = False
            state_radioButton[1] = True
            state_radioButton[2] = False

        imgui.same_line()

        if imgui.radio_button("Radio button 3", state_radioButton[2]):
            state_radioButton[0] = False
            state_radioButton[1] = False
            state_radioButton[2] = True

        # Color edits (just like sliders and drags) returns int and float
        # values or tuples.
        # "change_color" is a bool value
        # "color" is a tuple with the rgb values
        change_color, color = imgui.color_edit3("Color 1", *color)

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
