from rdkit import Chem
from rdkit.Chem import AllChem
import ast
from tqdm import tqdm

mols = []

smiles_list = ast.literal_eval(open('dgl_smiles.txt').readlines()[0])

for s in smiles_list:
      try:
            mols.append(Chem.MolFromSmiles(s))
      except:
            pass

for i,mol in tqdm(enumerate(mols)):
      try:
            mol = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol,randomSeed=0xf00d)
            AllChem.MMFFOptimizeMolecule(mol)
            Chem.MolToXYZFile(mol,f'./xyz/{smiles_list[i]}.xyz')
      except:
            pass