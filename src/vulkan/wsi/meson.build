vk_wsi = [
  'wsi_common.h',
  'wsi_common_queue.h',
]

vk_args = []

if get_option('wsi_wayland')
  vk_wsi_wl = [
    'wsi_common_wayland.c',
    'wsi_common_wayland.h',
    wl_drm_client_protocol,
  ]
  vk_args += '-DVK_USE_PLATFORM_WAYLAND_KHR'
else
  vk_wsi_wl = []
endif

if get_option('wsi_x11')
  vk_wsi_x11 = [
    'wsi_common_x11.c',
    'wsi_common_x11.h',
  ]
  vk_args += '-DVK_USE_PLATFORM_XCB_KHR'
  vk_args += '-DVK_USE_PLATFORM_XLIB_KHR'
else
  vk_wsi_x11 = []
endif

libvulkan_wsi = static_library(
  'vulkan_wsi',
  [vk_wsi, vk_wsi_wl, vk_wsi_x11],
  include_directories : [basic_includes, include_directories('../../egl/wayland/wayland-drm')],
  dependencies : [wl_client, wl_server, x11_xcb, x11_xcb_dri3, drm],
  c_args : vk_args,
)
