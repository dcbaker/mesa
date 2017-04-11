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

glcpp_lex_c = custom_target(
  'glcpp-lex.c',
  input : 'glcpp-lex.l',
  output : 'glcpp-lex.c',
  command : [prog_flex, '-o', '@OUTPUT@', '@INPUT@'],
  build_by_default : false,
)

glcpp_parse = custom_target(
  'glcpp_parse.[ch]',
  input : 'glcpp-parse.y',
  output : ['glcpp-parse.c', 'glcpp-parse.h'],
  command : [prog_bison, '-o', '@OUTPUT0@', '-p', 'glcpp_parser_',
             '--defines=@OUTPUT1@', '@INPUT@'],
  build_by_default : false,
)

files_glcpp = files(
  'glcpp.h',
  'pp.c',
)

libglcpp = shared_library(
  'glcpp',
  [files_glcpp, glcpp_parse, glcpp_lex_c],
  link_with : libmesautil,
  include_directories : inc_common,
)
