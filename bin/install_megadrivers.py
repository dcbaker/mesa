#!/usr/bin/env python
# encoding=utf-8
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

"""Script to install megadriver symlinks for meson."""

import argparse
import errno
import os
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('megadriver')
    parser.add_argument('libdir')
    parser.add_argument('drivers', nargs='+')
    args = parser.parse_args()

    to = os.path.join(os.environ.get('MESON_INSTALL_DESTDIR_PREFIX'), args.libdir)

    cross_found = False

    if not os.path.exists(to):
        os.makedirs(to)
    form_ = args.megadriver

    for each in args.drivers:
        final = os.path.join(to, each)
        if os.path.exists(final):
            os.unlink(final)
        print('installing {} to {}'.format(args.megadriver, to))
        try:
            os.link(from_, final)
        except OSError as e:
            if e.errno == errno.EXDEV:
                if cross_found:
                    raise Exception('Something went very wrong.')
                # if we hit this then we're trying to link from one filesystem,
                # which is obviously invalid. Instead copy the first binary,
                # then set that as the from so that the hard links will work
                shutil.copy(from_, final)
                from_ = final
                cross_found = True
            else:
                raise


if __name__ == '__main__':
    main()
