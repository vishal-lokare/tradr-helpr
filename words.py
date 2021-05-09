import pandas as pd

def main(text):
  data = pd.read_csv('convertcsv.csv')
  symbols = list(data['SYMBOL'].dropna())
  comp = list(data['NAME'].dropna())
  comps = []
  for i in range(len(comp)):
    comps.append(comp[i].upper().split())
  imp = []
  for i in text.upper().split():
    for j in range(len(comp)):
      if i in comps[j] and i not in ['AND','OR','THE','BANK','ECONOMIC','ZONE','LIMITED','ENTERPRISES']:imp.append(symbols[j])
  return list(set(imp))
