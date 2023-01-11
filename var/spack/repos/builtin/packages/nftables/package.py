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

    homepage = "https://www.netfilter.org"
    url = "https://netfilter.org/projects/nftables/files/nftables-1.0.5.tar.bz2"

    maintainers = ["benkirk"]

    version("1.0.5", sha256="8d1b4b18393af43698d10baa25d2b9b6397969beecac7816c35dd0714e4de50a")

    # FIXME: Add dependencies if required.
    depends_on("libmnl@1.0.4:")

    def configure_args(self):
        args = []
        return args
