# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libx265(CMakePackage):
    """x265 is an open source HEVC encoder"""

    homepage = "https://bitbucket.org/multicoreware/x265_git/wiki/Home"
    url = "https://bitbucket.org/multicoreware/x265_git/downloads/x265_3.5.tar.gz"

    maintainers = ["benkirk"]

    depends_on("nasm@2.13:")
    depends_on("numactl")

    version("3.5",   sha256="e70a3335cacacbba0b3a20ec6fecd6783932288ebc8163ad74bcc9606477cae8")
    version("3.3",   sha256="c6d744a87eda55560da715f56f878640554ddc06e2d0fcbd822fa330affc22cc")
    version("3.2.1", sha256="b68939625356459e7055b9589451689924f236bac8deba3db21e3c2fb062d328")
    version("3.2",   sha256="d837cb8137bc459d40ae19a851a0191e0b863f2227298baa32ef465f14936f8f")
    version("3.1.2", sha256="6f785f1c9a42e00a56402da88463bb861c49d9af108be53eb3ef10295f2a59aa")

    depends_on("cmake@3:", type="build")

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make("install")
