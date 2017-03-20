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

inc_vulkan_wsi = include_directories('.')

files_vk_wsi = [
  'wsi_common.h',
  'wsi_common_queue.h',
]

args_vk_wsi = []
deps_vk_wsi = []

if opt_wsi_wayland
  wayland_drm_protocol = custom_target(
    'wayland-drm-protocol.c',
    input : files_wl_xml[0],
    output : 'wayland-drm-protocol.c',
    command : [prog_wayland_scanner, 'code', '@INPUT@', '@OUTPUT@'],
  )

  wayland_drm_client_protocol = custom_target(
    'wayland-drm-client-protocol.h',
    input : files_wl_xml[0],
    output : 'wayland-drm-client-protocol.h',
    command : [prog_wayland_scanner, 'client-header', '@INPUT@', '@OUTPUT@'],
  )

  files_vk_wsi += [
    'wsi_common_wayland.c',
    'wsi_common_wayland.h',
    wayland_drm_protocol,
    wayland_drm_client_protocol
  ]

  args_vk_wsi += '-DVK_USE_PLATFORM_WAYLAND_KHR'

  deps_vk_wsi += [dep_wayland_client, dep_wayland_server]
endif

if opt_wsi_x11
  files_vk_wsi += [
    'wsi_common_x11.c',
    'wsi_common_x11.h',
  ]

  args_vk_wsi += ['-DVK_USE_PLATFORM_XCB_KHR', '-DVK_USE_PLATFORM_XLIB_KHR']
  deps_vk_wsi += [dep_xcb_dri3, dep_x11_xcb]
endif

libvulkan_wsi = static_library(
  'vulkan_wsi',
  files_vk_wsi,
  include_directories : inc_common,
  c_args : [args_c_visibility, args_vk_wsi],
  dependencies : [deps_vk_wsi, dep_libdrm],
)

dep_vk_wsi = declare_dependency(
  include_directories : inc_vulkan_wsi,
  link_with : libvulkan_wsi,
  compile_args : args_vk_wsi,
  dependencies : deps_vk_wsi,
)
