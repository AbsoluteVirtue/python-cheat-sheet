# @Copyright: 2018 LuminousLizard
# @Project: Pyimgui-user-friendly
# @License: BSD-3

# -*- coding: utf-8 -*
import imgui

from math import sin
from array import array

# Global variables
# Variables: Menubar
state_menu_options = True
value_slider_menu = 0.5
value_input_menu = 0.5
value_combo_menu = 0
list_combo_menu = ["Yes", "No", "Maybe"]
list_colors_menu = ["Text", "TextDisabled", "WindowBg", "ChildWindowBG", "PopupBg",
    "Border", "BorderShadow", "FrameBg", "FrameBgHovered", "FrameBgActive", "TitleBg",
    "TitleBgCollapsed", "TitleBgActive", "MenuBar", "ScrollbarBg", "ScrollbarGrab",
    "ScrollbarGrabHovered", "ScrollbarGrabActive", "ComboBg", "CheckMark", "SliderGrab",
    "SliderGrabActive", "Button", "ButtonHovered", "ButtonActive", "Header",
    "HeaderHovered", "HeaderActive", "Column", "ColumnHovered", "ColumnActive",
    "ResizeGrip", "ResizeGripHovered", "ResizeGripActive", "CloseButton",
    "CloseButtonHovered", "CloseButtonActive", "PlotLines", "PlotLinesHovered",
    "PlotHistogram", "PlotHistogramHovered", "TextSelectedBg", "ModalWindowDarkening"]

# Variable: Window options
winOps_NoTitlebar = 0
state_winOps_NoTitlebar = False

winOps_NoMove = 0
state_winOps_NoMove = False

winOps_Menu = 1024
state_winOps_Menu = False

winOps_NoBorder = None
state_winOps_NoBorder = None

winOps_NoScrollbar = 0
state_winOps_NoScrollbar = False

winOps_NoResize = 0
state_winOps_NoResize = False

winOps_NoCollapse = 0
state_winOps_NoCollapse = False

# Variables: Configuration
state_Config_NavEnableKeyboard = False
state_Config_NavEnableGamepad = False
state_Config_NavEnableSetMousePos = False
state_Config_NoMouse = False
state_Config_NoMouseCursorChange = False
state_Config_InputTextCursorBlink = True
state_Config_ResizeWindowsFromEdge = False
state_Config_MouseDrawCursor = False

state_Config_HasGamepad = False
state_Config_HasMouseCursors = False
state_Config_HasSetMousePos = False

# Variables: Widgets
# Basic
state_widgets_button = False
var_widgets_text = ""
# Selectables
state_selectables = [False, True, False, False]

state_selectables_grid = [[True, False, False, False],
                          [False, True, False, False],
                          [False, False, True, False],
                          [False, False, False, True]]

# Node: Filtered Text Input
var_filtered_text_default = ""
var_filtered_text_decimal = ""
var_filtered_text_hexadecimal = ""
var_filtered_text_uppercase = ""
var_filtered_text_no_blank = ""
var_filtered_text_password = "password123"

# Widget overview
state_checkbox = True
state_radioButton = [True, False, False]
button_clicked = ""

state_extraGroup = True
expanded_extraGroup = None

state_readOnly = False
text_inputMultiline = "/*\nThe Pentium F00F bug, shorthand for F0 0F C7 C8,\n" \
                      "the hexadecimal encoding of one offending instruction,\n" \
                      "more formally, the invalid operand with locked CMPXCHG8B\n" \
                      "instruction bug, is a design flaw in the majority of\n" \
                      "Intel Pentium, Pentium MMX, and Pentium OverDrive\n" \
                      "processors (all in the P5 microarchitecture).\n*/" \
                      "\n\nlabel:\n\tlock cmpxchg8b eax"

var_textWrap = 250

# Combobox
var_combo_current = 1
var_combo_items = ["aaaa", "bbbb", "cccc", "dddd", "eeee", ""] # empty item at the end to prevent a bug

var_comboScroll_current = 12
var_comboScroll_items = ["AAAA", "BBBB", "CCCC", "DDDD", "EEEE", "FFFF",
                   "GGGG", "HHHH", "IIII", "JJJJ", "KKKK"]

# Input widgets
var_inputText = "Hello, world!"
var_inputInt = 123
var_inputFloat1 = 0.001
var_inputDouble = 999999.00000001
var_inputFloat3 = 0.1, 0.2, 0.3

# Drag widgets
var_dragInt1 = 50
var_dragInt2 = 42
var_dragFloat1 = 1.0
var_dragSmallFloat = 0.006700

# Sliders
var_sliderInt1 = 0
var_sliderFloat = 0.123
var_sliderFloat_log = 0
var_sliderFloat_angle = 0

# Listbox
var_listbox_current = 1
var_listbox_items = ["Apple", "Banana", "Cherry", "Kiwi", "Mango",
                     "Orange", "Pineapple", "Strawberry", "Watermelon"]

# Colors
new_color1 = 1.0, 0, 0.1
new_color2 = 0.4, 0.7, 0, 0.5

# Multi-component widgets
var_float1 = 0.1
var_float2 = 0.2
var_float3 = 0.3
var_float4 = 0.44
var_int1 = 1
var_int2 = 5
var_int3 = 100
var_int4 = 255

# Vertical slider
var_vSlider_int = 0
var_vSlider_float = [0.0, 0.6, 0.35, 0.9, 0.7, 0.2, 0, 0.2, 0.8, 0.4, 0.25]
var_vSlider_float_2 = [0.2, 0.8, 0.4, 0.25]

# Variable: Layout
var_ChildRegion_Goto = 1
var_WidgetWidth = 100
state_layout = [False, False, False, False]
var_combo_layout_items = ["AAAA", "BBBB", "CCCC", "DDDD", ""]
var_combo_layout_current = 4

