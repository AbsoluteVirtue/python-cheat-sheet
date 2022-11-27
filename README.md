# Pyimgui user-friendly
* Copyright: 2018 LuminousLizard
* License: BSD-3

## Description:
This project provides examples to learn ["Pyimgui" (GitHub)](https://github.com/swistakm/pyimgui/),
a python binding maintained by Michał Jaworski for the ["dear imgui" (GitHub)](https://github.com/ocornut/imgui/) C++ GUI library maintained by ocornut.
All py-files are standalone executable and contains many comments.

For additional information you can use the [official documentation](https://pyimgui.readthedocs.io/en/latest/reference/imgui.core.html) of Pyimgui.

## Requiremens:

* Python 3
* Pyimgui 1.1.0

## Install pyimgui
Pyimgui currently supports 5 different graphic backends. The examples are currently written for the "pygame" and the "glfw3" backend.

* To use the examples you can use following commands to install "pyimgui" and "glfw3"...
```
pip install imgui[glfw]
```

* or "pyimgui" and "pygame" ...
```
pip install imgui[pygame]
```

* or you install the compatibility to all backends (cocos2d, pysdl2, pygame, glfw3 and pyglet).
```
pip install imgui[full]
```

## Repository content:

* Dir "pyimgui_elements_[glfw3]": Examples for each widget including functions and comments for the glfw3 backend.

* Dir "pyimgui_elements_[pygame]": Examples for each widget including functions and comments for the pygame backend.

* Dir "pyimgui_demo_window": A rewrite of the imgui demo window in Python/Pyimgui (pygame and glfw3 version). WIP !!!

## Help
Any help in the form of comments, improvements or extensions are welcome.
