subdir('util')
subdir('mesa')
subdir('egl')
subdir('vulkan')

libglsl_util_sources = [
  'mesa/main/extensions_table.c',
  'mesa/main/imports.c',
  'mesa/program/prog_parameter.c',
  'mesa/program/symbol_table.c',
  'mesa/program/dummy_errors.c',
]

libglsl_util = static_library(
  'glsl_util',
  libglsl_util_sources,
  include_directories : [basic_includes, include_directories('mapi')],
)

subdir('compiler')
subdir('intel')
