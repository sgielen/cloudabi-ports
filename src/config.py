# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import platform
import os

# Architectures for which we can build packages.
ARCHITECTURES = {
    'aarch64-unknown-cloudabi',
    'armv6-unknown-cloudabi-eabihf',
    'armv7-unknown-cloudabi-eabihf',
    'i686-unknown-cloudabi',
    'x86_64-unknown-cloudabi',
}

# Temporary directory where packages will be built. This directory has
# to be fixed, as the compilation process tends to hardcode paths to the
# build directory. Debug symbols and __FILE__ use absolute paths.
DIR_BUILDROOT = '/usr/obj/cloudabi-ports'

# Location where resource files are stored.
DIR_RESOURCES = os.path.join(os.getcwd(), 'misc')

# Location at which distfiles can be fetched in case the master sites
# are down.
FALLBACK_MIRRORS = {'https://nuxi.nl/distfiles/third_party/'}

# Host C and C++ compiler, used to compile the build tools. We'd better
# use Clang if available. Compared to GCC, it has the advantage that it
# does not depend on the 'as' and 'ld' utilities being part of $PATH.
for i in ['/usr/bin/clang', '/usr/bin/clang-3.7']:
    if os.path.exists(i):
        HOST_CC = i
        break
for i in ['/usr/bin/clang++', '/usr/bin/clang++-3.7']:
    if os.path.exists(i):
        HOST_CXX = i
        break

# Name of the Perl executable.
for i in ['/usr/bin/perl', '/usr/local/bin/perl']:
    if os.path.exists(i):
        PERL = i
        break
