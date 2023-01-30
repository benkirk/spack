# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PeakMemusage(AutotoolsPackage):
    """This utility is a wrapper around getrusage, which reports peak
    memory use of any executable. It is OpenMP and MPI aware and tries
    to report thread- and task- specific data. Of course, being OpenMP
    shared memory, that report cannot really separate thread-specific
    memory use."""

    homepage = "https://github.com/NCAR/peak_memusage"
    url = "https://github.com/NCAR/peak_memusage/archive/refs/tags/v2.1.0.tar.gz"

    maintainers = ["benkirk"]

    version("3.0.0", sha256="fa31489432da98980660310d7aaedccf406defab72a247e487a8210347d2534b")
    version("2.1.0", sha256="6d4ea85a9d77144ba7e140e84466fa1e545fc280049d99ec77f763cb8ce82187")

    variant("openmp", default=True, description="Build OpenMP-enabled test suite")
    variant("doc", default=False, description="Build Documentation from source files (requires Doxygen")
    variant("fortran", default=True, description="Build Fortran API")
    #variant("mpi", default=False, description="Build MPI-enabled test suite")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconf")
    depends_on("doxygen", when="+doc")


    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        args = []
        if "~openmp" in self.spec: args.append("--disable-openmp")
        if "+doc" in self.spec: args.append("--enable-doc")
        if "~fortran" in self.spec: args.append("--disable-fortran")
        return args
