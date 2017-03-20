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

# TODO: replace these with a generator, but it will require that the python
#       write the file itself

gen4_pack_h = custom_target(
  'gen4_pack.h',
  input : ['gen_pack_header.py', 'gen4.xml'],
  output : 'gen4_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

gen45_pack_h = custom_target(
  'gen45_pack.h',
  input : ['gen_pack_header.py', 'gen45.xml'],
  output : 'gen45_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

gen5_pack_h = custom_target(
  'gen5_pack.h',
  input : ['gen_pack_header.py', 'gen5.xml'],
  output : 'gen5_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

gen6_pack_h = custom_target(
  'gen6_pack.h',
  input : ['gen_pack_header.py', 'gen6.xml'],
  output : 'gen6_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

gen7_pack_h = custom_target(
  'gen7_pack.h',
  input : ['gen_pack_header.py', 'gen7.xml'],
  output : 'gen7_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

gen75_pack_h = custom_target(
  'gen75_pack.h',
  input : ['gen_pack_header.py', 'gen75.xml'],
  output : 'gen75_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

gen8_pack_h = custom_target(
  'gen8_pack.h',
  input : ['gen_pack_header.py', 'gen8.xml'],
  output : 'gen8_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

gen9_pack_h = custom_target(
  'gen9_pack.h',
  input : ['gen_pack_header.py', 'gen9.xml'],
  output : 'gen9_pack.h',
  command : [prog_python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genX_bits_h = custom_target(
  'genX_bits.h',
  input : ['gen_bits_header.py', 'gen4.xml', 'gen45.xml', 'gen5.xml',
           'gen6.xml', 'gen7.xml', 'gen75.xml', 'gen8.xml', 'gen9.xml'],
  output : 'genX_bits.h',
  command : [prog_python, '@INPUT0@', '-o', '@OUTPUT@', '@INPUT1@', '@INPUT2@',
             '@INPUT3@', '@INPUT4@', '@INPUT5@', '@INPUT6@', '@INPUT7@',
             '@INPUT8@'],
)

# TODO: aubinator xml
