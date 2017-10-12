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

nir_depends = files('nir_opcodes.py')

nir_builder_opcodes_h = custom_target(
  'nir_builder_opcodes.h',
  input : 'nir_builder_opcodes_h.py',
  output : 'nir_builder_opcodes.h',
  command : [prog_python2, '@INPUT@'],
  capture : true,
  depend_files : nir_depends,
)

nir_constant_expressions_c = custom_target(
  'nir_constant_expressions.c',
  input : 'nir_constant_expressions.py',
  output : 'nir_constant_expressions.c',
  command : [prog_python2, '@INPUT@'],
  capture : true,
  depend_files : nir_depends,
)

nir_opcodes_h = custom_target(
  'nir_opcodes.h',
  input : 'nir_opcodes_h.py',
  output : 'nir_opcodes.h',
  command : [prog_python2, '@INPUT@'],
  capture : true,
  depend_files : nir_depends,
)

nir_opcodes_c = custom_target(
  'nir_opcodes.c',
  input : 'nir_opcodes_c.py',
  output : 'nir_opcodes.c',
  command : [prog_python2, '@INPUT@'],
  capture : true,
  depend_files : nir_depends,
)

nir_opt_algebraic_c = custom_target(
  'nir_opt_algebraic.c',
  input : 'nir_opt_algebraic.py',
  output : 'nir_opt_algebraic.c',
  command : [prog_python2, '@INPUT@'],
  capture : true,
  depend_files : files('nir_algebraic.py'),
)

spirv_info_c = custom_target(
  'spirv_info.c',
  input : files('../spirv/spirv_info_c.py', '../spirv/spirv.core.grammar.json'),
  output : 'spirv_info.c',
  command : [prog_python2, '@INPUT0@', '@INPUT1@', '@OUTPUT@'],
)

libnir = static_library(
  'nir',
  [files_compiler.get('NIR_FILES', 'SPIRV_FILES'), spirv_info_c,
   nir_opt_algebraic_c, nir_opcodes_c, nir_opcodes_h,
   nir_constant_expressions_c, nir_builder_opcodes_h],
  include_directories : [inc_common, inc_compiler, include_directories('../spirv')],
  c_args : [c_vis_args, c_msvc_compat_args, no_override_init_args],
  link_with : libcompiler,
  build_by_default : false,
)

if with_tests
  nir_control_flow_test = executable(
    'nir_control_flow_test',
    [files('tests/control_flow_tests.cpp'), nir_opcodes_h],
    c_args : [c_vis_args, c_msvc_compat_args, no_override_init_args],
    include_directories : [inc_common],
    dependencies : [dep_thread, idep_gtest],
    link_with : [libmesa_util, libnir],
  )

  test('nir_control_flow', nir_control_flow_test)
endif
