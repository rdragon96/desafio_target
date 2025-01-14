#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
# que cada estado teve dentro do valor total mensal da distribuidora.  


faturamentos = {'SP':67836.43,'RJ':36678.66,'MG':29229.88,'ES':27165.48,'OUTROS':19849.53}

faturamento_total = sum(faturamentos.values())
print(f"Faturamento total: R${faturamento_total:.2f}")

for estado, faturamento in faturamentos.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"Percentual de {estado}: {percentual:.2f}%")