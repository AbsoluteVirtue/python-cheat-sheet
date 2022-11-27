# @Copyright: 2018 LuminousLizard
# @Project: Pyimgui-user-friendly
# @License: BSD-3

# -*- coding: utf-8 -*

# required packages
import sys

# Import render engine
import pygame
import OpenGL.GL as gl

# Import imgui-pygame-integration
from imgui.integrations.pygame import PygameRenderer

# Import elements from separate py-file
from demo_window_impl_elements import *


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
    pygame.display.set_caption("PyImGui: Demo window [pygame backend]")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    # NOTE: Variables containing the state of elements e.g. checkboxes,
    # radiobutton, coloredits or slider must be defined before main loop

    # Headers
    visible_header = None

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
        # ------------------------

        # Main Window
        # Optional: Determine the size of the window ...
        imgui.set_next_window_size(600, 700, condition = imgui.ONCE)

        # ... which is created.
        imgui.begin(
            "PyImGui: Demo window",
            flags = winOps_NoTitlebar | winOps_NoMove | winOps_Menu | winOps_NoScrollbar | winOps_NoResize | winOps_NoCollapse)

        imgui.text("Dear ImGui and Pyimgui says hello.")

        # Menu bar in the window
        if imgui.begin_menu_bar():
            if imgui.begin_menu("Menu"):
                WindowMenuBar_Menu()
                imgui.end_menu()
            if imgui.begin_menu("Examples"):
                _, state_mainMenuBar = imgui.menu_item("Main menu bar",
                    enabled = False)
                _, state_console = imgui.menu_item("Console",
                    enabled = False)
                _, state_log = imgui.menu_item("Log",
                    enabled = False)
                _, state_simpleLayout = imgui.menu_item("Simple layout",
                    enabled = False)
                _, state_propEditor = imgui.menu_item("Property editor",
                    enabled = False)
                _, state_longTextDisplay = imgui.menu_item("Long text display",
                    enabled = False)
                _, state_autoResizeWin = imgui.menu_item("Auto-resizing window",
                    enabled = False)
                _, state_constrResizeWin = imgui.menu_item("Constraining-resizing window",
                    enabled = False)
                _, state_simpleOverlay = imgui.menu_item("Simple overlay",
                    enabled = False)
                _, state_manipWinTitle = imgui.menu_item("Manipulating window title",
                    enabled = False)
                _, state_CustomRender = imgui.menu_item("Custom rendering",
                    enabled = False)

                imgui.end_menu()
            if imgui.begin_menu("Help"):
                _, state_metrics = imgui.menu_item("Metrics",
                    enabled = False)
                _, state_styleEditor = imgui.menu_item("Style Editor",
                    enabled = False)
                _, state_aboutImgui = imgui.menu_item("About ImGui",
                    enabled = False)
                _, state_aboutPyimgui = imgui.menu_item("About Pyimgui",
                    enabled = False)
                imgui.end_menu()
            imgui.end_menu_bar()

        # Header: Help
        # In this example the widgets are grouped in headers,
        # which can be expanded
        expanded_help, visible_header = imgui.collapsing_header(
            "Help", visible_header)
        # If the header is expanded ...
        if expanded_help:
            # ... following function is called, which includes the content
            header_help()

        expanded_configuration, visible_header = imgui.collapsing_header(
            "Configuration", visible_header)
        # If the header is expanded ...
        if expanded_configuration:
            header_configuration()

        # Header: Window options
        expanded_winOptions, visible_header = imgui.collapsing_header(
            "Window options", visible_header)
        # If the header is expanded ...
        if expanded_winOptions:
            header_winOptions()

        # Header: Widgets
        expanded_widgets, visible_header = imgui.collapsing_header(
            "Widgets", visible_header)
        # If the header is expanded ...
        if expanded_widgets:
            header_widgets()

        # Header: Graphs Widgets
        expanded_graphsWidgets, visible_header = imgui.collapsing_header(
            "Graphs widgets", visible_header)
        # If the header is expanded ...
        if expanded_graphsWidgets:
            header_graphWidgets()

        # Header: Layout
        expanded_layout, visible_header = imgui.collapsing_header(
            "Layout", visible_header)
        # If the header is expanded ...
        if expanded_layout:
            header_layout()

        # Header: Popups and Modal windows
        expanded_popupsModalWin, visible_header = imgui.collapsing_header(
            "Popups & Modal windows", visible_header)
        # If the header is expanded ...
        if expanded_popupsModalWin:
            header_popupsModalWin()

        # Header: Columns
        expanded_columns, visible_header = imgui.collapsing_header(
            "Columns", visible_header)
        # If the header is expanded ...
        if expanded_columns:
            header_columns()

        # Header: Filtering
        expanded_filtering, visible_header = imgui.collapsing_header(
            "Filtering", visible_header)
        # If the header is expanded ...
        if expanded_filtering:
            header_filtering()

        # Header: Keyboard, Mouse & Focus
        expanded_KeyMouseFocus, visible_header = imgui.collapsing_header(
            "Keyboard, Mouse & Focus", visible_header)
        # If the header is expanded ...
        if expanded_KeyMouseFocus:
            header_keyMouseFocus()

        imgui.end()

        # ------------------------
        # End GUI code
        # ------------------------

        # note: cannot use screen.fill((1, 1, 1)) because pygame's screen
        #       does not support fill() on OpenGL sufraces
        gl.glClearColor(0.1, 0.1, 0.1, 1) # Background color of the main screen
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.render()
        render_engine.render(imgui.get_draw_data())

        # Update the full display surface to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