var_slider_layout = [1, 2, 3]

# Elements
# Main menu bar
def main_menu_bar():
    if imgui.begin_main_menu_bar():
        # Create first dropdown
        # Syntax: imgui.begin_menu(string label, bool activated?)
        if imgui.begin_menu("Menu", True):
            # Create menu items
            # Syntax: imgui.menu_item(string label, string shortcut,
            #                        bool checked, bool activated)
            imgui.menu_item("New", "Ctrl+N", True, False)
            imgui.menu_item("Open", "Ctrl+O", False, True)

            # Create menu item with submenu
            if imgui.begin_menu("Save as", True):
                imgui.menu_item("*.txt", None, False, True)
                imgui.end_menu() # Close submenu

            # Close first dropdown
            imgui.end_menu()

        # Create second dropdown with new "if" statement
        # Like the first dropdown, the second is also included in the
        # the "begin_main_menu_bar" block.
        if imgui.begin_menu("About", True):
            imgui.menu_item("Info")

            # Close second dropdown
            imgui.end_menu()

        # Close main menu
        imgui.end_main_menu_bar()

# Window menu
def WindowMenuBar_Menu():
    global value_slider_menu
    global value_input_menu
    global value_combo_menu
    global list_combo_menu
    global list_colors_menu
    global state_menu_options
    # Menu bar in the window
    imgui.menu_item("(dummy menu)", enabled = False)
    imgui.menu_item("New")
    imgui.menu_item("Open", "Ctrl+O")
    if imgui.begin_menu("Open Recent"):
        imgui.menu_item("fish_hat.c")
        imgui.menu_item("fish_hat.inl")
        imgui.menu_item("fish_hat.h")
        if imgui.begin_menu("More"):
            imgui.menu_item("Hello")
            imgui.menu_item("Sailor")
            if imgui.begin_menu("Recurse.."):
                WindowMenuBar_Menu()
                imgui.end_menu()
            imgui.end_menu()
        imgui.end_menu()
    imgui.menu_item("Save", "Ctrl+S")
    imgui.menu_item("Save As")
    imgui.separator()
    if imgui.begin_menu("Options"):
        _, state_menu_options = imgui.menu_item("Enabled", selected = state_menu_options)
        imgui.begin_child("region", 300, 100, border = True)
        imgui.text("Scrolling Text 1")
        imgui.text("Scrolling Text 2")
        imgui.text("Scrolling Text 3")
        imgui.text("Scrolling Text 4")
        imgui.text("Scrolling Text 5")
        imgui.text("Scrolling Text 6")
        imgui.text("Scrolling Text 7")
        imgui.text("Scrolling Text 8")
        imgui.text("Scrolling Text 9")
        imgui.end_child()

        _, value_slider_menu = imgui.slider_float("Value",
            value = value_slider_menu, min_value = 0, max_value = 1)
        _, value_input_menu = imgui.input_float("Input",
            value = value_input_menu, step = 0.1)
        _, value_combo_menu = imgui.combo("Combo",
            value_combo_menu, list_combo_menu)

        imgui.end_menu()

    if imgui.begin_menu("Colors"):
        for i in list_colors_menu:
            imgui.menu_item(i)
        imgui.end_menu()
    if imgui.begin_menu("Disabled", enabled = False):
        imgui.end_menu()
    imgui.menu_item("Checked", selected = True)
    imgui.menu_item("Quit", "Alt+F4")

# Header: Help
def header_help():
    imgui.push_text_wrap_pos(0.0)
    imgui.text("This window is a rewrite of the DemoWindow() "
        "function in Python/Pyimgui. Please refer to the code for "
        "programming reference.")
    imgui.separator()
    imgui.text("PROGRAMMER GUIDE:")
    imgui.bullet_text("Please see the code in \"demo_window_impl_elements.py\".")
    imgui.bullet_text("Please see the coments in \"core.pyx\" or the official documentation.")
    imgui.bullet_text("Please see the examples in the \"doc\" folder.")
    imgui.pop_text_wrap_pos()
    imgui.text("\nUser Guide:")
    imgui.show_user_guide()

# Header: Configurations
def header_configuration():
    if imgui.tree_node("Configuration##Header"):
        imgui.push_style_color(imgui.COLOR_TEXT, 255, 0, 0)
        imgui.checkbox("io.ConfigFlags: NavEnableKeyboard", state = state_Config_NavEnableKeyboard)
        imgui.checkbox("io.ConfigFlags: NavEnableGamepad", state=state_Config_NavEnableGamepad)
        imgui.checkbox("io.ConfigFlags: NavEnableSetMousePos", state=state_Config_NavEnableSetMousePos)
        imgui.checkbox("io.ConfigFlags: NoMouse", state=state_Config_NoMouse)
        imgui.checkbox("io.ConfigFlags: NoMouseCursorChange", state=state_Config_NoMouseCursorChange)
        imgui.checkbox("io.ConfigInputTextCursorBlink", state=state_Config_InputTextCursorBlink)
        imgui.checkbox("io.ConfigResizeWindowsFromEdge [beta]", state=state_Config_ResizeWindowsFromEdge)
        imgui.checkbox("io.MouseDrawCursor", state=state_Config_MouseDrawCursor)
        imgui.pop_style_color()
        imgui.tree_pop()

    if imgui.tree_node("Backend Flags"):
        imgui.push_style_color(imgui.COLOR_TEXT, 255, 0, 0)
        imgui.checkbox("io.BackendFlags: HasGamepad", state = state_Config_HasGamepad)
        imgui.checkbox("io.BackendFlags: HasMouseCursors", state=state_Config_HasMouseCursors)
        imgui.checkbox("io.BackendFlags: HasSetousePos", state=state_Config_HasSetMousePos)
        imgui.pop_style_color()
        imgui.tree_pop()

    if imgui.tree_node("Style"):
        imgui.show_style_editor()
        imgui.tree_pop()

    if imgui.tree_node("Capture/Logging"):
        imgui.tree_pop()

