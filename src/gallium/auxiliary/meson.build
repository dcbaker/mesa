# Copyright © 2017 Dylan Baker

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

inc_gallium_aux = include_directories('.')
files_gallium_aux = mp.load('Makefile.sources')
files_libgallium = files_gallium_aux.get('C_SOURCES')

if dep_libdrm != [] and dep_libdrm.found()
  files_libgallium += files_gallium_aux.get('RENDERONLY_SOURCES')
endif

if with_llvm
  files_libgallium += files_gallium_aux.get('GALLIVM_SOURCES')
endif

files_libgalliumvl = files(
  'vl/vl_bicubic_filter.c',
  'vl/vl_bicubic_filter.h',
  'vl/vl_compositor.c',
  'vl/vl_compositor.h',
  'vl/vl_csc.c',
  'vl/vl_csc.h',
  'vl/vl_decoder.c',
  'vl/vl_decoder.h',
  'vl/vl_defines.h',
  'vl/vl_deint_filter.c',
  'vl/vl_deint_filter.h',
  'vl/vl_idct.c',
  'vl/vl_idct.h',
  'vl/vl_matrix_filter.c',
  'vl/vl_matrix_filter.h',
  'vl/vl_mc.c',
  'vl/vl_mc.h',
  'vl/vl_median_filter.c',
  'vl/vl_median_filter.h',
  'vl/vl_mpeg12_bitstream.c',
  'vl/vl_mpeg12_bitstream.h',
  'vl/vl_mpeg12_decoder.c',
  'vl/vl_mpeg12_decoder.h',
  'vl/vl_rbsp.h',
  'vl/vl_types.h',
  'vl/vl_vertex_buffers.c',
  'vl/vl_vertex_buffers.h',
  'vl/vl_video_buffer.c',
  'vl/vl_video_buffer.h',
  'vl/vl_vlc.h',
  'vl/vl_zscan.c',
  'vl/vl_zscan.h',
)

files_libgalliumvlwinsys = files_gallium_aux.get('VL_WINSYS_SOURCES')
if with_dri2
  files_libgalliumvlwinsys += files_gallium_aux.get('VL_WINSYS_DRI2_SOURCES')
  if with_dri3
    files_libgalliumvlwinsys += files_gallium_aux.get('VL_WINSYS_DRI3_SOURCES')
  endif
endif
if with_platform_drm
  files_libgalliumvlwinsys += files_gallium_aux.get('VL_WINSYS_DRM_SOURCES')
endif

u_indices_gen_c = custom_target(
  'u_indices_gen.c',
  input : 'indices/u_indices_gen.py',
  output : 'u_indices_gen.c',
  command : [prog_python2, '@INPUT@'],
  capture : true,
)

u_unfilled_gen_c = custom_target(
  'u_unfilled_gen.c',
  input : 'indices/u_unfilled_gen.py',
  output : 'u_unfilled_gen.c',
  command : [prog_python2, '@INPUT@'],
  capture : true,
)

u_format_table_c = custom_target(
  'u_format_table.c',
  input : ['util/u_format_table.py', 'util/u_format.csv'],
  output : 'u_format_table.c',
  command : [prog_python2, '@INPUT@'],
  depend_files : files('util/u_format_pack.py', 'util/u_format_parse.py'),
  capture : true,
)

libgallium = static_library(
  'gallium',
  [files_libgallium, u_indices_gen_c, u_unfilled_gen_c, u_format_table_c,
   nir_opcodes_h],
  include_directories : [
    inc_loader, inc_gallium, inc_src, inc_include, include_directories('util')
  ],
  c_args : [c_vis_args, c_msvc_compat_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  dependencies : [dep_libdrm, dep_llvm, dep_unwind, dep_dl],
  build_by_default : false,
)

libgalliumvl_stub = static_library(
  'galliumvl_stub',
  files_gallium_aux.get('VL_STUB_SOURCES'),
  c_args : [c_vis_args, c_msvc_compat_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  include_directories: [inc_gallium, inc_include, inc_src],
  build_by_default : false,
)

libgalliumvl = static_library(
  'galliumvl',
  files_gallium_aux.get('VL_SOURCES'),
  c_args : [c_vis_args, c_msvc_compat_args],
  cpp_args : [cpp_vis_args, cpp_msvc_compat_args],
  include_directories : [inc_gallium, inc_include, inc_src],
  build_by_default : false,
)

# XXX: The dependencies here may be off...
libgalliumvlwinsys = static_library(
  'galliumvlwinsys',
  files_libgalliumvlwinsys,
  include_directories : [inc_gallium, inc_include, inc_loader, inc_src],
  dependencies : [dep_libdrm],
  build_by_default : false,
)
