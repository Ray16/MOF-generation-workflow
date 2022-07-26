#import faulthandler
#faulthandler.enable()
from tqdm import tqdm
from dgllife.model import load_pretrained
model = load_pretrained('DGMG_ZINC_canonical')
model.eval()
smiles = []
print('generating new datasets ...')
for i in tqdm(range(1000)):
	smiles.append(model(rdkit_mol=True))
	with open('dgl_smiles.txt','w+') as f:
		f.write(str(smiles))