# Header: Window options
def header_winOptions():
    global winOps_NoTitlebar
    global state_winOps_NoTitlebar

    global winOps_NoMove
    global state_winOps_NoMove

    global winOps_Menu
    global state_winOps_Menu

    global winOps_NoBorder
    global state_winOps_NoBorder

    global winOps_NoScrollbar
    global state_winOps_NoScrollbar

    global winOps_NoResize
    global state_winOps_NoResize

    global winOps_NoCollapse
    global state_winOps_NoCollapse

    imgui.begin_group()

    _, state_winOps_NoTitlebar = imgui.checkbox("No titlebar", state_winOps_NoTitlebar)
    if state_winOps_NoTitlebar == True:
        winOps_NoTitlebar = 1
    else:
        winOps_NoTitlebar = 0

    _, state_winOps_NoMove = imgui.checkbox("No move", state_winOps_NoMove)
    if state_winOps_NoMove == True:
        winOps_NoMove = 4
    else:
        winOps_NoMove = 0

    imgui.push_style_color(imgui.COLOR_TEXT, 1, 0, 0)
    imgui.checkbox("No close", False)
    imgui.pop_style_color()

    imgui.end_group()
    imgui.same_line()
    imgui.begin_group()

    _, state_winOps_NoScrollbar = imgui.checkbox("No scrollbar", state_winOps_NoScrollbar)
    if state_winOps_NoScrollbar == True:
        winOps_NoScrollbar = 8
    else:
        winOps_NoScrollbar = 0

    _, state_winOps_NoResize = imgui.checkbox("No resize", state_winOps_NoResize)
    if state_winOps_NoResize == True:
        winOps_NoResize = 2
    else:
        winOps_NoResize = 0

    imgui.push_style_color(imgui.COLOR_TEXT, 1, 0, 0)
    imgui.checkbox("No nav", False)
    imgui.pop_style_color()

    imgui.end_group()
    imgui.same_line()
    imgui.begin_group()

    _, state_winOps_Menu = imgui.checkbox("No menu", state_winOps_Menu)
    if state_winOps_Menu == True:
        winOps_Menu = 0
    else:
        winOps_Menu = 1024

    _, state_winOps_NoCollapse = imgui.checkbox("No collapse", state_winOps_NoCollapse)
    if state_winOps_NoCollapse == True:
        winOps_NoCollapse = 32
    else:
        winOps_NoCollapse = 0

    imgui.end_group()

