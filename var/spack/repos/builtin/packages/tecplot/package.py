# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class Tecplot(Package):
    """Tecplot 360 is a Computational Fluid Dynamics (CFD) and numerical
    simulation software package used in post-processing simulation results.
    It is also used in chemistry applications to visualize molecule structure
    by post-processing charge density data."""

    homepage = "https://www.tecplot.com/"
    #manual_download = True

    version('2021r2', '768264ec76111613ca753226fce2d08c85ae4e4c6fdc8760cbc13a0c00678dd9', expand=False)
    version('2020r2', '8cc121ab46f86573fdf1c4b505ee09aa7c9035b1a12ae0a2bec283d9cb5c29eb', expand=False)
    version('2018r2', '768264ec76111613ca753226fce2d08c85ae4e4c6fdc8760cbc13a0c00678dd9', expand=False)

    def url_for_version(self, version):
        #return "file://{0}/tecplot360ex{1}_linux64.sh".format(os.getcwd(), version)

        # sample: /aerolab/admin/software/dist/tecplot/tecplot360ex_2021_r2/tecplot360ex2021r2_linux64.sh
        uversion = '{}'.format(version).replace('r', '_r')
        return  "file:///aerolab/admin/software/dist/tecplot/tecplot360ex_{0}/tecplot360ex{1}_linux64.sh".format(uversion, version)

    def install(self, spec, prefix):
        #BSK: skip this, seems to corrupt the emebedded .tgz.  We can accomplish the same with command-line args.
        #makefile = FileFilter(self.stage.archive_file)
        #makefile.filter('interactive=TRUE', 'interactive=FALSE')
        #makefile.filter('cpack_skip_license=FALSE', 'cpack_skip_license=TRUE')

        set_executable(self.stage.archive_file)
        installer = Executable(self.stage.archive_file)
        installer('--skip-license', '--exclude-chorus', '--prefix=%s' % prefix)
