# @Copyright: 2018 LuminousLizard
# @Project: Pyimgui-user-friendly
# @License: BSD-3

# -*- coding: utf-8 -*

# required packages
# Import render engine
import glfw
import OpenGL.GL as gl

# Import imgui-glfw-integration
from imgui.integrations.glfw import GlfwRenderer

# Import elements from separate py-file
from demo_window_impl_elements import *


# Main function
# It creates the instance and the program loop, and holds the
# frames and individual windows.
# It's called at the bottom of this file to start the application.
def main():
    window = init_glfw()

    imgui.create_context()

    render_engine = GlfwRenderer(window)

    # Headers
    visible_header = None

    while not glfw.window_should_close(window):
        glfw.poll_events()
        # Set screen title
        glfw.set_window_title(window, "PyImgui: Demo window [glfw3 backend]")
        # Set window size
        glfw.set_window_size(window, 1024, 768)

        # OpenGL options can be included
        # Set background color of the window (rgba)
        gl.glClearColor(0.1, 0.1, 0.1, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        render_engine.process_inputs()

        imgui.new_frame()

        # ------------------------
        # GUI code
        # ------------------------

        # Main Window
        # Optional: Determine the size of the window ...
        imgui.set_next_window_size(600, 700, condition = imgui.ONCE)

        # ... which is created.
        imgui.begin("PyImGui: Demo window",
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

        # ---------------
        # GUI code end
        # ---------------

        # Executes rendering the elements above
        imgui.render()
        render_engine.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

        # If there was a break from the main loop ...
        # ... termination of the rendering process and ...
    render_engine.shutdown()
    # ... termination of GLFW and all his open window
    glfw.terminate()


def init_glfw():
    # Initialize the GLFW library
    if not glfw.init():
        return

    # OpenGL 3 or above is required
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # OpenGL context should be forward-compatible
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a window in windowed mode and it's OpenGL context
    primary = glfw.get_primary_monitor()  # for GLFWmonitor
    window = glfw.create_window(
        1024,  # width, is required here but overwritten by "glfw.set_window_size()" above
        768,  # height, is required here but overwritten by "glfw.set_window_size()" above
        "pyimgui-examples-glfw",  # window name, is overwritten by "glfw.set_window_title()" above
        None,  # GLFWmonitor: None = windowed mode, 'primary' to choose fullscreen (resolution needs to be adjusted)
        None  # GLFWwindow
    )

    # Exception handler if window wasn't created
    if not window:
        glfw.terminate()
        return

    # Makes window current on the calling thread
    glfw.make_context_current(window)

    # Passing window to main()
    return window


if __name__ == "__main__":
    main()
