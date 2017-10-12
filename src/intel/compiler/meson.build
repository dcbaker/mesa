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

brw_nir_trig = custom_target(
  'brw_nir_trig_workarounds.c',
  input : 'brw_nir_trig_workarounds.py',
  output : 'brw_nir_trig_workarounds.c',
  command : [prog_python2, '@INPUT@', '-p',
             join_paths(meson.source_root(), 'src/compiler/nir/')],
  depend_files : files('../../compiler/nir/nir_algebraic.py'),
  capture : true,
)

libintel_compiler = static_library(
  'intel_compiler',
  [files_intel.get('COMPILER_FILES'), brw_nir_trig, nir_opcodes_h,
   nir_builder_opcodes_h, ir_expression_operation_h],
  include_directories : [inc_common, inc_intel, inc_nir],
  c_args : [c_vis_args, no_override_init_args],
  cpp_args : [cpp_vis_args],
  build_by_default : false,
)

if with_tests
  # The last two tests are not C++ or gtest, pre comment in autotools make
  foreach t : ['fs_cmod_propagation', 'fs_copy_propagation',
               'fs_saturate_propagation', 'vf_float_conversions',
               'vec4_register_coalesce', 'vec4_copy_propagation',
               'vec4_cmod_propagation', 'eu_compact', 'eu_validate']
    _exe = executable(
      [t, nir_opcodes_h, ir_expression_operation_h],
      'test_@0@.cpp'.format(t),
      include_directories : [inc_common, inc_intel],
      link_with : [libintel_compiler, libintel_common, libnir, libmesa_util,
                   libisl],
      dependencies : [dep_thread, dep_dl, idep_gtest],
    )
    test(t, _exe)
  endforeach
endif
