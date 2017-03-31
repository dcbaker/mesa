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

files_mapi_glapi = files(
  'entry.c',
  'mapi_glapi.c',
  'stub.c',
  'stub.h',
  'table.c',
  'table.h',
)

files_mapi_util = files(
  'u_current.c',
  'u_current.h',
  'u_execmem.c',
  'u_execmem.h',
)

files_mapi_bridge = files(
  'entry.c',
  'entry.h',
  'entry_x86-64_tls.h',
  'entry_x86_tls.h',
  'entry_x86_tsd.h',
  'mapi_tmp.h',
)

mapi_abi_gen_files = files('mapi_abi.py', 'glapi/gen/gl_and_es_API.xml')

if opt_shared_glapi
  subdir('shared-glapi')
endif
if opt_gl_api
  subdir('glapi')
endif

# TODO: GLES1
# TODO: GLES2
