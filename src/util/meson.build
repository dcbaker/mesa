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

files_libmesautil = [
  'bitscan.c',
  'bitscan.h',
  'bitset.h',
  'build_id.c',
  'build_id.h',
  'crc32.c',
  'crc32.h',
  'debug.c',
  'debug.h',
  'disk_cache.c',
  'disk_cache.h',
  'format_r11g11b10f.h',
  'format_rgb9e5.h',
  'format_srgb.h',
  'half_float.c',
  'half_float.h',
  'hash_table.c',
  'hash_table.h',
  'list.h',
  'macros.h',
  'mesa-sha1.c',
  'mesa-sha1.h',
  'sha1/sha1.c',
  'sha1/sha1.h',
  'ralloc.c',
  'ralloc.h',
  'rand_xor.c',
  'rand_xor.h',
  'register_allocate.c',
  'register_allocate.h',
  'rgtc.c',
  'rgtc.h',
  'rounding.h',
  'set.c',
  'set.h',
  'simple_list.h',
  'slab.c',
  'slab.h',
  'string_to_uint_map.cpp',
  'string_to_uint_map.h',
  'strndup.h',
  'strtod.c',
  'strtod.h',
  'texcompress_rgtc_tmp.h',
  'u_atomic.h',
  'u_endian.h',
  'u_queue.c',
  'u_queue.h',
  'u_string.h',
  'u_thread.h',
  'u_vector.c',
  'u_vector.h',
  'vk_alloc.h',
  'vk_util.h',
]

ct_format_srgb = custom_target(
  'format_srgb',
  input : 'format_srgb.py',
  output : '@BASENAME@.c',
  command : [prog_python, '@INPUT@'],
  capture : true,
)

inc_util = include_directories('.')

libmesautil = static_library(
  'mesautil',
  [files_libmesautil, ct_format_srgb],
  include_directories : inc_common,
  c_args : [args_c_visibility, args_c_msvc_compat],
  dependencies : dep_zlib,
)

# TODO: tests
