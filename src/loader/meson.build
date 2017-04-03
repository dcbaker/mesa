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

files_lib_loader = files(
  'loader.c',
  'loader.h',
  'pci_id_driver_map.c',
  'pci_id_driver_map.h',
)

# TODO: have_dricommon

libloader = static_library(
  'loader',
  files_lib_loader,
  include_directories : inc_common,
  c_args : args_c_visibility,
  dependencies : [dep_libdrm, dep_xcb_dri3],
  build_by_default : false,
)

# TODO: only if have dri3

libloader_dri3_helper = static_library(
  'loader_dri3_helper',
  ['loader_dri3_helper.c', 'loader_dri3_helper.h'],
  include_directories : inc_common,
  dependencies : [dep_libdrm, dep_xcb_dri3],
  build_by_default : false,
)
