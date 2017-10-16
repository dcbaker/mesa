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

# TODO: main/tests
# TODO: xlib_glx
# TODO: osmesa
# TODO: asm_offsets

files_mesa = mp.load('Makefile.sources')

subdir('program')
subdir('main')

# TODO: sse41
libmesa_sse41 = []

matypes_h = []
if with_asm_arch == 'x86' or with_asm_arch == 'x86_64'
  gen_matypes = executable(
    'gen_matypes',
    'x86/gen_matypes.c',
    c_args : [c_vis_args, c_msvc_compat_args],
    include_directories : inc_common,
  )
  matypes_h = custom_target(
    'matypes.h',
    output : 'matypes.h',
    command : [gen_matypes],
    capture : true,
  )
endif

if with_asm_arch == 'x86'
  files_libmesa_arch = files_mesa.get('X86_FILES')
elif with_asm_arch == 'x86_64'
  files_libmesa_arch = files_mesa.get('X86_64_FILES')
endif
# TODO: sparc

format_fallback_c = custom_target(
  'format_fallback.c',
  input : ['main/format_fallback.py', 'main/formats.csv'],
  output : 'format_fallback.c',
  command : [prog_python2, '@INPUT0@', '@INPUT1@', '@OUTPUT@'],
  depend_files : files('main/format_parser.py'),
)

get_hash_h = custom_target(
  'get_hash.h',
  input : ['main/get_hash_generator.py', gl_and_es_api_files],
  output : 'get_hash.h',
  command : [prog_python2, '@INPUT0@', '-f', '@INPUT1@'],
  depend_files : files('main/get_hash_params.py'),
  capture : true,
)

files_libmesa_generated = [
  mesa_lex,
  program_parse_tab,
  main_api_exec_c,
  main_enums_c,
  format_fallback_c,
  get_hash_h,
  main_marshal_generated_c,
  main_marshal_generated_h,
  main_dispatch_h,
  ir_expression_operation_h,
  nir_opcodes_h,
  main_remap_helper_h,
  matypes_h,
  sha1_h,
]

foreach x : [['format_info.h', 'format_info.py'],
             ['format_pack.c', 'format_pack.py'],
             ['format_unpack.c', 'format_unpack.py']]
  files_libmesa_generated += custom_target(
    x[0],
    input : ['main/@0@'.format(x[1]), 'main/formats.csv'],
    output : x[0],
    command : [prog_python2, '@INPUT0@', '@INPUT1@'],
    depend_files : files('main/format_parser.py'),
    capture : true,
  )
endforeach

libmesa_classic = static_library(
  'mesa_classic',
  [files_mesa.get('MESA_FILES', 'PROGRAM_FILES', 'PROGRAM_NIR_FILES'),
   files_libmesa_generated, files_libmesa_arch],
  c_args : [c_vis_args, c_msvc_compat_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  include_directories : [inc_common, include_directories('main')],
  link_with : [libglsl, libmesa_sse41],
  build_by_default : false,
)

libmesa_gallium = static_library(
  'mesa_gallium',
  [files_mesa.get('MESA_GALLIUM_FILES', 'PROGRAM_FILES', 'PROGRAM_NIR_FILES'),
   files_libmesa_generated, files_libmesa_arch],
  c_args : [c_vis_args, c_msvc_compat_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  include_directories : [inc_common, include_directories('main')],
  link_with : [libglsl, libmesa_sse41],
  build_by_default : false,
)

subdir('drivers/dri')
