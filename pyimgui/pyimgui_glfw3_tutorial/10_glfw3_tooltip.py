# @Copyright: 2018 LuminousLizard
# @Project: Pyimgui-user-friendly
# @License: BSD-3

# -*- coding: utf-8 -*

# required packages
# GUI library
import imgui
from imgui.integrations.glfw import GlfwRenderer
# render engine
import glfw
import OpenGL.GL as gl


# Entry point of the application
def main():
    # Initialization of the main window via GLFW
    window = init_glfw()

    if glfw.vulkan_supported():
        print("Vulkan support available.")

    imgui.create_context()

    # Execute rendering of window via GLFWRenderer
    render_engine = GlfwRenderer(window)

    # Main loop which is executed during the entire execution time of the program
    # This loop contains all widgets or at least the embedding of elements which are defined outside the loop.
    while not glfw.window_should_close(window):
        # Event handler for input
        glfw.poll_events()
        # Set screen title (element, str title)
        glfw.set_window_title(window, "Pyimgui-examples: 00_base_app")
        # Set window size (element, int width, int height)
        glfw.set_window_size(window, 1024, 768)

        # OpenGL options can be included
        # Set background color of the window (rgba)
        gl.glClearColor(0.1, 0.1, 0.1, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        render_engine.process_inputs()

        # Set a new frame inside the window (defined above) which holds the widgets (below)
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
            imgui.columns(2, "Table") # Start: Number of columns / table title
            imgui.text("Column 1")
            imgui.next_column()
            imgui.text("Column 2")
            imgui.next_column()
            imgui.text("... and a ...")
            imgui.next_column()
            imgui.text("... table.")
            imgui.columns(1) # Closure of the table

            # Closure of the complex tooltip
            imgui.end_tooltip()

        # Closure of the window
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


# Main function call if file is executed via python
if __name__ == "__main__":
    main()
