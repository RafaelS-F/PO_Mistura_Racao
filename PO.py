import pulp

# 1. Criação do Problema (Minimização)
prob = pulp.LpProblem("Problema_da_Racao", pulp.LpMinimize)

# 2. Variáveis de Decisão (x1 a x4, limite inferior 0)
# Representam a proporção de cada ingrediente (0 a 1)
milho = pulp.LpVariable("Milho", lowBound=0)
soja = pulp.LpVariable("Soja", lowBound=0)
calcario = pulp.LpVariable("Calcario", lowBound=0)
oleo = pulp.LpVariable("Oleo", lowBound=0)

# 3. Função Objetivo (Custos)
# Custo por kg de cada ingrediente
prob += 1.20*milho + 2.80*soja + 0.15*calcario + 5.50*oleo, "Custo_Total"

# 4. Restrições

# Restrição de Balanço (Soma das proporções = 1)
prob += milho + soja + calcario + oleo == 1, "Total_100_Porcento"

# Restrição de Proteína (Mínimo 20%)
prob += 0.085*milho + 0.450*soja + 0.0*calcario + 0.0*oleo >= 0.20, "Min_Proteina"

# Restrição de Energia (Mínimo 3000 Kcal)
prob += 3390*milho + 2240*soja + 0*calcario + 8800*oleo >= 3000, "Min_Energia"

# Restrição de Cálcio (Mínimo 0.9%)
prob += 0.0002*milho + 0.003*soja + 0.380*calcario + 0.0*oleo >= 0.009, "Min_Calcio"

# 5. Resolver o modelo
prob.solve()

# 6. Exibir Resultados
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Custo Mínimo por Kg: R$ {pulp.value(prob.objective):.4f}")
print("\nComposição Otimizada (por kg):")
vars_list = [milho, soja, calcario, oleo]
for v in vars_list:
    print(f"{v.name}: {v.varValue:.4f} kg ({(v.varValue*100):.2f}%)")

# Verificação das propriedades finais
prot_final = 0.085*milho.varValue + 0.450*soja.varValue
energ_final = 3390*milho.varValue + 2240*soja.varValue + 8800*oleo.varValue
calc_final = 0.0002*milho.varValue + 0.003*soja.varValue + 0.380*calcario.varValue

print("\nPropriedades Nutricionais Resultantes:")
print(f"Proteína: {prot_final*100:.2f}% (Mín: 20%)")
print(f"Energia: {energ_final:.2f} Kcal (Mín: 3000)")
print(f"Cálcio: {calc_final*100:.2f}% (Mín: 0.9%)")

# Análise de Sensibilidade (Preço Sombra)
print("\n--- Análise de Sensibilidade (Preço Sombra) ---")
for name, c in prob.constraints.items():
    print(f"Restrição {name}: Shadow Price = {c.pi:.4f}")