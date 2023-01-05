#!/usr/bin/env python
# Author: Nike Dattani, nike@hpqc.org

import numpy as np
import pyscf
from pyscf import gto, scf, ao2mo, fci,ci

mol = pyscf.M(atom = 'Ne 0 0 0',basis = 'cc-pvDz',verbose=9,output='out_fci.txt')
mhf = scf.RHF(mol).run()
mci = fci.FCI(mhf).set(conv_tol=1e-5,nroots=3)
e, civec = mci.kernel()
