# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Podman(Package):
    """An optionally rootless and daemonless container engine: alias docker=podman"""

    homepage = "https://podman.io"
    url = "https://github.com/containers/podman/archive/refs/tags/v4.3.1.tar.gz"
    maintainers("bernhardkaindl")

    version("4.7.2", sha256="10346c5603546427bd809b4d855d1e39b660183232309128ad17a64969a0193d")
    version("4.7.1", sha256="b785fe69041a0f222a8e1f8165816d767cb9bff5418f3f559547da82c0c279cc")
    version("4.7.0", sha256="8fbeab8a821c59ac10ade87c9597d7bb13be4f7868b438278a9f6a17c50bf20d")
    version("4.6.2", sha256="2d8e04f0c3819c3f0ed1ca5d01da87e6d911571b96ae690448f7f75df41f2ad1")
    version("4.6.1", sha256="6b3bfdc5ea9ca91f19b569d5a0763403823bde64be895060ec81dde4df692745")
    version("4.6.0", sha256="a1b4fd7c3a9b850ab4b405f8d03115248a780c89b11e7d8ffbba2d1f668f678e")
    version("4.5.1", sha256="ee2c8b02b7fe301057f0382637b995a9c6c74e8d530692d6918e4c509ade6e39")
    version("4.3.1", sha256="455c29c4ee78cd6365e5d46e20dd31a5ce4e6e1752db6774253d76bd3ca78813")
    version("3.4.7", sha256="4af6606dd072fe946960680611ba65201be435b43edbfc5cc635b2a01a899e6e")
    version("3.4.2", sha256="b0c4f9a11eb500b1d440d5e51a6c0c632aa4ac458e2dc0362f50f999eb7fbf31")

    # See <https://github.com/containers/podman/issues/16996> for the
    # respective issue and the suggested patch
    patch("markdown-utf8.diff", when="@4.3")

    depends_on("go", type="build")
    depends_on("go-md2man", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("python", type="build")
    depends_on("cni-plugins", type="run")
    depends_on("conmon", type="run")
    depends_on("runc", type="run")
    depends_on("slirp4netns", type="run")
    depends_on("gpgme")
    depends_on("libassuan")
    depends_on("libgpg-error")
    depends_on("libseccomp")

    def patch(self):
        defs = FileFilter("vendor/github.com/containers/common/pkg/config/default.go")

        # Prepend the provided runc executable to podman's built-in runc search path
        defs.filter('"runc": {', '"runc": {' + '"{0}",'.format(self.spec["runc"].prefix.sbin.runc))
        # Prepend the provided conmon executable to podman's built-in conmon search path
        defs.filter(
            r"ConmonPath = \[\]string{",
            "ConmonPath = []string{"
            + '\n        "{0}",'.format(self.spec["conmon"].prefix.bin.conmon),
        )
        # Prepend the provided cni-plugins directory to the cni-plugin search path
        defs.filter(
            r"DefaultCNIPluginDirs = \[\]string{",
            "DefaultCNIPluginDirs = []string{"
            + '\n        "{0}",'.format(self.spec["cni-plugins"].prefix.bin),
        )
        # Set the default path for slirp4netns to the provided slirp4netns executable
        defs.filter(
            "cniConfig := _cniConfigDir",
            "cniConfig := _cniConfigDir"
            + '\n        defaultEngineConfig.NetworkCmdPath = "{0}"'.format(
                self.spec["slirp4netns"].prefix.bin.slirp4netns
            ),
        )
        # Use the podman install prefix as fallback path for finding container.conf
        filter_file(
            r"/usr", self.prefix, "vendor/github.com/containers/common/pkg/config/config.go"
        )

    def install(self, spec, prefix):
        # Set default policy.json to be located in the install prefix (documented)
        env["EXTRA_LDFLAGS"] = (
            "-X github.com/containers/image/v5/signature.systemDefaultPolicyPath="
            + prefix
            + "/etc/containers/policy.json"
        )
        # Build and installation needs to be in two separate make calls
        # The devicemapper and btrfs drivers are (so far) not enabled in this recipe
        tags = "seccomp exclude_graphdriver_devicemapper exclude_graphdriver_btrfs"
        make("-e", "BUILDTAGS=" + tags)
        make("install", "PREFIX=" + prefix)
        # Install an initial etc/containers/policy.json (configured in prefix above)
        mkdirp(prefix.etc.containers)
        install("test/policy.json", prefix.etc.containers)
        # Cleanup directory trees which are created as part of the go build process
        remove_linked_tree(prefix.src)
        remove_linked_tree(prefix.pkg)
