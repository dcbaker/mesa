wl_drm_protocol = custom_target(
  'wl_drm_protocol',
  input : 'wayland-drm.xml',
  output : 'wayland-drm-protocol.h',
  command : [wl_scanner, 'code', '@INPUT@', '@OUTPUT@'],
)

wl_drm_server_protocol = custom_target(
  'wl_drm_server_protocol',
  input : 'wayland-drm.xml',
  output : 'wayland-drm-server-protocol.h',
  command : [wl_scanner, 'server-header', '@INPUT@', '@OUTPUT@'],
)

wl_drm_client_protocol = custom_target(
  'wl_drm_client_protocol',
  input : 'wayland-drm.xml',
  output : 'wayland-drm-client-protocol.h',
  command : [wl_scanner, 'client-header', '@INPUT@', '@OUTPUT@'],
)
