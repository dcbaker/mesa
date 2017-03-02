libblorp = static_library(
  'blorp',
  ['blorp_blit.c', 'blorp_genX_exec.h', 'blorp_clear.c', 'blorp.c', 'blorp_priv.h', 'blorp.h'],
  include_directories : [basic_includes,
                         include_directories('../../compiler/nir', '..', '../compiler',
                                             '../../mesa/drivers/dri/i965')],
)
