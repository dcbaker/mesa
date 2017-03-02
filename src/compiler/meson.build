ir_exp_op_enum = custom_target(
  'ir_exp_op_enum',
  input : 'glsl/ir_expression_operation.py',
  output : 'ir_expression_operation.h',
  capture : true,
  command : [python, '@INPUT@', 'enum']
)

libcompiler_sources = [
  'builtin_type_macros.h',
  'glsl_types.cpp',
  'glsl_types.h',
  'nir_types.cpp',
  'nir_types.h',
  'shader_enums.c',
  'shader_enums.h',
  'shader_info.h',
  ir_exp_op_enum,
]

libcompiler = static_library(
  'compiler', libcompiler_sources,
  include_directories : [basic_includes, include_directories('../mapi', './glsl')]
)

subdir('nir')
#subdir('glsl')

spirv2nir = executable(
  'spirv2nir',
  'spirv/spirv2nir.c', nir_opcodes_h,
  include_directories : [basic_includes, include_directories('.', 'spirv')],
  link_with : [libnir, libmesautil],
  dependencies : [thread_dep],
)
