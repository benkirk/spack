# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Criu(MakefilePackage):
    """CRIU: Checkpoint/Restore In Userspace can freeze a running
    container, or an individual application, and checkpoint its state
    to disk. The data saved can be used to restore the application and
    run it exactly as it was during the time of the freeze."""

    homepage = "http://criu.org/"
    url = "http://github.com/checkpoint-restore/criu/archive/v3.17.1/criu-3.17.1.tar.gz"

    maintainers = ["benkirk"]

    conflicts("platform=darwin", msg="CRIU requires Linux")
    conflicts("platform=windows", msg="CRIU requires Linux")

    version("3.17.1", sha256="f90fe2323ed1b84f273dc41dde1a38dd424157a57f713d1ba39094e70f90eca6")
    version("3.15", sha256="23c4c8824be081a162c8874ff79f5a2c30cf02b62662a12c89a43ed6bc5c5014")

    variant("doc", default=True, description="Build documentation")
    variant("tests", default=False, description="Build testsuite")

    # ref: https://criu.org/Installation
    depends_on("pkgconfig", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    depends_on("gnutls")
    depends_on("iproute2")
    depends_on("libbsd")
    depends_on("libcap")
    depends_on("libnet")
    depends_on("libnl")
    depends_on("nftables")
    depends_on("protobuf")
    depends_on("protobuf-c")
    depends_on("py-ipaddress")
    depends_on("py-protobuf")

    depends_on("asciidoc", when="+doc")
    depends_on("xmlto", when="+doc")

    depends_on("libaio", when="+tests")
    depends_on("py-future", when="+tests")

    def patch(self):
        # CRIU source comes with a hardcode symlink into /usr/...,
        # which is either missing or in any case wrong.
        # Point it to our dependent protobuf instead
        force_symlink(self.spec['protobuf'].prefix.include + "/google/protobuf/descriptor.proto",
                      "images/google/protobuf/descriptor.proto")

    def install(self, spec, prefix):
        make()
        make("PREFIX={0}".format(prefix), "install")
