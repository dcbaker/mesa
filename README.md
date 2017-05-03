# Mesa Meson build WIP

Currently nothing is built by default, check meson_options.txt for available options.

to build anvil with x11 and wayland support:

meson build -Dvk_intel=true -Dwsi_x11=true -Dwsi_wayland=true
