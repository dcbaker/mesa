get_hash = custom_target(
  'get_hash',
  input : ['get_hash_generator.py', '../../mapi/glapi/gen/gl_and_es_API.xml'],
  output : 'get_hash.h',
  # TODO: depends : declare_dependency(sources : 'get_hash_generator.py'),
  capture : true,
  command : [python, '@INPUT0@', '@INPUT1@'],
)

format_info = custom_target(
  'format_info',
  input : ['format_info.py', 'formats.csv'],
  output : 'format_info.h',
  # TODO: depends : declare_dependency(sources : 'format_parser.py'),
  capture : true,
  command : [python, '@INPUT0@', '@INPUT1@'],
)
