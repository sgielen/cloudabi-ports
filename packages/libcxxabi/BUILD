# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    ctx.extract('libunwind-%(version)s.src').rename(root.path('libunwind'))
    sources = {
        'abort_message.cpp',
        'cxa_aux_runtime.cpp',
        'cxa_default_handlers.cpp',
        'cxa_demangle.cpp',
        'cxa_exception.cpp',
        'cxa_exception_storage.cpp',
        'cxa_guard.cpp',
        'cxa_handlers.cpp',
        'cxa_new_delete.cpp',
        'cxa_noexception.cpp',
        'cxa_personality.cpp',
        'cxa_thread_atexit.cpp',
        'cxa_unexpected.cpp',
        'cxa_vector.cpp',
        'cxa_virtual.cpp',
        'fallback_malloc.cpp',
        'private_typeinfo.cpp',
        'stdlib_exception.cpp',
        'stdlib_stdexcept.cpp',
        'stdlib_typeinfo.cpp',
    }
    srcdir = root.path('src')
    libcxxabi = ctx.archive(
        srcdir.path(f).compile(
            ['-I../include', '-I../libunwind/include', '-std=c++11'])
        for f in sources)

    libcxxabi.install('lib/libc++abi.a')
    for f in {'include/cxxabi.h', 'include/__cxxabi_config.h'}:
        root.path(f).install(f)


package(
    name='libcxxabi',
    version='4.0.0',
    homepage='http://libcxxabi.llvm.org/',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build)

distfile(
    name='libcxxabi-4.0.0.src.tar.xz',
    checksum='dca9cb619662ad2d3a0d685c4366078345247218c3702dd35bcaaa23f63481d8',
    master_sites={'http://www.llvm.org/releases/4.0.0/'})
