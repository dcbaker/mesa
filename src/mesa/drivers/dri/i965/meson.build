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

files_i965 = mp.load('Makefile.sources')

i965_gen_libs = []
foreach v : [4, 5, 6, 7, 8, 9, 10]
  i965_gen_libs += static_library(
    'libi965_gen@0@'.format(v),
    [files_i965.get('i965_gen@0@_FILES'.format(v)), nir_opcodes_h, gen_xml_pack],
    include_directories : [inc_common, inc_intel, inc_dri_common],
    c_args : [c_vis_args, no_override_init_args, '-msse2',
              '-DGEN_VERSIONx10=@0@'.format(v * 10)],
    dependencies : [dep_libdrm],
  )
endforeach
foreach v : [45, 75]
  i965_gen_libs += static_library(
    'libi965_gen@0@'.format(v),
    [files_i965.get('i965_gen@0@_FILES'.format(v)), nir_opcodes_h, gen_xml_pack],
    include_directories : [inc_common, inc_intel, inc_dri_common],
    c_args : [c_vis_args, no_override_init_args, '-msse2',
              '-DGEN_VERSIONx10=@0@'.format(v)],
    dependencies : [dep_libdrm],
  )
endforeach

oa_generator = generator(
  prog_python2,
  arguments : ['@CURRENT_SOURCE_DIR@/brw_oa.py', '@INPUT@',
               '--chipset', '@EXTRA_ARGS@', '--code', '@OUTPUT0@',
               '--header', '@OUTPUT1@'],
  output : ['@BASENAME@.c', '@BASENAME@.h'],
)

i965_oa_sources = []
foreach hw : ['hsw', 'bdw', 'chv', 'sklgt2', 'sklgt3', 'sklgt4', 'bxt',
              'kblgt2', 'kblgt3', 'glk']
  _xml = 'brw_oa_@0@.xml'.format(hw)
  i965_oa_sources += oa_generator.process(_xml, extra_args : hw)
endforeach

libi965 = static_library(
  'i965',
  [files_i965.get('i965_FILES'), i965_oa_sources, nir_opcodes_h,
   ir_expression_operation_h, xmlpool_options_h],
  include_directories : [inc_common, inc_intel, inc_dri_common, inc_util,
                         inc_drm_uapi, inc_nir],
  c_args : [c_vis_args, no_override_init_args, '-msse2'],
  cpp_args : [cpp_vis_args, '-msse2'],
  link_with : [i965_gen_libs, libintel_common, libisl, libintel_compiler,
               libblorp],
  dependencies : [dep_libdrm, dep_valgrind],
)

dri_drivers += libi965
dri_link += 'i965_dri.so'
