# Copyright © 2017 Intel Corporation

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

project('mesa', ['c', 'cpp'], version : '17.0.1-devel', soversion : '0')

yacc = find_program('yacc')
lex = find_program('lex')
python = find_program('python2')
touch = find_program('touch')
wl_scanner = find_program('wayland-scanner', require : get_option('wsi_wayland'))

c_compiler = meson.get_compiler('c')

if c_compiler.get_id() == 'gcc'
  ver = c_compiler.version()
  if ver.version_compare('<4.2')
    error('When using GCC, vresion 4.2.0 or greater is required')
  elif ver.version_compare('<4.6')
    add_global_arguments('-std=gnu99', langauge : 'c')
  else
    add_global_arguments('-std=c99', language : 'c')
  endif
else
  add_global_arguments('-std=c99', language : 'c')
endif

add_global_arguments('-D__STDC_CONSTANT_MACROS', '-D__STDC_FORMAT_MACROS', '-D__STDC_LIMIT_MACROS', language : 'c')
add_global_arguments('-D__STDC_CONSTANT_MACROS', '-D__STDC_FORMAT_MACROS', '-D__STDC_LIMIT_MACROS', language : 'cpp')

# TODO: this only handles linux atm
add_global_arguments('-D_GNU_SOURCE', language: 'c')
add_global_arguments('-D_GNU_SOURCE', language: 'cpp')

# FIXME: this is lazy, it probably is always correct, but....
if c_compiler.has_function('bswap32')
  add_global_arguments('-DHAVE___BUILTIN_BSWAP32', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_BSWAP32', language : 'cpp')
endif
if c_compiler.has_function('bswap64')
  add_global_arguments('-DHAVE___BUILTIN_BSWAP64', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_BSWAP64', language : 'cpp')
endif
if c_compiler.has_function('clz')
  add_global_arguments('-DHAVE___BUILTIN_CLZ', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_CLZ', language : 'cpp')
endif
if c_compiler.has_function('clzll')
  add_global_arguments('-DHAVE___BUILTIN_CLZLL', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_CLZLL', language : 'cpp')
endif
if c_compiler.has_function('ctz')
  add_global_arguments('-DHAVE___BUILTIN_CTZ', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_CTZ', language : 'cpp')
endif
if c_compiler.has_function('expect')
  add_global_arguments('-DHAVE___BUILTIN_EXPECT', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_EXPECT', language : 'cpp')
endif
if c_compiler.has_function('ffs')
  add_global_arguments('-DHAVE___BUILTIN_FFS', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_FFS', language : 'cpp')
endif
if c_compiler.has_function('ffsll')
  add_global_arguments('-DHAVE___BUILTIN_FFSLL', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_FFSLL', language : 'cpp')
endif
if c_compiler.has_function('popcount')
  add_global_arguments('-DHAVE___BUILTIN_POPCOUNT', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_POPCOUNT', language : 'cpp')
endif
if c_compiler.has_function('popcountll')
  add_global_arguments('-DHAVE___BUILTIN_POPCOUNTLL', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_POPCOUNTLL', language : 'cpp')
endif
if c_compiler.has_function('unreachable')
  add_global_arguments('-DHAVE___BUILTIN_UNREACHABLE', language : 'c')
  add_global_arguments('-DHAVE___BUILTIN_UNREACHABLE', language : 'cpp')
endif
if c_compiler.has_function('dl_iterate_phdr', required : false)
  add_global_arguments('-DHAVE_DL_ITERATE_PHDR', language : 'c')
  add_global_arguments('-DHAVE_DL_ITERATE_PHDR', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((const)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_CONST', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_CONST', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((format)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_FORMAT', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_FORMAT', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((malloc)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_MALLOC', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_MALLOC', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((packed)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_PACKED', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_PACKED', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((pure)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_PURE', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_PURE', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((returns_nonnull)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_RETURNS_NONNULL', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_RETURNS_NONNULL', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((unused)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_UNUSED', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_UNUSED', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((visibility)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_VISIBILITY', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_VISIBILITY', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((warn_unused_result)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_WARN_UNUSED_RESULT', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_WARN_UNUSED_RESULT', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((weak)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_WEAK', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_WEAK', language : 'cpp')
endif
if c_compiler.compiles('''__attribute__((alias)) void foo();''')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_ALIAS', language : 'c')
  add_global_arguments('-DHAVE_FUNC_ATTRIBUTE_ALIAS', language : 'cpp')
endif

if c_compiler.has_argument('-fvisibility=hidden')
  hidden_flags = '-fvisibility=hidden'
else
  hidden_flags = []
endif

# TODO: Windows and Cygwin
thread_dep = dependency('threads')
if host_machine.system() == 'linux'
  add_global_arguments('-DHAVE_PTHREAD', language : 'c')
  add_global_arguments('-DHAVE_PTHREAD', language : 'cpp')
  dl_open_args = '-ldl'
else
  dl_open_args = ''
endif
m_dep = c_compiler.find_library('m', required : host_machine.system() == 'linux')
dl_dep = c_compiler.find_library('dl')

# TODO: this needs to depend on a vulkan driver
if not (get_option('wsi_wayland') or get_option('wsi_x11'))
  error('Vulkan requires at least one Window system')
endif

wl_client = dependency('wayland-client', require : get_option('wsi_wayland'))
wl_server = dependency('wayland-server', require : get_option('wsi_wayland'))
x11_xcb = dependency('xcb', require : get_option('wsi_x11'))
x11_xcb_dri3 = dependency('xcb-dri3', require : get_option('wsi_x11'))
drm = dependency('libdrm', require : get_option('wsi_x11')) # TODO: or anv

# TODO: fix this
add_global_arguments('-DDEBUG', language : 'c')
add_global_arguments('-DDEBUG', language : 'cpp')

# XXX: work-around?
add_global_arguments('-Wno-error=non-virtual-dtor', '-Wno-non-virtual-dtor', language : 'cpp')

basic_includes = include_directories(
  'include', 'src', 'src/mapi', 'src/mesa', 'src/gallium/include',
  'src/gallium/auxiliary')

subdir('include')
subdir('src')
