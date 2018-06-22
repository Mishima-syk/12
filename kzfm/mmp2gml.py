#!/usr/bin/env python

from schema import mmpdb, Pair, Compound, CompoundProperty
from igraph import Graph

g = Graph()
smiles = []
names = []
pIC50 = []
pIC50_dict = {}

for cp in mmpdb.query(CompoundProperty).filter_by(property_name_id=0).all():
    pIC50_dict[cp.compound_id] = cp.value

for c in mmpdb.query(Compound).all():
    smiles.append(c.clean_smiles)
    pIC50.append(pIC50_dict[c.id])
    names.append(c.public_id)


g.add_vertices(len(smiles))

pairs = []
dpIC50 = []
for pair in mmpdb.query(Pair).all():
    if (pair.compound1_id, pair.compound2_id) not in pairs:
        pairs.append((pair.compound1_id, pair.compound2_id))
        dpIC50.append(abs(pIC50_dict[pair.compound1_id] - pIC50_dict[pair.compound2_id]))

g.add_edges(pairs)
g.vs["smiles"] = smiles
g.vs["pIC50"] = pIC50
g.vs["pubid"] = names
g.es["delta"] = dpIC50

g.save("CHEMBL930273.gml")

