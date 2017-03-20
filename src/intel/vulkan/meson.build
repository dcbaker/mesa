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

anv_entrypoints = custom_target(
  'anv_entrypoints',
  input : ['anv_entrypoints_gen.py', files_vk_api[0]],
  output : ['anv_entrypoints.c', 'anv_entrypoints.h'],
  command : [prog_python, '@INPUT0@', '--xml', '@INPUT1@',
             '--outdir', meson.current_build_dir()],
)

# TODO: check this?
flags_anv = ['-msse2']

files_anv_genx = [
  'genX_blorp_exec.c',
  'genX_cmd_buffer.c',
  'genX_gpu_memcpy.c',
  'genX_pipeline.c',
  'genX_query.c',
  'genX_state.c',
  anv_entrypoints,
]

libanv_gen7 = static_library(
  'anv_gen7',
  [files_anv_genx, gen7_pack_h, 'gen7_cmd_buffer.c'],
  c_args : [flags_anv, '-DGEN_VERSIONx10=70'],
  include_directories : [inc_common, inc_intel, inc_vulkan_wsi, inc_nir],
  dependencies : [dep_libdrm, dep_valgrind],
)

libanv_gen75 = static_library(
  'anv_gen75',
  [files_anv_genx, gen75_pack_h, 'gen7_cmd_buffer.c'],
  c_args : [flags_anv, '-DGEN_VERSIONx10=75'],
  include_directories : [inc_common, inc_intel, inc_vulkan_wsi, inc_nir],
  dependencies : [dep_libdrm, dep_valgrind],
)

libanv_gen8 = static_library(
  'anv_gen8',
  [files_anv_genx, gen8_pack_h, 'gen8_cmd_buffer.c'],
  c_args : [flags_anv, '-DGEN_VERSIONx10=80'],
  include_directories : [inc_common, inc_intel, inc_vulkan_wsi, inc_nir],
  dependencies : [dep_libdrm, dep_valgrind],
)

libanv_gen9 = static_library(
  'anv_gen9',
  [files_anv_genx, gen8_pack_h, 'gen8_cmd_buffer.c'],
  c_args : [flags_anv, '-DGEN_VERSIONx10=90'],
  include_directories : [inc_common, inc_intel, inc_vulkan_wsi, inc_nir],
  dependencies : [dep_libdrm, dep_valgrind],
)

files_anv = [
  anv_entrypoints,
  nir_opcodes_h,
  'anv_allocator.c',
  'anv_batch_chain.c',
  'anv_blorp.c',
  'anv_cmd_buffer.c',
  'anv_descriptor_set.c',
  'anv_device.c',
  'anv_dump.c',
  'anv_formats.c',
  'anv_genX.h',
  'anv_image.c',
  'anv_intel.c',
  'anv_nir.h',
  'anv_nir_apply_pipeline_layout.c',
  'anv_nir_lower_input_attachments.c',
  'anv_nir_lower_push_constants.c',
  'anv_pass.c',
  'anv_pipeline.c',
  'anv_pipeline_cache.c',
  'anv_private.h',
  'anv_util.c',
  'anv_wsi.c',
  'vk_format_info.h',
  'anv_gem.c',
]

dep_anv = []
if opt_wsi_wayland
  files_anv += 'anv_wsi_wayland.c'
endif
if opt_wsi_x11
  files_anv += 'anv_wsi_x11.c'
  dep_anv += [dep_xshmfence, dep_xcb_present, dep_xcb_sync]
endif

# TODO: make nir a dependecy
# TODO: make vulkan util a dependency

libintel_vulkan = shared_library(
  'intel_vulkan',
  [files_anv, vk_enum_to_str],
  include_directories : [inc_common, inc_intel, inc_compiler, inc_nir],
  link_with : [libanv_gen7, libanv_gen75, libanv_gen8, libanv_gen9,
               libintel_compiler, libintel_common, libblorp, libvulkanutil,
               libnir, libmesautil],
  dependencies : [dep_libdrm, dep_math, dep_valgrind, dep_vk_wsi, dep_isl,
                  dep_thread, dep_dl, dep_anv],
  install : true,
)
# TODO: linker flags

# TODO: move this to top
prog_sed = find_program('sed')

# XXX: the DEV ICD doesn't make sense for meson, since it doesn't put things in /bin and /lib
# TODO: make ICD dir configurable
anv_conf = configuration_data()
anv_conf.set('install_libdir', join_paths(get_option('prefix'), get_option('libdir')))
configure_file(
  input : 'intel_icd.json.in',
  output : 'intel_icd.@0@.json'.format(host_machine.cpu_family()),
  configuration : anv_conf,
  install_dir : join_paths(get_option('datadir'), 'vulkan/icd.d'),
)
