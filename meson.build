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

project('mesa', ['c', 'cpp'], version : '17.1-dev', license : 'MIT',
        default_options : ['c_std=gnu99'])

prog_bison = find_program('bison')
prog_flex = find_program('flex')
prog_python = find_program('python2.7', 'python2', 'python')
check_mako = run_command(prog_python, '-c', 'import mako')
if check_mako.returncode() != 0
  error('Mako python module is required.')
endif

# TODO: Set -std=gnu99 for old version of GCC

# TODO: handle asm_offsets

# XXX: no need to check for suncc, meson doesn't support it.

# TODO: handle GCC version requirements

# Set global compiler arguments for C and C++ compilers
args_global = []
args_c_msvc_compat = []
args_cpp_msvc_compat = []
args_c_visibility = []
args_cpp_visibility = []

# Define compiler objects for testing their features
cc = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')

# FUTURE TODO: use a config.h file, which is sooooo much easier and cleaner
# TODO: this might be able to be simplified with a foreach loop...
if cc.has_function('bswap32')
  args_global += '-DHAVE___BUILTIN_BSWAP32'
endif
if cc.has_function('bswap64')
  args_global += '-DHAVE___BUILTIN_BSWAP64'
endif
if cc.has_function('clz')
  args_global += '-DHAVE___BUILTIN_CLZ'
endif
if cc.has_function('clzll')
  args_global += '-DHAVE___BUILTIN_CLZll'
endif
if cc.has_function('ctz')
  args_global += '-DHAVE___BUILTIN_CTZ'
endif
if cc.has_function('expect')
  args_global += '-DHAVE___BUILTIN_EXPECT'
endif
if cc.has_function('ffs')
  args_global += '-DHAVE___BUILTIN_FFS'
endif
if cc.has_function('ffsll')
  args_global += '-DHAVE___BUILTIN_FFSLL'
endif
if cc.has_function('popcount')
  args_global += '-DHAVE___BUILTIN_POPCOUNT'
endif
if cc.has_function('popcountll')
  args_global += '-DHAVE___BUILTIN_POPCOUNTLL'
endif
if cc.has_function('unreachable')
  args_global += '-DHAVE___BUILTIN_UNREACHABLE'
endif
if cc.compiles('''int foo(void) __attribute__((const));''', name : 'attribute const')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_CONST'
endif
if cc.compiles('''int foo(void) __attribute__((flatten));''', name : 'attribute flatten')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_FLATTEN'
endif
if cc.compiles('''int foo(const char * p, ...) __attribute__((format (printf, 1, 2)));''', name : 'attribute format')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_FORMAT'
endif
if cc.compiles('''int foo(void) __attribute__((__malloc__));''', name : 'attribute malloc')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_MALLOC'
endif
if cc.compiles('''int foo(void) __attribute__((__packed__));''', name : 'attribute packed')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_PACKED'
endif
if cc.compiles('''int foo(void) __attribute__((__pure__));''', name : 'attribute pure')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_PURE'
endif
if cc.compiles('''void* foo(void) __attribute__((__returns_nonnull__));''', name : 'attribute returns_nonnull')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_RETURNS_NONNULL'
endif
if cc.compiles('''int foo(void) __attribute__((unused));''', name : 'attribute unused')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_UNUSED'
endif
if cc.compiles('''int foo(void) __attribute__((visibility("hidden")));''', name : 'attribute visibility(("hidden"))')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_VISIBILITY'
endif
if cc.compiles('''int foo(void) __attribute__((warn_unused_result));''', name : 'attribute warn_unused_result')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_WARN_UNUSED_RESULT'
endif
if cc.compiles('''int foo(void) __attribute__((weak));''', name : 'attribute weak')
  args_global += '-DHAVE_FUNC_ATTRIBUTE_WEAK'
endif
# TODO: is alias unused?

# TODO: android?
host_os = host_machine.system()
if (host_os.startswith('linux') or host_os.startswith('cygwin') or 
    host_os.contains('gnu'))
  args_global += '-D_GNU_SOURCE'
