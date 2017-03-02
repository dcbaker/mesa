glcpp_parse = custom_target(
  'glcpp_parse',
  input : 'glcpp-parse.y',
  output : ['glcpp-parse.c', 'glcpp-parser.h'],
  command : [yacc, '-o', '@OUTPUT0@', '-p', 'glcpp_parser_', '--defines=@OUTPUT1@', '@INPUT@']
)

glcpp_lex = custom_target(
  'glcpp_lex',
  input : 'glcpp-lex.l',
  output : 'glcpp-lex.c',
  command : [lex, '-o', '@OUTPUT@', '@INPUT'],
)

libglcpp_sources = [
  glcpp_parse,
  glsl_lexer,
  glsl_parser,
  ir_exp_op_const,
  ir_exp_op_enum,
  ir_exp_op_str,
  'glcpp.h',
  'pp.c',
]

libglcpp = static_library(
  'glcpp',
  libglcpp_sources,
  include_directories : [basic_includes, include_directories('.', '..')],
  link_with : [libmesautil, libglsl_util],
)

# TODO:
#glcpp = executable(
  #'glcpp',
  #'glcpp.c',
  #include_directories : [basic_includes],
  #dependencies : m_dep,
  #link_with : [libglcpp, libglsl_util],
#)
