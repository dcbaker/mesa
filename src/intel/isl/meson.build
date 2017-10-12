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

isl_gen_libs = [
  static_library(
    'libisl_gen75',
    [files_intel.get('ISL_GEN75_FILES'), gen_xml_pack],
    include_directories : [inc_common, inc_intel],
    c_args : [
      c_vis_args, no_override_init_args,
      '-DGEN_VERSIONx10=75'
    ],
    build_by_default : false,
  )
]
foreach _gen : [4, 5, 6, 7, 8, 9, 10]
  _lib = static_library(
    'libisl_gen@0@'.format(_gen),
    [files_intel.get('ISL_GEN@0@_FILES'.format(_gen)), gen_xml_pack],
    include_directories : [inc_common, inc_intel],
    c_args : [
      c_vis_args, no_override_init_args,
      '-DGEN_VERSIONx10=@0@'.format(_gen * 10),
    ],
    build_by_default : false,
  )
  isl_gen_libs += _lib
endforeach

isl_format_layout_c = custom_target(
  'isl_format_layout.c',
  input : ['gen_format_layout.py', 'isl_format_layout.csv'],
  output : 'isl_format_layout.c',
  command : [prog_python2, '@INPUT0@', '--csv', '@INPUT1@', '--out', '@OUTPUT@'],
)

libisl = static_library(
  'isl',
  [files_intel.get('ISL_FILES'), isl_format_layout_c, genX_bits_h],
  include_directories : [inc_common, inc_intel, inc_drm_uapi],
  link_with : isl_gen_libs,
  c_args : [c_vis_args, no_override_init_args],
  build_by_default : false,
)

if with_tests
  isl_surf_get_image_offset_test = executable(
    'isl_surf_get_image_offset_test',
    'tests/isl_surf_get_image_offset_test.c',
    dependencies : dep_m,
    include_directories : [inc_common, inc_intel],
    link_with : [libisl, libintel_common],
    build_by_default : false,
  )

  test('isl_surf_get_image_offset', isl_surf_get_image_offset_test)
endif