# Header: Widgets
def header_widgets():
    # Basic
    global state_widgets_button
    global var_widgets_text
    # First widgets
    global state_checkbox
    global state_radioButton
    global button_clicked
    global state_extraGroup
    global expanded_extraGroup
    global var_textWrap
    global state_readOnly
    global text_inputMultiline
    # Combobox
    global var_combo_current
    global var_comboScroll_current
    # Input widgets
    global var_inputText
    global var_inputInt
    global var_inputFloat1
    global var_inputDouble
    global var_inputFloat3
    # Drag widgets
    global var_dragInt1
    global var_dragInt2
    global var_dragFloat1
    global var_dragSmallFloat
    # Slider
    global var_sliderInt1
    global var_sliderFloat
    global var_sliderFloat_log
    global var_sliderFloat_angle
    # Listbox
    global var_listbox_current
    global var_listbox_items
    # Color edit
    global new_color1
    global new_color2

    # Filtered text input
    global var_filtered_text_default
    global var_filtered_text_decimal
    global var_filtered_text_hexadecimal
    global var_filtered_text_uppercase
    global var_filtered_text_no_blank
    global var_filtered_text_password

    # Multi-component widgets
    global var_float1
    global var_float2
    global var_float3
    global var_float4
    global var_int1
    global var_int2
    global var_int3
    global var_int4

    global var_vSlider_int
    global var_vSlider_float
    global var_vSlider_float_2

    visible_header = None
    #expanded_Header = False

    if imgui.tree_node("Basic"):
        # Button
        state_widgets_button = imgui.button("Button")
        if state_widgets_button == True:
            var_widgets_text = "Thanks for clicking me!"
        imgui.same_line()
        imgui.text(var_widgets_text)

        # Checkbox
        clicked, state_checkbox = imgui.checkbox("checkbox", state_checkbox)

        # Radiobutton
        imgui.begin_group()
        if imgui.radio_button("radio a", state_radioButton[0]):
            # Following statements handle the states of the radio buttons
            # Only one radio button can always be active
            # TODO: better state handling
            state_radioButton[0] = True
            state_radioButton[1] = False
            state_radioButton[2] = False

        imgui.same_line()

        if imgui.radio_button("radio b", state_radioButton[1]):
            state_radioButton[0] = False
            state_radioButton[1] = True
            state_radioButton[2] = False

        imgui.same_line()

        if imgui.radio_button("radio c", state_radioButton[2]):
            state_radioButton[0] = False
            state_radioButton[1] = False
            state_radioButton[2] = True
        imgui.end_group()

        for i in range(1, 8):
            if i > 1:
                imgui.same_line()
            # TODO: better color choice
            imgui.push_style_color(imgui.COLOR_BUTTON, i / 8, 0.6, 0.6)
            imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED, i / 8, 0.7, 0.7)
            imgui.push_style_color(imgui.COLOR_BUTTON_ACTIVE, i / 8, 0.8, 0.8)
            imgui.button("Click##Click_{}".format(i))
            imgui.pop_style_color(3)

        imgui.text("Hover over me ")
        if imgui.is_item_hovered():
            imgui.set_tooltip("I am a tooltip")
        imgui.same_line()
        imgui.text("- or me")
        if imgui.is_item_hovered():
            imgui.begin_tooltip()
            imgui.text("I am a fancy tooltip")
            imgui.plot_lines("Curve", array('f', [sin(x * 0.1) for x in range(100)]))
            # TODO: Adding curve if function is available
            imgui.end_tooltip()

        imgui.separator()

        imgui.label_text("label", "Value")

        # Combobox
        _, var_combo_current = imgui.combo(
            label="combo",
            current=var_combo_current,
            items=var_comboScroll_items
        )

        _, var_comboScroll_current = imgui.combo(
            label="combo scroll",
            current=var_comboScroll_current,
            items=var_comboScroll_items,
            height_in_items=7
        )

        # Input widgets
        _, var_inputText = imgui.input_text(
            label="input text",
            value=var_inputText,
            buffer_length=256
        )

        _, var_inputInt = imgui.input_int(
            label="input int",
            value=var_inputInt,
            step=1
        )

        _, var_inputFloat1 = imgui.input_float(
            label="input float",
            value=var_inputFloat1,
            step=0.01
        )

        _, var_inputDouble = imgui.input_double(
            label="input double",
            value=var_inputDouble,
            step=0.00000001
        )

        _, var_inputFloat3 = imgui.input_float3("input float3", *var_inputFloat3)

        _, var_dragInt1 = imgui.drag_int(
            label="drag int",
            value=var_dragInt1,
            change_speed=1.0,
        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("Click and drag to edit value.\n"
                              "Hold SHIFT/ALT for faster/slower edit.\n"
                              "Double-click or CTRL+click to input value.")

        _, var_dragInt2 = imgui.drag_int(
            label="drag int 0..100",
            value=var_dragInt2,
            change_speed=1.0,
            min_value=0,
            max_value=100,
            format="%.0f{}".format("%%")
        )

        _, var_dragFloat1 = imgui.drag_float(
            label="drag float",
            value=var_dragFloat1,
            change_speed=0.005
        )

        _, var_dragSmallFloat = imgui.drag_float(
            label="drag small float",
            value=var_dragSmallFloat,
            change_speed=0.0001,
            format="%.6f ns"
        )

        _, var_sliderInt1 = imgui.slider_int(
            "slider int",
            var_sliderInt1,
            min_value=-1,
            max_value=3
        )

        _, var_sliderFloat = imgui.slider_float(
            "slider float",
            var_sliderFloat,
            min_value=0.0,
            max_value=1.0,
            format="{}%.3f".format("ratio = ")
        )

        _, var_sliderFloat_log = imgui.slider_float(
            "slider log float",
            var_sliderFloat_log,
            min_value=-10,
            max_value=10,
            power=2,
            format="%.4f"
        )

        _, var_sliderFloat_angle = imgui.slider_float(
            "slider angle",
            var_sliderFloat_angle,
            min_value=-360,
            max_value=360,
            format="%.0f {}".format("deg")
        )

        # Color edit
        color_changed, new_color1 = imgui.color_edit3(
            "color 1",
            *new_color1
        )

        color_changed, new_color2 = imgui.color_edit4(
            "color 2",
            *new_color2
        )

        _, var_listbox_current = imgui.listbox(
            "listbox\n(single select)",
            var_listbox_current,
            var_listbox_items,
            height_in_items=4
        )

        # Range widgets
        if imgui.tree_node("Range Widgets"):
            imgui.push_style_color(imgui.COLOR_TEXT, 1, 0, 0)
            imgui.text("Not implemented yet")
            imgui.pop_style_color()
            imgui.tree_pop()

        imgui.tree_pop()


    if imgui.tree_node("Trees"):
        if imgui.tree_node("Basic trees"):
            # manual creation of nodes
            if imgui.tree_node("Child 0"):
                imgui.text("blah blah")
                imgui.same_line()
                if imgui.button("print", width = 50, height = 15):
                    print("Child 0 pressed")
                imgui.tree_pop()
            # functional creation of nodes
            for i in range(1, 5):
                if imgui.tree_node("Child " + str(i)):
                    imgui.text("blah blah")
                    imgui.same_line()
                    if imgui.button("print", width = 50, height = 15):
                        print("Child " + str(i) + " pressed")
                    imgui.tree_pop()
            # Close node "Basic trees"
            imgui.tree_pop()

        if imgui.tree_node("Advanced, with Selectable nodes"):
            imgui.tree_pop()
        imgui.tree_pop()

    if imgui.tree_node("Collapsing Headers"):
        expanded_Header, visible_header = imgui.collapsing_header(
            "Header", visible_header)

        if expanded_Header:
            # Checkbox to disable the "extraGroup" header
            _, state_extraGroup = imgui.checkbox("Enable extra group", state_extraGroup)
            for i in range(0, 5):
                imgui.text("Some content " + str(i))

        if state_extraGroup == True:

            expanded_extraGroup, visible_header = imgui.collapsing_header(
                "Header with a close button", visible_header)

            if expanded_extraGroup == True:
                for i in range(0, 5):
                    imgui.text("More content " + str(i))

        imgui.tree_pop()

    if imgui.tree_node("Bullets"):
        imgui.bullet_text("Bullet point 1")
        imgui.bullet_text("Bullet point 2\nOn multiple lines")

        imgui.bullet()
        imgui.same_line()
        imgui.text("Bullet point 3 (two calls)")

        imgui.bullet()
        imgui.same_line()
        imgui.button("Button")

        imgui.tree_pop()

    if imgui.tree_node("Colored Text"):

        imgui.push_style_color(imgui.COLOR_TEXT, 1, 0, 1, 1)
        imgui.text("Pink")
        imgui.pop_style_color()

        imgui.push_style_color(imgui.COLOR_TEXT, 1, 1, 0, 1)
        imgui.text("Yellow")
        imgui.pop_style_color()

        imgui.tree_pop()

    if imgui.tree_node("Word Wrapping"):
        imgui.push_text_wrap_pos(0.0)
        imgui.text("This text should automatically wrap on the edge of the window. "
            "The current implementation for tet wrapping follows simple rules suitable "
            "for English and possibly other laguages.")
        imgui.pop_text_wrap_pos()

        _, var_textWrap = imgui.slider_int("Wrap width", var_textWrap, min_value = 0, max_value = 600)

        imgui.text("Test paragraph 1:")
        imgui.push_style_color(imgui.COLOR_BORDER, 1, 1, 0, 1)
        imgui.begin_child("paragraph_1", width = var_textWrap, height = 100, border = True)
        imgui.push_text_wrap_pos(var_textWrap)
        imgui.text("The lazy dog is a good dog. This paragraph is made to fit within {} pixels. "
            "Testing a 1 character word. The quick brown fox jumps over the lazy dog.".format(var_textWrap))
        imgui.pop_text_wrap_pos()
        imgui.end_child()
        imgui.pop_style_color()

        imgui.text("Test paragraph 2:")
        imgui.push_style_color(imgui.COLOR_BORDER, 1, 1, 0, 1)
        imgui.begin_child("paragraph_2", width = var_textWrap, height = 100, border = True)
        imgui.push_text_wrap_pos(var_textWrap)
        imgui.text("aaaaaaaa bbbbbbbb, c cccccccc,dddddddd. d eeeeeeee   ffffffff. gggggggg!hhhhhhhh")
        imgui.pop_text_wrap_pos()
        imgui.end_child()
        imgui.pop_style_color()

        imgui.tree_pop()

    if imgui.tree_node("UTF-8 Text"):
        # TODO
        imgui.push_style_color(imgui.COLOR_TEXT, 1, 0, 0)
        imgui.text("Not implemented yet")
        imgui.pop_style_color()

        imgui.tree_pop()

    if imgui.tree_node("Images"):
        # TODO
        imgui.push_style_color(imgui.COLOR_TEXT, 1, 0, 0)
        imgui.text("Not implemented yet")
        imgui.pop_style_color()

        imgui.tree_pop()

    if imgui.tree_node("Selectables"):
        if imgui.tree_node("Basic"):
            _, state_selectables[0] = imgui.selectable("1. I am selectable", # label
                             selected = state_selectables[0], # default: False
                             flags = 0, # default: 0
                             width = 0, # default: 0
                             height = 0) # default: 0
            _, state_selectables[1] = imgui.selectable("2. I am selectable",
                             selected = state_selectables[1])
            imgui.text("3. I am not selectable") # TODO: Workaround with text element ??? Maybe there is a better way.
            _, state_selectables[2] = imgui.selectable("4. I am selectable",
                                                       selected = state_selectables[2])
            _, state_selectables[3] = imgui.selectable("5. I am double clickable",
                                                       selected = state_selectables[3],
                                                       flags = imgui.SELECTABLE_ALLOW_DOUBLE_CLICK) # Or: flags = 4
            imgui.tree_pop()

        if imgui.tree_node("Rendering more text into the same block"):
            imgui.selectable("main.py")
            imgui.same_line(position = 300)
            imgui.text(" 2,345 bytes")

            imgui.selectable("hello.py")
            imgui.same_line(position = 300)
            imgui.text("12,345 bytes")

            imgui.selectable("test.py")
            imgui.same_line(position = 300)
            imgui.text(" 2,345 bytes")

            imgui.tree_pop()

        if imgui.tree_node("Grid"):
            for grid_row in range(0, 4):
                for grid_column in range(0, 4):
                    if grid_row == grid_column:
                        _, state_selectables_grid[grid_row][grid_column] = imgui.selectable("Sailor\n{0} {1}".
                                                                                            format(grid_column, grid_row),
                                         selected = state_selectables_grid[grid_row][grid_column],
                                         width = 50,
                                         height = 50)
                    else:
                        _, state_selectables_grid[grid_row][grid_column] = imgui.selectable("Sailor\n{0} {1}".
                                                                                            format(grid_column, grid_row),
                                         selected = state_selectables_grid[grid_row][grid_column],
                                         width = 50,
                                         height = 50)
                    if grid_column != 3:
                        imgui.same_line()
            imgui.tree_pop()

        imgui.tree_pop()

    if imgui.tree_node("Filtered Text Input"):
        _, var_filtered_text_default = imgui.input_text(label = "default",
                         value = var_filtered_text_default,
                         buffer_length = 64,
                         flags = 0)

        _, var_filtered_text_decimal = imgui.input_text(label = "decimal",
                         value = var_filtered_text_decimal,
                         buffer_length = 64,
                         flags = imgui.INPUT_TEXT_CHARS_DECIMAL)

        _, var_filtered_text_hexadecimal = imgui.input_text(label = "hexadeciaml",
                         value = var_filtered_text_hexadecimal,
                         buffer_length = 64,
                         flags = imgui.INPUT_TEXT_CHARS_HEXADECIMAL)

        _, var_filtered_text_uppercase = imgui.input_text(label = "uppercase",
                         value = var_filtered_text_uppercase,
                         buffer_length = 64,
                         flags = imgui.INPUT_TEXT_CHARS_UPPERCASE)

        _, var_filtered_text_no_blank = imgui.input_text(label = "no blank",
                         value = var_filtered_text_no_blank,
                         buffer_length = 64,
                         flags = imgui.INPUT_TEXT_CHARS_NO_BLANK)

        # Password input
        imgui.text("Password input")
        _, var_filtered_text_password = imgui.input_text(label = "password",
                         value = var_filtered_text_password,
                         buffer_length = 64,
                         flags = imgui.INPUT_TEXT_PASSWORD | imgui.INPUT_TEXT_CHARS_NO_BLANK)

        _, var_filtered_text_password = imgui.input_text(label = "password (clear)",
                                                         value = var_filtered_text_password,
                                                         buffer_length = 64,
                                                         flags = imgui.INPUT_TEXT_CHARS_NO_BLANK)

        imgui.tree_pop()

    if imgui.tree_node("Multi-line Text Input"):
        _, state_readOnly = imgui.checkbox("Read-only", state_readOnly)

        if state_readOnly == True:
            _, text_inputMultiline = imgui.input_text_multiline(
                "Message",
                text_inputMultiline,
                buffer_length = 5000,
                width = 500,
                height = 200,
                flags = imgui.INPUT_TEXT_READ_ONLY
            )
        else:
            _, text_inputMultiline = imgui.input_text_multiline(
                "Message",
                text_inputMultiline,
                buffer_length = 5000,
                width = 500,
                height = 200
            )

        imgui.tree_pop()

# Multi-component widgets
    if imgui.tree_node("Multi-component Widgets"):
        # 2 values
        _, [var_float1, var_float2] = imgui.input_float2(
            "input float2",
            var_float1,
            var_float2
        )

        _, [var_float1, var_float2] = imgui.drag_float2(
            "drag float2",
            var_float1,
            var_float2,
            max_value = 1.0,
            min_value = 0.0
        )

        _, [var_float1, var_float2] = imgui.slider_float2(
            "slider float2",
            var_float1,
            var_float2,
            min_value = 0,
            max_value = 1
        )

        _, [var_int1, var_int2] = imgui.drag_int2(
            "drag int2",
            var_int1,
            var_int2,
            min_value = 0,
            max_value = 255
        )

        _, [var_int1, var_int2] = imgui.input_int2(
            "input int2",
            var_int1,
            var_int2,
        )

        _, [var_int1, var_int2] = imgui.slider_int2(
            "slider int2",
            var_int1,
            var_int2,
            min_value = 0,
            max_value = 255
        )

        imgui.new_line()

        # 3 values
        _, [var_float1, var_float2, var_float3] = imgui.input_float3(
            "input float3",
            var_float1,
            var_float2,
            var_float3
        )

        _, [var_float1, var_float2, var_float3] = imgui.drag_float3(
            "drag float3",
            var_float1,
            var_float2,
            var_float3,
            min_value = 0,
            max_value = 1
        )

        _, [var_float1, var_float2, var_float3] = imgui.slider_float3(
            "slider float3",
            var_float1,
            var_float2,
            var_float3,
            min_value = 0,
            max_value = 1
        )

        _, [var_int1, var_int2, var_int3] = imgui.drag_int3(
            "drag int3",
            var_int1,
            var_int2,
            var_int3,
            min_value = 0,
            max_value = 255
        )

        _, [var_int1, var_int2, var_int3] = imgui.input_int3(
            "input int3",
            var_int1,
            var_int2,
            var_int3,
        )

        _, [var_int1, var_int2, var_int3] = imgui.slider_int3(
            "slider int3",
            var_int1,
            var_int2,
            var_int3,
            min_value = 0,
            max_value = 255
        )

        imgui.new_line()

        # 4 values
        _, [var_float1, var_float2, var_float3, var_float4] = imgui.input_float4(
            "input float4",
            var_float1,
            var_float2,
            var_float3,
            var_float4
        )

        _, [var_float1, var_float2, var_float3, var_float4] = imgui.drag_float4(
            "drag float4",
            var_float1,
            var_float2,
            var_float3,
            var_float4,
            min_value = 0,
            max_value = 1
        )

        _, [var_float1, var_float2, var_float3, var_float4] = imgui.slider_float4(
            "slider float4",
            var_float1,
            var_float2,
            var_float3,
            var_float4,
            min_value = 0,
            max_value = 1
        )

        _, [var_int1, var_int2, var_int3, var_int4] = imgui.drag_int4(
            "drag int4",
            var_int1,
            var_int2,
            var_int3,
            var_int4,
            min_value = 0,
            max_value = 255
        )

        _, [var_int1, var_int2, var_int3, var_int4] = imgui.input_int4(
            "input int4",
            var_int1,
            var_int2,
            var_int3,
            var_int4
        )

        _, [var_int1, var_int2, var_int3, var_int4] = imgui.slider_int4(
            "slider int4",
            var_int1,
            var_int2,
            var_int3,
            var_int4,
            min_value = 0,
            max_value = 255
        )

        imgui.tree_pop()

    # Vertical slider
    if imgui.tree_node("Vertical Sliders"):
        _, var_vSlider_int = imgui.v_slider_int(
            "##Vertical slider 1",
            width = 20,
            height = 150,
            value = var_vSlider_int,
            min_value = 0,
            max_value = 5,
            format = "%.1f"
        )
        imgui.same_line()

        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, 1, 0, 0)
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, 1, 0, 0, 0.2)
        _, var_vSlider_float[0] = imgui.v_slider_float(
            "##Vertical slider 2",
            width = 20,
            height = 150,
            value = var_vSlider_float[0],
            min_value = 0.0,
            max_value = 1.0,
            format = "%.1f",
            power = 1

        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("{:.3f}".format(var_vSlider_float[0], 3))
        imgui.pop_style_color(2)

        imgui.same_line()

        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, 1, 1, 0)
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, 1, 1, 0, 0.2)
        _, var_vSlider_float[1] = imgui.v_slider_float(
            "##Vertical slider 3",
            width = 20,
            height = 150,
            value = var_vSlider_float[1],
            min_value = 0.0,
            max_value = 1.0,
            format = "%.1f",
            power = 1

        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("{:.3f}".format(var_vSlider_float[1], 3))
        imgui.pop_style_color(2)

        imgui.same_line()

        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, 0, 1, 0)
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, 0, 1, 0, 0.2)
        _, var_vSlider_float[2] = imgui.v_slider_float(
            "##Vertical slider 4",
            width = 20,
            height = 150,
            value = var_vSlider_float[2],
            min_value = 0.0,
            max_value = 1.0,
            format = "%.1f",
            power = 1

        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("{:.3f}".format(var_vSlider_float[2], 3))
        imgui.pop_style_color(2)

        imgui.same_line()

        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, 0, 1, 1)
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, 0, 1, 1, 0.2)
        _, var_vSlider_float[3] = imgui.v_slider_float(
            "##Vertical slider 5",
            width = 20,
            height = 150,
            value = var_vSlider_float[3],
            min_value = 0.0,
            max_value = 1.0,
            format = "%.1f",
            power = 1

        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("{:.3f}".format(var_vSlider_float[3], 3))
        imgui.pop_style_color(2)

        imgui.same_line()

        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, 0, 0, 1)
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, 0, 0, 1, 0.2)
        _, var_vSlider_float[4] = imgui.v_slider_float(
            label = "##Vertical slider 6",
            width = 20,
            height = 150,
            value = var_vSlider_float[4],
            min_value = 0.0,
            max_value = 1.0,
            format = "%.1f",
            power = 1

        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("{:.3f}".format(var_vSlider_float[4], 3))
        imgui.pop_style_color(2)

        imgui.same_line()

        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, 0.5, 0, 1)
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, 0.5, 0, 1, 0.2)
        _, var_vSlider_float[5] = imgui.v_slider_float(
            "##Vertical slider 7",
            width = 20,
            height = 150,
            value = var_vSlider_float[5],
            min_value = 0.0,
            max_value = 1.0,
            format = "%.1f",
            power = 1

        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("{:.3f}".format(var_vSlider_float[5], 3))
        imgui.pop_style_color(2)

        imgui.same_line()

        imgui.push_style_color(imgui.COLOR_SLIDER_GRAB, 1, 0, 1)
        imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND, 1, 0, 1, 0.2)
        _, var_vSlider_float[6] = imgui.v_slider_float(
            "##Vertical slider 8",
            width = 20,
            height = 150,
            value = var_vSlider_float[6],
            min_value = 0.0,
            max_value = 1.0,
            format = "%.1f",
            power = 1

        )
        if imgui.is_item_hovered():
            imgui.set_tooltip("{:.3f}".format(var_vSlider_float[6], 3))
        imgui.pop_style_color(2)

        imgui.same_line()

        imgui.begin_group()
        imgui.columns(1, "vertical sliders", border = False)
        for i in range(0, 3):
            for j in range(0, 4):
                _, var_vSlider_float_2[j] = imgui.v_slider_float(
                    "##{}{}".format(str(i), str(j)),
                    width = 20,
                    height = 47,
                    value = var_vSlider_float_2[j],
                    min_value = 0.0,
                    max_value = 1.0,
                    format = "%.1f",
                    power = 1
                )
                if imgui.is_item_hovered():
                    imgui.set_tooltip("{:.3f}".format(var_vSlider_float_2[j], 3))
                if j < 3:
                    imgui.same_line()
            imgui.next_column()
        imgui.columns(1)
        imgui.end_group()

        imgui.same_line()

        imgui.begin_group()
        for i in range(0, 4):
            imgui.push_style_var(imgui.STYLE_GRAB_MIN_SIZE, 40)
            _, var_vSlider_float[i] = imgui.v_slider_float(
                "##Vertical Sliders sec{}".format(str(i)),
                width = 40,
                height = 150,
                value = var_vSlider_float[i],
                min_value = 0.0,
                max_value = 1.0,
                format = "%.2f\n{}".format("sec"),
                power = 1
            )
            imgui.pop_style_var()
            if i < 3:
                imgui.same_line()
        imgui.end_group()

        imgui.tree_pop()

