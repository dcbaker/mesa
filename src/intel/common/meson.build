intel_common_sources = [
  'gen_debug.c',
  'gen_debug.h',
  'gen_device_info.c',
  'gen_device_info.h',
  'gen_l3_config.c',
  'gen_l3_config.h',
  'gen_urb_config.c',
  'gen_sample_positions.h',
]

libintel_common = static_library(
  'intel_common',
  intel_common_sources,
  include_directories : [basic_includes, include_directories('..')],
)
