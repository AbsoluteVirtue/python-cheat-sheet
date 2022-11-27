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

    # Custom variables used by elements in the UI
    # must be defined before the while-loop
    value = 10

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

        # Construction window 1
        imgui.set_next_window_size(500, 400, imgui.ONCE)
        imgui.begin("Window 1")

        # Create group
        imgui.begin_group() # element has no parameters

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