def header_graphWidgets():
    imgui.push_style_color(imgui.COLOR_TEXT, 1, 0, 0)
    imgui.text("Not implemented yet")
    imgui.pop_style_color()

def header_layout():
    global var_ChildRegion_Goto

    global var_WidgetWidth

    global state_layout
    global var_combo_layout_current
    global var_combo_layout_items
    global var_slider_layout

    if imgui.tree_node("Child regions"):
        imgui.begin_child("GotoHeader", width = 200, height = 40)
        imgui.text("Without border")

        imgui.button("Goto") # TODO: implement goto function
        #if imgui.is_item_clicked():
            #goto number

        imgui.same_line()

        _, var_ChildRegion_Goto = imgui.input_int("##GotoButton", var_ChildRegion_Goto)
        imgui.end_child()

        imgui.begin_child("ScrollRegion_WithoutBorder", width = 250, height = 300)
        for i in range(0, 101):
            imgui.text("{:04}: scrollable region".format(i))

        imgui.end_child()
        imgui.same_line()

        imgui.push_style_var(imgui.STYLE_CHILD_ROUNDING, 5)
        imgui.begin_child("ScrollRegion_WithBorder", width = 250, height = 300, border = True)
        imgui.text("With border")
        imgui.columns(2)
        for i in range(0, 101):
            imgui.button("{:08}".format(i), width = 100)
            if i < 100:
                imgui.next_column()
        imgui.end_child()
        imgui.pop_style_var()

        imgui.tree_pop()

    if imgui.tree_node("Widgets Width"):

        imgui.text("push_item_width(100)")
        imgui.same_line()
        imgui.push_style_color(imgui.COLOR_TEXT, 0.7, 0.7, 0.7)
        imgui.text("(?)")
        imgui.pop_style_color()
        if imgui.is_item_hovered():
            imgui.set_tooltip("Fixed width.")
        imgui.push_item_width(100)
        _, var_WidgetWidth = imgui.drag_float("float##1", var_WidgetWidth)
        imgui.pop_item_width()

        imgui.text("push_item_width(get_window_width() * 0.5)")
        imgui.same_line()
        imgui.push_style_color(imgui.COLOR_TEXT, 0.7, 0.7, 0.7)
        imgui.text("(?)")
        imgui.pop_style_color()
        if imgui.is_item_hovered():
            imgui.set_tooltip("Half of window width.")
        imgui.push_item_width(imgui.get_window_width() * 0.5)
        _, var_WidgetWidth = imgui.drag_float("float##2", var_WidgetWidth)
        imgui.pop_item_width()

        imgui.text("push_item_width(get_content_region_available_width() * 0.5)")
        imgui.same_line()
        imgui.push_style_color(imgui.COLOR_TEXT, 0.7, 0.7, 0.7)
        imgui.text("(?)")
        imgui.pop_style_color()
        if imgui.is_item_hovered():
            imgui.set_tooltip("Half of available width.\n"
                              "(~ right-cursor_pos)\n"
                              "(works within a column set)")
        imgui.push_item_width(imgui.get_content_region_available_width() * 0.5)
        _, var_WidgetWidth = imgui.drag_float("float##3", var_WidgetWidth)
        imgui.pop_item_width()

        imgui.text("push_item_width(-100)")
        imgui.same_line()
        imgui.push_style_color(imgui.COLOR_TEXT, 0.7, 0.7, 0.7)
        imgui.text("(?)")
        imgui.pop_style_color()
        if imgui.is_item_hovered():
            imgui.set_tooltip("Align to right edge minus 100.")
        imgui.push_item_width(-100)
        _, var_WidgetWidth = imgui.drag_float("float##4", var_WidgetWidth)
        imgui.pop_item_width()

        imgui.text("push_item_width(-1)")
        imgui.same_line()
        imgui.push_style_color(imgui.COLOR_TEXT, 0.7, 0.7, 0.7)
        imgui.text("(?)")
        imgui.pop_style_color()
        if imgui.is_item_hovered():
            imgui.set_tooltip("Align to right edge.")
        imgui.push_item_width(-1)
        _, var_WidgetWidth = imgui.drag_float("float##5", var_WidgetWidth)
        imgui.pop_item_width()

        imgui.tree_pop()

    if imgui.tree_node("Basic Horizontal Layout"):
        imgui.text("(Use imgui.sameline() to keep adding items to the right if the preceeding item)")

        imgui.text("Two items: Hello")
        imgui.same_line()
        imgui.push_style_color(imgui.COLOR_TEXT, 1, 1, 0)
        imgui.text("Sailor")
        imgui.pop_style_color()

        imgui.text("More spacing: Hello")
        imgui.same_line(spacing = 20)
        imgui.push_style_color(imgui.COLOR_TEXT, 1, 1, 0)
        imgui.text("Sailor")
        imgui.pop_style_color()


        imgui.text("Normal buttons")
        imgui.same_line()
        imgui.button("Banana")
        imgui.same_line()
        imgui.button("Apple")
        imgui.same_line()
        imgui.button("Corniflower")

        imgui.text("Small buttons")
        imgui.same_line()
        imgui.small_button("Like this one")
        imgui.same_line()
        imgui.text("can fit within a text block.")

        imgui.text("Aligned")
        imgui.same_line(spacing = 150)
        imgui.text("x=150")
        imgui.same_line(spacing = 150)
        imgui.text("x=300")

        imgui.text("Aligned")
        imgui.same_line(spacing = 150)
        imgui.small_button("x=150")
        imgui.same_line(spacing = 150)
        imgui.small_button("x=300")

        _, state_layout[0] = imgui.checkbox("My", state_layout[0])
        imgui.same_line()
        _, state_layout[1] = imgui.checkbox("Tailor", state_layout[1])
        imgui.same_line()
        _, state_layout[2] = imgui.checkbox("Is", state_layout[2])
        imgui.same_line()
        _, state_layout[3] = imgui.checkbox("Rich", state_layout[3])

        imgui.push_item_width(70)
        _, var_combo_layout_current = imgui.combo(
            "Combo",
            var_combo_layout_current,
            var_combo_layout_items
        )
        imgui.same_line(position = 150)
        _, var_slider_layout[0] = imgui.slider_float(
            "X",
            var_slider_layout[0],
            min_value = 0,
            max_value = 5
        )
        imgui.same_line(position = 240)
        _, var_slider_layout[1] = imgui.slider_float(
            "Y",
            var_slider_layout[1],
            min_value = 0,
            max_value = 5
        )
        imgui.same_line(position = 330)
        _, var_slider_layout[2] = imgui.slider_float(
            "Z",
            var_slider_layout[2],
            min_value = 0,
            max_value = 5
        )

        imgui.tree_pop()

def header_popupsModalWin():
    imgui.text("Popups & Modal windows")

def header_columns():
    imgui.text("Columns")

def header_filtering():
    imgui.text("Filtering")

def header_keyMouseFocus():
    imgui.text("Keyboard, Mouse & Focus")


if __name__ == "__main__":
    main()