elif host_os.startswith('solaris')
  args_global += '-DSVR4'
endif

# Check for C compiler arguments
potential_c_args = [
  '-Wall',
  '-Werror=implicit-function-declaration',
  '-Werror=missing-prototypes',
  '-Wmissing-prototypes',
  '-fno-math-errno',
  '-fno-trapping-math',
  '-Qunused-arguments',
]
foreach f : potential_c_args
  if cc.has_argument(f)
    add_project_arguments(f, language : 'c')
  endif
endforeach

foreach f : ['-Werror=pointer-arith', '-Werror=vla']
  if cc.has_argument(f)
    args_c_msvc_compat += f
  endif
endforeach
if cc.has_argument('-fvisibility=hidden')
  args_c_visibility += '-fvisibility=hidden'
endif

# Check for C++ compiler arguments
potential_cpp_args = [
  '-Wall',
  '-Wno-non-virtual-dtor',  # Is this required.
  '-fno-math-errno',
  '-fno-trapping-math',
  '-Qunused-arguments',
]
foreach f : potential_cpp_args
  if cpp.has_argument(f)
    add_project_arguments(f, language : 'cpp')
  endif
endforeach
if cpp.has_argument('-fvisibility=hidden')
  args_cpp_visibility += '-fvisibility=hidden'
endif

# Check for SSE41 support
if (host_machine.cpu_family().startswith('x86') and
    cc.compiles('''
      #include <smmintrin.h>
      int param;
      int main() {
        __m128i a = _mm_set1_epi32 (param), b = _mm_set1_epi32 (param + 1), c;
        c = _mm_max_epu32(a, b);
        return _mm_cvtsi128_si32(c);
      }
      ''',
      args : ['-msse4.1', '-mstackrealign'],
      name : 'SSE 4.1')
    )
  add_project_arguments(['-msse4.1', '-mstackrealign'], language : 'c')
  args_global += '-DUSE_SSE41'
endif

# Check for new-style atomic builtins
if cc.compiles('''int main() { int n; return __atomic_load_n(&n, __ATOMIC_ACQUIRE); }''',
               name : 'Atomic Builtins')
  args_global += '-DUSE_GCC_ATOMIC_BUILTINS'
endif

# TODO: endian checks

# TODO: POWER8

# TODO: shared vs static

# TODO: enable-profile

# TODO: handle debug properly
args_global += '-DNDEBUG'

# Check linker argument
args_ld_symbolic = []
args_ld_gc_sections = []
if cc.links('''int main() { return 0; };''', args : '-Wl,-Bsymbolic',
            name : '-Bsymbolic')
  args_ld_symbolic += '-Wl,-Bsymbolic'
endif
if cc.links('''static char UnusedFunc() { return 5; } int main() { return 0; }''',
            args : '-Wl,--gc-sections', name : '--gc-sections')
  args_ld_gc_sections += '-Wl,--gc-sections'
endif
if cc.links('''int main() { return 0; }''',
            args : ['-Wl,--version-script', 
                    '@0@/meson/test-version-script.map'.format(meson.current_source_dir())],
            name : '--version-script')
  args_global += '-DHAVE_LD_VERSION_SCRIPT'
endif

# TODO: --dynamic-list

# TODO: texture_float

# TODO: asm

if cc.has_header('xlocale.h')
  args_global += '-DHAVE_XLOCALE_H'
endif
if cc.has_header('sys/sysctl.h')
  args_global += '-DHAVE_SYS_SYSCTL_H'
endif
if cc.has_header('strtof')
  args_global += '-DHAVE_STRTOF'
endif
if cc.has_header('mkostemp')
  args_global += '-DHAVE_MKOSTEMP'
endif
if cc.has_function('dl_iterate_phdr')
  args_global += '-DHAVE_DL_ITERATE_PHDR'
endif

if cc.has_function('posix_memalign')
  args_global += '-DHAVE_POSIX_MEMALIGN'
endif

# TODO : dladdr

# TODO: check for -lrt

# TODO: selinux

