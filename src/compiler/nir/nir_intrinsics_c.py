
template = """\
/* Copyright (C) 2018 Red Hat
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice (including the next
 * paragraph) shall be included in all copies or substantial portions of the
 * Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

#include "nir.h"

const nir_intrinsic_info nir_intrinsic_infos[nir_num_intrinsics] = {
% for name, opcode in sorted(intr_opcodes.iteritems()):
{
   .name = "${name}",
   .num_srcs = ${opcode.num_srcs},
   .src_components = {
      ${ ", ".join(str(comp) for comp in opcode.src_components) }
   },
   .has_dest = ${ "TRUE" if opcode.has_dest else "FALSE" },
   .dest_components = ${opcode.dest_components},
   .num_variables = ${opcode.num_variables},
   .num_indices = ${opcode.num_indices},
   .index_map = {
      ${ ", ".join(str(idx) for idx in opcode.indices) }
    },
   .flags = ${ "0" if len(opcode.flags) == 0 else " | ".join(opcode.flags) },
},
% endfor
};
"""

from nir_intrinsics import intr_opcodes
from mako.template import Template

print Template(template).render(intr_opcodes=intr_opcodes)
