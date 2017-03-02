anv_entrypoints_c = custom_target(
  'anv_entrypoints_c',
  input : [vk_xml[0], 'anv_entrypoints_gen.py'],
  output : 'anv_entrypoints.c',
  command : [python, '@INPUT1@', 'code', '@INPUT0@'],
  capture : true,
)

anv_entrypoints_h = custom_target(
  'anv_entrypoints_h',
  input : [vk_xml[0], 'anv_entrypoints_gen.py'],
  output : 'anv_entrypoints.h',
  command : [python, '@INPUT1@', 'header', '@INPUT0@'],
  capture : true,
)

anv_entrypoints_dep = declare_dependency(sources : anv_entrypoints_h)

libanv_genx_sources = [
  'genX_blorp_exec.c',
  'genX_cmd_buffer.c',
  'genX_gpu_memcpy.c',
  'genX_pipeline.c',
  'genX_query.c',
  'genX_state.c',
]

libanv_gen_includes = include_directories(
  '..',
  '../../mesa/drivers/dri/i965',
  '../../mesa/drivers/dri/common',
  '../../vulkan/wsi',
  '../../compiler/nir',
)

libanv_gen7 = static_library(
  'anv_gen7',
  ['gen7_cmd_buffer.c', libanv_genx_sources],
  include_directories : [basic_includes, libanv_gen_includes],
  dependencies : [drm, anv_entrypoints_dep],
  c_args : ['-Wno-override-init', '-msse2', '-DGEN_VERSIONx10=70'],
)

libanv_gen75 = static_library(
  'anv_gen75',
  ['gen7_cmd_buffer.c', libanv_genx_sources],
  include_directories : [basic_includes, libanv_gen_includes],
  dependencies : [drm, anv_entrypoints_dep],
  c_args : ['-Wno-override-init', '-msse2', '-DGEN_VERSIONx10=75'],
)

libanv_gen8 = static_library(
  'anv_gen8',
  ['gen8_cmd_buffer.c', libanv_genx_sources],
  include_directories : [basic_includes, libanv_gen_includes],
  dependencies : [drm, anv_entrypoints_dep],
  c_args : ['-Wno-override-init', '-msse2', '-DGEN_VERSIONx10=80'],
)

libanv_gen9 = static_library(
  'anv_gen9',
  ['gen8_cmd_buffer.c', libanv_genx_sources],
  include_directories : [basic_includes, libanv_gen_includes],
  dependencies : [drm, anv_entrypoints_dep],
  c_args : ['-Wno-override-init', '-msse2', '-DGEN_VERSIONx10=90'],
)

libvulkan_common_sources = [
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
  'anv_nir_apply_dynamic_offsets.c',
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
  anv_entrypoints_c,
  anv_entrypoints_h,
]

libvulkan_common_c_args = []

if get_option('wsi_wayland')
  libvulkan_common_sources += 'anv_wsi_wayland.c'
  libvulkan_common_c_args += '-DVK_USE_PLATFORM_WAYLAND_KHR'
endif

if get_option('wsi_x11')
  libvulkan_common_sources += 'anv_wsi_x11.c'
  libvulkan_common_c_args += ['-DVK_USE_PLATFORM_XCB_KHR', '-DVK_USE_PLATFORM_XLIB_KHR']
endif

libvulkan_intel = shared_module(
  'vulkan_intel',
  libvulkan_common_sources,
  include_directories : [basic_includes, libanv_gen_includes,
                         include_directories('../../compiler', '../../vulkan/util',
                                             '../../egl/wayland/wayland-drm')],
  dependencies : [drm, x11_xcb_dri3, wl_client, wl_server],
  cpp_args : libvulkan_common_c_args,
  c_args : libvulkan_common_c_args,
  link_args : ['-Wno-undef', '-Wno-version', '-Wl,--build-id=sha1'],
  link_with : [libvulkanutil, libvulkan_wsi, libintel_compiler, libnir,
               libmesautil, libintel_common, libisl, libblorp, libanv_gen7,
               libanv_gen75, libanv_gen8, libanv_gen9],
  dependencies : [thread_dep, m_dep, dl_dep, drm],
)
