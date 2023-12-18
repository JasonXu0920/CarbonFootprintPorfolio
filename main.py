# flake8: noqa

import pandas as pd
import matplotlib.pyplot as plt


portfoliaHoldings = pd.read_csv('PortfolioHoldings.csv')
id = pd.read_csv('IDmap.csv')
carbon = pd.read_csv('CarbonData.csv')

sedol = []
pCategory = []
for i in range(len(portfoliaHoldings)):
    for j in range(len(id)):
        if portfoliaHoldings.iloc[i]['Ticker'] == id.iloc[j]['ticker']:
            sedol.append(id.iloc[j]['sedol'])
            pCategory.append(id.iloc[j]['CategoryGroup'])
portfoliaHoldings['sedol'] = sedol
portfoliaHoldings['category'] = pCategory

scope1 = []
scope2 = []
revenue = []
for i in range(len(portfoliaHoldings)):
    matchedScope1 = 0
    matchedScope2 = 0
    matchedRevenue = 0
    for j in range(len(carbon)):
        if portfoliaHoldings.iloc[i]['sedol'] == carbon.iloc[j]['SEDOL']:
            matchedScope1 = carbon.iloc[j]['EMISSIONS_SCOPE_1']
            matchedScope2 = carbon.iloc[j]['EMISSIONS_SCOPE_2']
            matchedRevenue = carbon.iloc[j]['REVENUE_USD'] 
    scope1.append(matchedScope1)
    scope2.append(matchedScope2)
    revenue.append(matchedRevenue)

portfoliaHoldings['scope1'] = scope1
portfoliaHoldings['scope2'] = scope2
portfoliaHoldings['revenue'] = revenue
#print(portfoliaHoldings)

totalInvested = 0
weight = 0
porfolioWACI = 0
C1porfolioWACI = 0
C2porfolioWACI = 0
C3porfolioWACI = 0

for i in range(len(portfoliaHoldings)):
    totalInvested += (portfoliaHoldings.iloc[i]['Units']*portfoliaHoldings.iloc[i]['Price'])

for i in range(len(portfoliaHoldings)):
    if portfoliaHoldings.iloc[i]['scope1'] != 0 and portfoliaHoldings.iloc[i]['scope2'] != 0 and portfoliaHoldings.iloc[i]['revenue'] != 0:
        weight = (portfoliaHoldings.iloc[i]['Units']*portfoliaHoldings.iloc[i]['Price']) / totalInvested
        porfolioWACI += (weight * (portfoliaHoldings.iloc[i]['scope1']*portfoliaHoldings.iloc[i]['scope2']/portfoliaHoldings.iloc[i]['revenue']))
        if portfoliaHoldings.iloc[i]['category'] == 1:
            C1porfolioWACI += (weight * (portfoliaHoldings.iloc[i]['scope1']*portfoliaHoldings.iloc[i]['scope2']/portfoliaHoldings.iloc[i]['revenue']))
        if portfoliaHoldings.iloc[i]['category'] == 2:
            C2porfolioWACI += (weight * (portfoliaHoldings.iloc[i]['scope1']*portfoliaHoldings.iloc[i]['scope2']/portfoliaHoldings.iloc[i]['revenue']))
        if portfoliaHoldings.iloc[i]['category'] == 3:
            C3porfolioWACI += (weight * (portfoliaHoldings.iloc[i]['scope1']*portfoliaHoldings.iloc[i]['scope2']/portfoliaHoldings.iloc[i]['revenue']))



print(f'porfolioWACI: {porfolioWACI}')
print(f'C1 - porfolioWACI: {C1porfolioWACI}, contribution to total is: {C1porfolioWACI/porfolioWACI}')
print(f'C2 - porfolioWACI: {C2porfolioWACI}, contribution to total is: {C2porfolioWACI/porfolioWACI}')
print(f'C3 - porfolioWACI: {C3porfolioWACI}, contribution to total is: {C3porfolioWACI/porfolioWACI}')

 
plt.title("PortfolioHoldings - Each Category's Contribution")
categoryGroup = ['C1', 'C2', 'C3']
contributions = [round(C1porfolioWACI, 2), round(C1porfolioWACI,2), round(C3porfolioWACI,2)]
plt.bar(categoryGroup,contributions)
plt.savefig("porfolioHoldings.jpg")
plt.show()
plt.clf()