# TODO: LLVM

# TODO: meson_options [opengl, gles1, gles2, dri, gallium-extra-hud]

# TODO: sensors

# TODO: meson_options [dri3, glx, osmesa, gallium-osmesa, egl, xa, gbm, nin,
#                      xvmc, vdpau, omx, va, opencl, opencl_icd, gallium-tests,
#                      gallium-drivers, glvnd, gl-lib-name, osmesa-lib-name, 
#                      mangling]

# TODO: shared_glapi

# TODO: osmesa

# TODO: GLX

# TODO: toggle for this?
args_global += '-DGLX_USE_TLS'

# TODO: glx-read-only-text

# TODO: dri paths?

# TODO: dri drivers

# TODO: more dri options

# TODO: classic drivers

# TODO: more llvm

# TODO: meson_options : vulkan

# TODO: meson_options : vulkan-icdddir

# TODO: shader_cache

# TODO: osmesa channel bits

# TODO: gbm

# TODO: egl

# TODO: gallium state trackers

# TODO: nine

# TODO: clang-libdir

# TODO: libclc

# TODO: opencl

# TODO: egl-platforms

# TODO: egl no x11

# TODO: xvmc

# TODO: gallium tests

# TODO: xvmc

# TODO: vdpau

# TODO: omx

# TODO: va

# TODO: d3dlibdir

# TODO: SWR

# TODO: gallium drivers

# TODO: even more llvm

# TODO: valgrind
if meson.version() >= '0.40.0'
  dep_valgrind = dependency('valgrind', required : false)
  if dep_valgrind.found()
    add_project_arguments('-DHAVE_VALGRIND', language : 'c')
    add_project_arguments('-DHAVE_VALGRIND', language : 'cpp')
  endif
else
  dep_valgrind = []
endif

opt_wsi_wayland = get_option('wsi_wayland')
opt_wsi_x11 = get_option('wsi_x11')

opt_vk_intel = get_option('vk_intel')
opt_gl_intel = get_option('gl_intel')

opt_gl = opt_gl_intel
opt_vk = opt_vk_intel

opt_gl_api = true
opt_gles1_api = false
opt_gles2_api = false

opt_shared_glapi = true

if opt_vk and not (opt_wsi_wayland or opt_wsi_x11)
  error('Vulkan drivers require at least one of: wsi_x11, wsi_wayland')
endif

dep_dl = []
dep_elf = []
dep_libdrm = []
dep_math = []
dep_thread = []
dep_zlib = dependency('zlib', version : '>=1.2.8')

host_os = host_machine.system()

if host_os != 'solaris'
  dep_dl = cc.find_library('dl')
endif
if host_os != 'windows'
  dep_thread = dependency('threads')
  args_global += '-DHAVE_PTHREAD'
endif
if host_os != 'windows' and host_os != 'darwin'
  dep_elf = dependency('libelf')
  need_drm = true
  args_global += '-DHAVE_LIBDRM'
endif
if host_os == 'linux'
  dep_math = cc.find_library('m', required : true)  # TODO: require only on linux
endif
if opt_wsi_wayland
  prog_wayland_scanner = find_program('wayland-scanner')
  dep_wayland_client = dependency('wayland-client', version : '>=1.11')
  dep_wayland_server = dependency('wayland-server', version : '>=1.11')
endif
if opt_wsi_x11
  dep_x11_xcb = dependency('x11-xcb')
  dep_xcb_dri3 = dependency('xcb-dri3')
  dep_xcb_present = dependency('xcb-present')
  dep_xcb_sync = dependency('xcb-sync')
  dep_xshmfence = dependency('xshmfence')
endif

foreach a : args_global
  add_project_arguments(a, language : 'c')
  add_project_arguments(a, language : 'cpp')
endforeach

if need_drm
  # XXX: probably don't want this indenfinately
  dep_libdrm = dependency('libdrm', version : '>=2.4.74', fallback : ['libdrm', 'libdrm_dep'])
endif

inc_include = include_directories('include')
subdir('src')
