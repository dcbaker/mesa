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

subdir('glcpp')

glsl_parser = custom_target(
  'glsl_parser',
  input : 'glsl_parser.yy',
  output : ['glsl_parser.cpp', 'glsl_parser.h'],
  command : [prog_bison, '-o', '@OUTPUT0@', '-p', '_mesa_glsl_',
             '--defines=@OUTPUT1@', '@INPUT@'],
)

glsl_lexer_cpp = custom_target(
  'glsl_lexer_cpp',
  input : 'glsl_lexer.ll',
  output : 'glsl_lexer.cpp',
  command : [prog_flex, '-o', '@OUTPUT@', '@INPUT@'],
)

ir_expression_operation_constant_h = custom_target(
  'ir_expression_operation_constant.h',
  input : 'ir_expression_operation.py',
  output : 'ir_expression_operation_constant.h',
  command : [prog_python2, '@INPUT@', 'constant'],
  capture : true,
)

ir_expression_operation_strings_h = custom_target(
  'ir_expression_operation_strings.h',
  input : 'ir_expression_operation.py',
  output : 'ir_expression_operation_strings.h',
  command : [prog_python2, '@INPUT@', 'strings'],
  capture : true,
)

files_libglsl_standalone = files(
  'ir_builder_print_visitor.cpp',
  'ir_builder_print_visitor.h',
  'opt_add_neg_to_sub.h',
  'standalone_scaffolding.cpp',
  'standalone_scaffolding.h',
  'standalone.cpp',
  'standalone.h',
)

libglsl = static_library(
  'glsl',
  [files_compiler.get('LIBGLSL_FILES', 'LIBGLSL_SHADER_CACHE_FILES'),
   glsl_parser, glsl_lexer_cpp, ir_expression_operation_h,
   ir_expression_operation_strings_h, ir_expression_operation_constant_h],
  c_args : [c_vis_args, c_msvc_compat_args, no_override_init_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  link_with : [libnir, libglcpp],
  include_directories : [inc_common, inc_nir],
  dependencies : [dep_valgrind],
  build_by_default : false,
)

libglsl_standalone = static_library(
  'glsl_standalone',
  [files_compiler.get('GLSL_COMPILER_CXX_FILES'), ir_expression_operation_h],
  c_args : [c_vis_args, c_msvc_compat_args, no_override_init_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  include_directories : [inc_common],
  link_with : [libglsl, libglsl_util, libmesa_util],
  dependencies : [dep_thread],
  build_by_default : false,
)

glsl_compiler = executable(
  'glsl_compiler',
  'main.cpp',
  c_args : [c_vis_args, c_msvc_compat_args, no_override_init_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  dependencies : [dep_clock],
  include_directories : [inc_common],
  link_with : [libglsl_standalone],
  build_by_default : false,
)

glsl_test = executable(
  'glsl_test',
  ['test.cpp', 'test_optpass.cpp', 'test_optpass.h',
   ir_expression_operation_h],
  c_args : [c_vis_args, c_msvc_compat_args, no_override_init_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  include_directories : [inc_common],
  dependencies : [dep_clock, dep_thread],
  link_with : [libglsl, libglsl_standalone, libglsl_util],
  build_by_default : false,
)

if with_tests
  subdir('tests')
endif