benchmarkHoldings = pd.read_csv("BenchmarkHoldings.csv")
sedol = []
bCategory = []
for i in range(len(benchmarkHoldings)):
    for j in range(len(id)):
        if benchmarkHoldings.iloc[i]['ticker'] == id.iloc[j]['ticker']:
            sedol.append(id.iloc[j]['sedol'])
            bCategory.append(id.iloc[j]['CategoryGroup'])
benchmarkHoldings['sedol'] = sedol
benchmarkHoldings['category'] = bCategory

scope1 = []
scope2 = []
revenue = []
for i in range(len(benchmarkHoldings)):
    matchedScope1 = 0
    matchedScope2 = 0
    matchedRevenue = 0
    for j in range(len(carbon)):
        if benchmarkHoldings.iloc[i]['sedol'] == carbon.iloc[j]['SEDOL']:
            matchedScope1 = carbon.iloc[j]['EMISSIONS_SCOPE_1']
            matchedScope2 = carbon.iloc[j]['EMISSIONS_SCOPE_2']
            matchedRevenue = carbon.iloc[j]['REVENUE_USD'] 
    scope1.append(matchedScope1)
    scope2.append(matchedScope2)
    revenue.append(matchedRevenue)

benchmarkHoldings['scope1'] = scope1
benchmarkHoldings['scope2'] = scope2
benchmarkHoldings['revenue'] = revenue
#print(benchmarkHoldings)
benchmarkWACI = 0
C1benchmarkWACI = 0
C2benchmarkWACI = 0
C3benchmarkWACI = 0
for i in range(len(benchmarkHoldings)):
    if benchmarkHoldings.iloc[i]['scope1'] != 0 and benchmarkHoldings.iloc[i]['scope2'] != 0 and benchmarkHoldings.iloc[i]['revenue'] != 0:
        benchmarkWACI += (benchmarkHoldings.iloc[i]['IndexWeight'] * (benchmarkHoldings.iloc[i]['scope1']*benchmarkHoldings.iloc[i]['scope2']/benchmarkHoldings.iloc[i]['revenue']))
        if benchmarkHoldings.iloc[i]['category'] == 1:
            C1benchmarkWACI += (benchmarkHoldings.iloc[i]['IndexWeight'] * (benchmarkHoldings.iloc[i]['scope1']*benchmarkHoldings.iloc[i]['scope2']/benchmarkHoldings.iloc[i]['revenue']))
        if benchmarkHoldings.iloc[i]['category'] == 2:
            C2benchmarkWACI += (benchmarkHoldings.iloc[i]['IndexWeight'] * (benchmarkHoldings.iloc[i]['scope1']*benchmarkHoldings.iloc[i]['scope2']/benchmarkHoldings.iloc[i]['revenue']))
        if benchmarkHoldings.iloc[i]['category'] == 3:
            C3benchmarkWACI += (benchmarkHoldings.iloc[i]['IndexWeight'] * (benchmarkHoldings.iloc[i]['scope1']*benchmarkHoldings.iloc[i]['scope2']/benchmarkHoldings.iloc[i]['revenue']))


print(f'benchmarkWACI: {benchmarkWACI}')
print(f'C1 - benchmarkWACI: {C1benchmarkWACI}, contribution to total is: {C1benchmarkWACI/benchmarkWACI}')
print(f'C2 - benchmarkWACI: {C2benchmarkWACI}, contribution to total is: {C2benchmarkWACI/benchmarkWACI}')
print(f'C3 - benchmarkWACI: {C3benchmarkWACI}, contribution to total is: {C3benchmarkWACI/benchmarkWACI}')

plt.title("BenchmarkHolding - Each Category's Contribution")
categoryGroup = ['C1', 'C2', 'C3']
contributions = [round(C1benchmarkWACI, 2), round(C2benchmarkWACI,2), round(C3benchmarkWACI,2)]
plt.bar(categoryGroup,contributions)
plt.savefig("benchmarkHolding.jpg")
plt.show()
plt.clf()

