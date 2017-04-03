# Copyright © 2017 Intel Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

inc_common = include_directories(
  '.',
  'mesa',
  'gallium/auxiliary',
  'gallium/include',
  'mapi',
  '../include',
)

files_wl_xml = files('egl/wayland/wayland-drm/wayland-drm.xml')

subdir('util')
# TODO: HAVE_OPENGL
# TODO: HAVE_GLX
# TODO: HAVE_COMMON_OSMESA
subdir('compiler')
if opt_wsi_wayland
  subdir('egl/wayland/wayland-egl')
endif
if opt_vk
  subdir('vulkan')
endif
if opt_vk_intel  # TODO: or i965 (i915?)
  subdir('intel')
endif
# TODO: if shared_glapi
subdir('mapi')
subdir('loader')
if opt_wsi_x11 and opt_gl
  subdir('glx')
endif
