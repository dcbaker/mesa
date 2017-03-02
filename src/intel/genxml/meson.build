genxml_gen4_pack = custom_target(
  'genxml_gen4_pack',
  input : ['gen_pack_header.py', 'gen4.xml'],
  output : 'gen4_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_gen45_pack = custom_target(
  'genxml_gen45_pack',
  input : ['gen_pack_header.py', 'gen45.xml'],
  output : 'gen45_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_gen5_pack = custom_target(
  'genxml_gen5_pack',
  input : ['gen_pack_header.py', 'gen5.xml'],
  output : 'gen5_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_gen6_pack = custom_target(
  'genxml_gen6_pack',
  input : ['gen_pack_header.py', 'gen6.xml'],
  output : 'gen6_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_gen7_pack = custom_target(
  'genxml_gen7_pack',
  input : ['gen_pack_header.py', 'gen7.xml'],
  output : 'gen7_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_gen75_pack = custom_target(
  'genxml_gen75_pack',
  input : ['gen_pack_header.py', 'gen75.xml'],
  output : 'gen75_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_gen8_pack = custom_target(
  'genxml_gen8_pack',
  input : ['gen_pack_header.py', 'gen8.xml'],
  output : 'gen8_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_gen9_pack = custom_target(
  'genxml_gen9_pack',
  input : ['gen_pack_header.py', 'gen9.xml'],
  output : 'gen9_pack.h',
  command : [python, '@INPUT0@', '@INPUT1@'],
  capture : true,
)

genxml_pack = declare_dependency(
  sources : [genxml_gen4_pack, genxml_gen45_pack, genxml_gen5_pack,
             genxml_gen6_pack, genxml_gen7_pack, genxml_gen75_pack,
             genxml_gen8_pack, genxml_gen9_pack]
)
