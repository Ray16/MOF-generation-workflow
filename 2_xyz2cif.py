import os
from ase import Atoms
from ase.io import read, write
from ase.visualize import view
from ase.build import bulk

xyz_dir = 'xyz/'
for i in os.listdir(xyz_dir):
      xyz = read(xyz_dir+i)
      cell = Atoms(xyz,pbc=True,cell=[30,30,30])
      cif = write(f"./cif/{i.split('.')[0]}.cif", cell,format="cif")