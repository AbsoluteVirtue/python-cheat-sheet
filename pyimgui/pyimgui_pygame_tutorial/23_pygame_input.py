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
    pygame.display.set_caption("Pyimgui: 23_input")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    visible_header = None

    expanded_floatInput = False
    float_val_1 = 3.14159
    float_val_2 = 3.14159
    float2_val = 3.14159, 4.2784
    float3_val = 3.14159, 4.2784, 7.7777
    float4_val = 3.14159, 4.2784, 7.7777, 1.23456

    expanded_intInput = False
    int_val_1 = 4
    int_val_2 = 4
    int2_val = 4, 77
    int3_val = 4, 77, 42
    int4_val = 4, 7, 42, 100

    expanded_textInput = False
    text_val = "Please, type the coefficient here."
    multiText_val = "Type your message here."

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

        imgui.set_next_window_size(500, 400, imgui.ONCE)
        imgui.begin("Input widgets")

        # Input widgets

        # Float input
        expanded_floatInput, visible_header = imgui.collapsing_header(
            "Float input", visible_header)

        if expanded_floatInput:
            changed, float_val_1 = imgui.input_float("Input float 1.1", float_val_1)
            imgui.text("You wrote: {}".format(float_val_1))

            changed, float_val_2 = imgui.input_float("Input float 1.2", float_val_2,
                step = 1.0, step_fast = 5.0)
            imgui.text("You wrote: {}".format(float_val_2))

            imgui.separator()

            changed, float2_val = imgui.input_float2("Input float 2", *float2_val)
            imgui.text("You wrote: {} and {}".format(float2_val[0], float2_val[1]))

            imgui.separator()

            changed, float3_val = imgui.input_float3("Input float 3", *float3_val)
            imgui.text("You wrote: {}, {} and {}".format(
                float3_val[0],
                float3_val[1],
                float3_val[2]
                )
            )

            imgui.separator()

            changed, float4_val = imgui.input_float4("Input float 4", *float4_val)
            imgui.text("You wrote: {}, {}, {} and {}".format(
                float4_val[0],
                float4_val[1],
                float4_val[2],
                float4_val[3]
                )
            )

        expanded_intInput, visible_header = imgui.collapsing_header("Int input",
            visible_header)

        if expanded_intInput:
            changed, int_val_1 = imgui.input_int("Input int 1.1", int_val_1)
            imgui.text("You wrote: {}".format(int_val_1))

            changed, int_val_2 = imgui.input_int("Input int 1.2", int_val_2,
                step = 1.0, step_fast = 5.0)
            imgui.text("You wrote: {}".format(int_val_2))

            imgui.separator()

            changed, int2_val = imgui.input_int2("Input int 2", *int2_val)
            imgui.text("You wrote: {} and {}".format(int2_val[0], int2_val[1]))

            imgui.separator()

            changed, int3_val = imgui.input_int3("Input int 3", *int3_val)
            imgui.text("You wrote: {}, {} and {}".format(
                int3_val[0],
                int3_val[1],
                int3_val[2]
                )
            )

            imgui.separator()

            changed, int4_val = imgui.input_int4("Input int 4", *int4_val)
            imgui.text("You wrote: {}, {}, {} and {}".format(
                int4_val[0],
                int4_val[1],
                int4_val[2],
                int4_val[3]
                )
            )

        expanded_textInput, visible_header = imgui.collapsing_header("Text input",
            visible_header)
        if expanded_textInput:
            changed, text_val = imgui.input_text(
                "Amount:",
                text_val,
                256
            )

            imgui.text("You wrote: {}".format(text_val))

            imgui.separator()

            changed, multiText_val = imgui.input_text_multiline(
                "Message:",
                multiText_val,
                2056
            )

            imgui.text("You wrote:\n{}".format(multiText_val))

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
