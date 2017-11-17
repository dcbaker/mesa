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

hsp_cpp_args = []
hsp_deps = []
hsp_links = []

if with_llvm
  hsp_deps += dep_llvm
  hsp_cpp_args += '-DGALLIUM_LLVMPIPE'
  hsp_links += libllvmpipe
endif
# TODO: SWR

libswpipe = shared_library(
  'swpipe',
  files('GalliumContext.cpp', 'SoftwareRenderer.cpp'),
  cpp_args : [
    '-DGALLIUM_SOFTPIPE', '-DGALLIUM_RBUG', '-DGALLIUM_TRACE',
    hsp_cpp_args, cpp_vis_args,
  ],
  include_directories : [
    inc_src, inc_include, inc_mapi, inc_mesa, inc_mesa_main, inc_haikugl,
    inc_gallium, inc_gallium_aux, inc_gallium_winsys, inc_gallium_drivers,
    include_directories(
      '../../state_trackers/hgl', '/boot/system/develop/headers/private',
    ),
  ],
  link_with : [
    libGL, libswhgl, libhgl, librbug, libtrace, libgallium, libmesa_gallium,
    libsoftpipe, hsp_links,
  ],
  dependencies : [hsp_deps, cpp.find_library('network'), dep_unwind],
  install : true,
)
