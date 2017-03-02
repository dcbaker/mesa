isl_format_layout = custom_target(
  'isl_format_layout',
  input : ['gen_format_layout.py', 'isl_format_layout.csv'],
  output : 'isl_format_layout.c',
  command : [python, '@INPUT0@', '--csv', '@INPUT1@', '--out', '@OUTPUT@'],
)

libisl_gen4 = static_library(
  'isl_gen4',
  ['isl_gen4.c', 'isl_gen4.h', 'isl_surface_state.c'],
  c_args : '-DGEN_VERSIONx10=40',
  include_directories : [basic_includes, include_directories('..')],
  dependencies : declare_dependency(sources : genxml_gen4_pack),
)

libisl_gen5 = static_library(
  'isl_gen5',
  'isl_surface_state.c',
  c_args : '-DGEN_VERSIONx10=50',
  include_directories : [basic_includes, include_directories('..')],
  dependencies : declare_dependency(sources : genxml_gen5_pack),
)

libisl_gen6 = static_library(
  'isl_gen6',
  ['isl_gen6.c', 'isl_gen6.h', 'isl_surface_state.c'],
  c_args : '-DGEN_VERSIONx10=60',
  include_directories : [basic_includes, include_directories('..')],
  dependencies : declare_dependency(sources : genxml_gen6_pack),
)

libisl_gen7 = static_library(
  'isl_gen7',
  ['isl_gen7.c', 'isl_gen7.h', 'isl_surface_state.c'],
  c_args : '-DGEN_VERSIONx10=70',
  include_directories : [basic_includes, include_directories('..')],
  dependencies : declare_dependency(sources : genxml_gen7_pack),
)

libisl_gen75 = static_library(
  'isl_gen75',
  'isl_surface_state.c',
  c_args : '-DGEN_VERSIONx10=75',
  include_directories : [basic_includes, include_directories('..')],
  dependencies : declare_dependency(sources : genxml_gen75_pack),
)

libisl_gen8 = static_library(
  'isl_gen8',
  ['isl_gen8.c', 'isl_gen8.h', 'isl_surface_state.c'],
  c_args : '-DGEN_VERSIONx10=80',
  include_directories : [basic_includes, include_directories('..')],
  dependencies : declare_dependency(sources : genxml_gen8_pack),
)

libisl_gen9 = static_library(
  'isl_gen9',
  ['isl_gen9.c', 'isl_gen9.h', 'isl_surface_state.c'],
  c_args : '-DGEN_VERSIONx10=90',
  include_directories : [basic_includes, include_directories('..')],
  dependencies : declare_dependency(sources : genxml_gen9_pack),
)

libisl_sources = [
  isl_format_layout,
  'isl.c',
  'isl.h',
  'isl_format.c',
  'isl_priv.h',
  'isl_storage_image.c',
]

libisl = static_library(
  'isl',
  libisl_sources,
  include_directories : [basic_includes, include_directories('..', '../compiler')],
  link_with : [libisl_gen4, libisl_gen5, libisl_gen6, libisl_gen7, libisl_gen75,
               libisl_gen8, libisl_gen9],
  dependencies : genxml_pack
)
