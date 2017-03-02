vk_enum_to_str = custom_target(
  'vk_enum_to_str',
  input : 'gen_enum_to_str.py',
  output : ['vk_enum_to_str.c', 'vk_enum_to_str.h'],
  command : [python, '@INPUT@', '--xml', vk_xml[0], '--outdir', '@OUTDIR@'],
)

libvulkanutil = static_library(
  'vulkanutil',
  vk_enum_to_str,
  include_directories : basic_includes
)
