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

static_glapi_mapi_tmp_h = custom_target(
  'static_glapi_mapi_tmp.h',
  input : mapi_abi_gen_files,
  output : 'glapi_mapi_tmp.h',
  command : [prog_python, '@INPUT0@', '--mode', 'lib',
             '--printer', 'glapi', '@INPUT1@'],
  capture : true,
  build_by_default : false,
)

files_glapi_static = []

# TODO: assembly

# TODO: apple and windows dri

if opt_shared_glapi
  args_c_glapi_static = [
    '-DMAPI_MODE_BRIDGE',
    '-DMAPI_ABI_HEADER="glapi/glapi_mapi_tmp.h"',
  ]
  files_glapi_static += files_mapi_bridge
  files_glapi_static += static_glapi_mapi_tmp_h
else
  # TODO
endif

# TODO: SELINUX
libglapi_static = static_library(
  'glapi',
  files_glapi_static,
  include_directories : inc_common,
  c_args : [args_c_glapi_static, args_c_msvc_compat],
)
