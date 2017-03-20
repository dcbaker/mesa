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

inc_nir = include_directories('.')

files_libnir = files(
  'nir.c',
  'nir.h',
  'nir_array.h',
  'nir_builder.h',
  'nir_clone.c',
  'nir_constant_expressions.h',
  'nir_control_flow.c',
  'nir_control_flow.h',
  'nir_control_flow_private.h',
  'nir_dominance.c',
  'nir_from_ssa.c',
  'nir_gather_info.c',
  'nir_gs_count_vertices.c',
  'nir_inline_functions.c',
  'nir_instr_set.c',
  'nir_instr_set.h',
  'nir_intrinsics.c',
  'nir_intrinsics.h',
  'nir_liveness.c',
  'nir_loop_analyze.c',
  'nir_loop_analyze.h',
  'nir_lower_64bit_packing.c',
  'nir_lower_alu_to_scalar.c',
  'nir_lower_atomics.c',
  'nir_lower_bitmap.c',
  'nir_lower_clamp_color_outputs.c',
  'nir_lower_clip.c',
  'nir_lower_clip_cull_distance_arrays.c',
  'nir_lower_constant_initializers.c',
  'nir_lower_double_ops.c',
  'nir_lower_drawpixels.c',
  'nir_lower_global_vars_to_local.c',
  'nir_lower_gs_intrinsics.c',
  'nir_lower_load_const_to_scalar.c',
  'nir_lower_locals_to_regs.c',
  'nir_lower_idiv.c',
  'nir_lower_indirect_derefs.c',
  'nir_lower_int64.c',
  'nir_lower_io.c',
  'nir_lower_io_to_temporaries.c',
  'nir_lower_io_to_scalar.c',
  'nir_lower_io_types.c',
  'nir_lower_passthrough_edgeflags.c',
  'nir_lower_patch_vertices.c',
  'nir_lower_phis_to_scalar.c',
  'nir_lower_regs_to_ssa.c',
  'nir_lower_returns.c',
  'nir_lower_samplers.c',
  'nir_lower_system_values.c',
  'nir_lower_tex.c',
  'nir_lower_to_source_mods.c',
  'nir_lower_two_sided_color.c',
  'nir_lower_vars_to_ssa.c',
  'nir_lower_var_copies.c',
  'nir_lower_vec_to_movs.c',
  'nir_lower_wpos_center.c',
  'nir_lower_wpos_ytransform.c',
  'nir_metadata.c',
  'nir_move_vec_src_uses_to_dest.c',
  'nir_normalize_cubemap_coords.c',
  'nir_opt_conditional_discard.c',
  'nir_opt_constant_folding.c',
  'nir_opt_copy_prop_vars.c',
  'nir_opt_copy_propagate.c',
  'nir_opt_cse.c',
  'nir_opt_dce.c',
  'nir_opt_dead_cf.c',
  'nir_opt_gcm.c',
  'nir_opt_global_to_local.c',
  'nir_opt_if.c',
  'nir_opt_loop_unroll.c',
  'nir_opt_move_comparisons.c',
  'nir_opt_peephole_select.c',
  'nir_opt_remove_phis.c',
  'nir_opt_trivial_continues.c',
  'nir_opt_undef.c',
  'nir_phi_builder.c',
  'nir_phi_builder.h',
  'nir_print.c',
  'nir_propagate_invariant.c',
  'nir_remove_dead_variables.c',
  'nir_repair_ssa.c',
  'nir_search.c',
  'nir_search.h',
  'nir_search_helpers.h',
  'nir_split_var_copies.c',
  'nir_sweep.c',
  'nir_to_lcssa.c',
  'nir_validate.c',
  'nir_vla.h',
  'nir_worklist.c',
  'nir_worklist.h',
)

files_nir_opcodes = files('nir_opcodes.py')

nir_builder_opcodes_h = custom_target(
  'nir_builder_opcodes.h',
  input : 'nir_builder_opcodes_h.py',
  output : 'nir_builder_opcodes.h',
  command : [prog_python, '@INPUT@'],
  capture : true,
  depend_files : files_nir_opcodes,
)

nir_constant_expressions_c = custom_target(
  'nir_constant_expressions.c',
  input : 'nir_constant_expressions.py',
  output : '@BASENAME@.c',
  command : [prog_python, '@INPUT@'],
  capture : true,
  depend_files : files_nir_opcodes,
)

nir_opcodes_h = custom_target(
  'nir_opcodes.h',
  input : 'nir_opcodes_h.py',
  output : 'nir_opcodes.h',
  command : [prog_python, '@INPUT@'],
  capture : true,
  depend_files : files_nir_opcodes,
)

nir_opcodes_c = custom_target(
  'nir_opcodes.c',
  input : 'nir_opcodes_c.py',
  output : 'nir_opcodes.c',
  command : [prog_python, '@INPUT@'],
  capture : true,
  depend_files : files_nir_opcodes,
)

nir_opt_algebraic_c = custom_target(
  'nir_opt_algebraic.c',
  input : 'nir_opt_algebraic.py',
  output : '@BASENAME@.c',
  command : [prog_python, '@INPUT@'],
  capture : true,
  depend_files : files('nir_algebraic.py'),
)

libnir = static_library(
  'nir',
  [files_compiler, files_libnir, files_spirv, nir_builder_opcodes_h,
   nir_constant_expressions_c, nir_opcodes_h, nir_opcodes_c,
   nir_opt_algebraic_c, ir_expression_operation_h],
  include_directories : [inc_common, inc_compiler],
  c_args : [args_c_visibility, args_c_msvc_compat],
  cpp_args : [args_cpp_visibility, args_cpp_msvc_compat],
)
