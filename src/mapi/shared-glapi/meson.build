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

shared_glapi_mapi_tmp_h = custom_target(
  'shared_glapi_mapi_tmp.h',
  input : mapi_abi_gen_files,
  output : 'glapi_mapi_tmp.h',
  command : [prog_python, '@INPUT0@', '--mode', 'lib',
             '--printer', 'shared-glapi', '@INPUT1@'],
  capture : true,
)

# TODO: SELINUX dependency
libglapi_shared = shared_library(
  'glapi',
  [shared_glapi_mapi_tmp_h, files_mapi_glapi, files_mapi_util],
  include_directories : inc_common, 
  c_args : ['-DMAPI_ABI_HEADER="shared-glapi/glapi_mapi_tmp.h"',
            '-DMAPI_MODE_GLAPI', args_c_visibility,
            args_c_msvc_compat],
  link_args : args_ld_symbolic + args_ld_gc_sections,
  dependencies : [dep_thread],
  install : true,
)

# TODO: tests
