# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libnftnl(AutotoolsPackage):
    """A library for low-level interaction with nftables Netlink's API
    over libmnl."""

    homepage = "https://git.netfilter.org/libnftnl/"
    #url = "http://ftp.netfilter.org/pub/libnftnl/libnftnl-1.1.5.tar.bz2"
    url = "https://netfilter.org/projects/libnftnl/files/libnftnl-1.2.4.tar.bz2"

    version("1.2.4", sha256="c0fe233be4cdfd703e7d5977ef8eb63fcbf1d0052b6044e1b23d47ca3562477f")
    version("1.1.6", sha256="c1eb5a696fc1d4b3b412770586017bc01af93da3ddd25233d34a62979dee1eca")
    version("1.1.5", sha256="66de4d05227c0a1a731c369b193010d18a05b1185c2735211e0ecf658eeb14f3")
    version("1.1.4", sha256="c8c7988347adf261efac5bba59f8e5f995ffb65f247a88cc144e69620573ed20")
    version("1.1.0", sha256="ec0eaca11b165110c2b61e6a7b50a7a0a9b17fa04a0c333f795bec2d19f78f6c")
    version("1.0.8", sha256="e6bdd799ef9c59fc247954aba9f2c6469d8e04cfaee73526728011eaa3632038")

    depends_on("pkgconfig", type="build")
    depends_on("libmnl@1.0.3:")
