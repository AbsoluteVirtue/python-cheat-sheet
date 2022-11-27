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
    pygame.display.set_caption("Pyimgui: 20_sliders")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    visible_header = None

    slider_expanded = False
    value_slider_1 = 50.0
    value_slider_2 = 10.5, 70.0
    value_slider_3 = 7.5, 90.0, 42.0
    value_slider_4 = 7.5, 90.0, 42.0, 77.0

    value_intSlider_1 = 1
    value_intSlider_2 = 20, 40
    value_intSlider_3 = 20, 40, 100
    value_intSlider_4 = 20, 40, 100, 42

    drag_expanded = False
    value_floatDrag_1 = 500.5
    value_floatDrag_2 = 420, 770.5
    value_floatDrag_3 = 420, 770.5, 220
    value_floatDrag_4 = 420, 770.5, 220, 590.3

    value_intDrag_1 = 500
    value_intDrag_2 = 420, 770
    value_intDrag_3 = 420, 770, 220
    value_intDrag_4 = 420, 770, 220, 590

    verticalSlider_expanded = False
    value_vSlider_float = 42.424242
    value_vSlider_int = 42

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

        imgui.set_next_window_size(500, 600, condition = imgui.ONCE)
        imgui.begin("Sliders")

        slider_expanded, visible_header = imgui.collapsing_header(
            "Slider", visible_header)
        if slider_expanded:
            # Slider to set a float value between a defined min and max value
            changed, value_slider_1 = imgui.slider_float("Slider floats 1",
                value_slider_1, min_value = 0.0, max_value = 100.0, power = 1.0)

            imgui.text("Value: %s" % value_slider_1)

            imgui.separator()

            # Slider with 2 float values
            changed, value_slider_2 = imgui.slider_float2("Slider floats 2",
                *value_slider_2, min_value = 0.0, max_value = 100, power = 1.0)

            imgui.text("Value 1: {}\nValue 2: {}".format(round(value_slider_2[0],3),
                                                        round(value_slider_2[1],3)))

            imgui.separator()

            # Slider for 3 float values
            changed, value_slider_3 = imgui.slider_float3("Slider floats 3",
                *value_slider_3, min_value = 0, max_value = 100, power = 1.0)

            imgui.text("Value 1: {}\nValue 2: {}\nValue 3: {}".format(
                round(value_slider_3[0],3),
                round(value_slider_3[1],3),
                round(value_slider_3[2],3)
                )
            )

            imgui.separator()

            # Slider for 4 float values
            changed, value_slider_4 = imgui.slider_float4("Slider floats 4",
                *value_slider_4, min_value = 0, max_value = 100, power = 1.0)

            imgui.text("Value 1: {}\nValue 2: {}\nValue 3: {}\nValue 4: {}".format(
                round(value_slider_4[0],3),
                round(value_slider_4[1],3),
                round(value_slider_4[2],3),
                round(value_slider_4[3],3),
                )
            )

            imgui.separator()

            # Slider for 1 int value
            changed, value_intSlider_1 = imgui.slider_int("Slider int 1",
                value_intSlider_1, min_value = 0, max_value = 100)

            imgui.text("Value: {}".format(value_intSlider_1))

            imgui.separator()

            # Slider for 2 int values
            changed, value_intSlider_2 = imgui.slider_int2("Slider int 2",
                *value_intSlider_2, min_value = 0, max_value = 100)

            imgui.text("Value 1: {}\nValue 2: {}".format(value_intSlider_2[0],
                value_intSlider_2[1]))

            imgui.separator()

            # Slider for 3 int values
            changed, value_intSlider_3 = imgui.slider_int3("Slider int 3",
                *value_intSlider_3, min_value = 0, max_value = 100)

            imgui.text("Value 1: {}\nValue 2: {}\nValue 3: {}".format(
                value_intSlider_3[0], value_intSlider_3[1], value_intSlider_3[2]))

            imgui.separator()

            # Slider for 4 int values
            changed, value_intSlider_4 = imgui.slider_int4("Slider int 4",
                *value_intSlider_4, min_value = 0, max_value = 100)

            imgui.text("Value 1: {}\nValue 2: {}\nValue 3: {}\nValue 4: {}".format(
                value_intSlider_4[0], value_intSlider_4[1],
                value_intSlider_4[2], value_intSlider_4[3]))

        # Drag
        drag_expanded, visible_header = imgui.collapsing_header("Drag", visible_header)
        if drag_expanded:
            changed, value_floatDrag_1 = imgui.drag_float("Drag float 1",
                value_floatDrag_1, change_speed = 10.0,
                min_value = 0, max_value = 1000)

            imgui.text("Value: {}".format(round(value_floatDrag_1)))

            imgui.separator()

            changed, value_floatDrag_2 = imgui.drag_float2("Drag float 2",
                *value_floatDrag_2, change_speed = 10.0,
                min_value = 0, max_value = 1000)

            imgui.text("Value 1: {}\nValue 2: {}".format(
                round(value_floatDrag_2[0]),
                round(value_floatDrag_2[1])
                )
            )

            imgui.separator()

            changed, value_floatDrag_3 = imgui.drag_float3("Drag float 3",
                *value_floatDrag_3, change_speed = 10.0,
                min_value = 0, max_value = 1000)

            imgui.text("Value 1: {}\nValue 2: {}\nValue 3: {}".format(
                round(value_floatDrag_3[0]),
                round(value_floatDrag_3[1]),
                round(value_floatDrag_3[2])
                )
            )

            imgui.separator()

            changed, value_floatDrag_4 = imgui.drag_float4("Drag float 4",
                *value_floatDrag_4, change_speed = 10.0,
                min_value = 0, max_value = 1000)

            imgui.text("Value 1: {}\nValue 2: {}\nValue 3: {}\nValue 4: {}".format(
                round(value_floatDrag_4[0]),
                round(value_floatDrag_4[1]),
                round(value_floatDrag_4[2]),
                round(value_floatDrag_4[3])
                )
            )

            imgui.separator()

            changed, value_intDrag_1 = imgui.drag_int("Drag int 1",
                value_intDrag_1, change_speed = 10.0,
                min_value = 0, max_value = 1000)

            imgui.separator()

            changed, value_intDrag_2 = imgui.drag_int2("Drag int 2",
                *value_intDrag_2, change_speed = 10.0,
                min_value = 0, max_value = 1000)

            imgui.separator()

            changed, value_intDrag_3 = imgui.drag_int3("Drag int 3",
                *value_intDrag_3, change_speed = 10.0,
                min_value = 0, max_value = 1000)

            imgui.separator()

            changed, value_intDrag_4 = imgui.drag_int4("Drag int 4",
                *value_intDrag_4, change_speed = 10.0,
                min_value = 0, max_value = 1000)
        verticalSlider_expanded, visible_header = imgui.collapsing_header(
            "Vertical slider", visible_header
        )
        if verticalSlider_expanded:
            changed, value_vSlider_float = imgui.v_slider_float(
                "Vertical slider float", 20, 100, value_vSlider_float,
                min_value = 0, max_value = 100, power = 1
            )

            changed, value_vSlider_int = imgui.v_slider_int(
                "Vertical slider int", 20, 100, value_vSlider_int,
                min_value = 20, max_value = 100
            )


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
