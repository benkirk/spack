# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Nftables(AutotoolsPackage):
    """The netfilter project enables packet filtering, network address
    [and port] translation (NA[P]T), packet logging, userspace packet
    queueing and other packet mangling.

    nftables is the successor of iptables, it allows for much more
    flexible, scalable and performance packet classification. This is
    where all the fancy new features are developed."""

    homepage = "https://netfilter.org/projects/nftables"
    url = "https://netfilter.org/projects/nftables/files/nftables-1.0.5.tar.bz2"

    maintainers = ["benkirk"]

    version("1.0.5", sha256="8d1b4b18393af43698d10baa25d2b9b6397969beecac7816c35dd0714e4de50a")
    version("0.9.3", sha256="956b915ce2a7aeaff123e49006be7a0690a0964e96c062703181a36e2e5edb78")
    version("0.8.4", sha256="ef372ee4592b07852f4cac233584ead7cbd08fa3041b2d3ff3d3590c8d76769f")

    depends_on("pkgconf", type="build")
    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("libedit")
    depends_on("libnftnl")
    depends_on("libmnl@1.0.4:")
    depends_on("gmp")
    depends_on("readline", when="@:1.0.0")

    def configure_args(self):
        args = ["--disable-man-doc"]
        return args
