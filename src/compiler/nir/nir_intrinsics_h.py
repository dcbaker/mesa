
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

#ifndef _NIR_INTRINSICS_
#define _NIR_INTRINSICS_

<% opcode_names = sorted(intr_opcodes.iterkeys()) %>

typedef enum {
% for name in opcode_names:
   nir_intrinsic_${name},
% endfor

   nir_last_intrinsic = nir_intrinsic_${opcode_names[-1]},
   nir_num_intrinsics = nir_last_intrinsic + 1
} nir_intrinsic_op;

#endif /* _NIR_INTRINSICS_ */"""

from nir_intrinsics import intr_opcodes
from mako.template import Template

print Template(template).render(intr_opcodes=intr_opcodes)
