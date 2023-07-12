#!/usr/bin/env python

import pyscf as pyscf
import sys as sys
from pyscf import scf, cc
from pyscf.lib import logger

neutralMolecule = pyscf.M(atom = [['O', (0,0,0)]], basis = 'STO-3G', verbose = 9, charge = 0, spin = 2)
neutralMoleculeHF = scf.UHF(neutralMolecule).run()

logObject = logger.new_logger(neutralMoleculeHF) # Creates a new logger object
orbitals, _, stability, _  = neutralMoleculeHF.stability(return_status = True) # Returns four variables: Internal MO, External MO, Internal Stability, External Stability
