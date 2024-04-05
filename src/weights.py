import json

with open('data/weights.json') as f:
    weights = json.load(f)

with open('data/systems.json') as f:
    systems = json.load(f)

print(weights['investFactor'])
investFactor = weights['investFactor']
operatingFactor = weights['operatingFactor']
co2Factor = weights['co2Factor']

suppliers = systems['supplier']
storages = systems['storages']
lines = systems['line']

supplier_values = dict()
for supplier in suppliers:
    supplier_values[supplier] = suppliers[supplier]["invest"] * investFactor + suppliers[supplier]["operatingCost"] * operatingFactor * 24 * 360 * 25 + suppliers[supplier]["co2"] * co2Factor * 24 * 360 * 25
    print(supplier, supplier_values[suppliers[supplier]['name']])


with open('data/loadprofiles/potentials_summer.json') as f:
    potentials = json.load(f)

sum = 0
for potential in potentials['pv_potential']:
    sum += potential

print(sum * suppliers['Photovoltaics']['output']['factor'])