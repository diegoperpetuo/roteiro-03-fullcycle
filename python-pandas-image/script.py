import pandas as pd
data = {
    "Nome": ["Ana", "Bruno", "Cartlos"],
    "Idade": [28, 34, 29],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}
df = pd.DataFrame(data)

print ("DataFrame criado no contêiner:")
print (df)