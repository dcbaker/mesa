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

# TODO: tests

libisl_gen4 = static_library(
  'isl_gen4',
  ['isl_gen4.c', 'isl_gen4.h', 'isl_surface_state.c', gen4_pack_h],
  c_args : [args_c_intel, args_c_visibility, '-DGEN_VERSIONx10=40'],
  include_directories : [inc_common, inc_intel],
)

libisl_gen5 = static_library(
  'isl_gen5',
  ['isl_surface_state.c', gen5_pack_h],
  c_args : [args_c_intel, args_c_visibility, '-DGEN_VERSIONx10=50'],
  include_directories : [inc_common, inc_intel],
)

libisl_gen6 = static_library(
  'isl_gen6',
  ['isl_gen6.c', 'isl_gen6.h', 'isl_surface_state.c', gen6_pack_h],
  c_args : [args_c_intel, args_c_visibility, '-DGEN_VERSIONx10=60'],
  include_directories : [inc_common, inc_intel],
)

libisl_gen7 = static_library(
  'isl_gen7',
  ['isl_gen7.c', 'isl_gen7.h', 'isl_surface_state.c', gen7_pack_h],
  c_args : [args_c_intel, args_c_visibility, '-DGEN_VERSIONx10=70'],
  include_directories : [inc_common, inc_intel],
)

libisl_gen75 = static_library(
  'isl_gen75',
  ['isl_surface_state.c', gen75_pack_h],
  c_args : [args_c_intel, args_c_visibility, '-DGEN_VERSIONx10=75'],
  include_directories : [inc_common, inc_intel],
)

libisl_gen8 = static_library(
  'isl_gen8',
  ['isl_gen8.c', 'isl_gen8.h', 'isl_surface_state.c', gen8_pack_h],
  c_args : [args_c_intel, args_c_visibility, '-DGEN_VERSIONx10=80'],
  include_directories : [inc_common, inc_intel],
)

libisl_gen9 = static_library(
  'isl_gen9',
  ['isl_gen9.c', 'isl_gen9.h', 'isl_surface_state.c', gen9_pack_h],
  c_args : [args_c_intel, args_c_visibility, '-DGEN_VERSIONx10=90'],
  include_directories : [inc_common, inc_intel],
)

isl_format_layout_c = custom_target(
  'isl_format_layout.c',
  input : ['gen_format_layout.py', 'isl_format_layout.csv'],
  output : 'isl_format_layout.c',
  command : [prog_python, '@INPUT0@', '--csv', '@INPUT1@', '--out', '@OUTPUT@'],
)

files_libisl = [
  isl_format_layout_c,
  genX_bits_h,
  'isl.c',
  'isl.h',
  'isl_format.c',
  'isl_priv.h',
  'isl_storage_image.c',
]

libisl_common = static_library(
  'isl_common',
  files_libisl,
  c_args : [args_c_intel, args_c_visibility],
  include_directories : [inc_common, inc_intel],
)

dep_isl = declare_dependency(
  link_with : [libisl_common, libisl_gen4, libisl_gen5, libisl_gen6,
               libisl_gen7, libisl_gen75, libisl_gen8, libisl_gen9],
)
