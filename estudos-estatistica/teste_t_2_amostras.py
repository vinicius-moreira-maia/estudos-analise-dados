from scipy import stats
from sys import exit

amostra1 = [23, 20, 22, 21, 24]
amostra2 = [30, 29, 31, 28, 32]

# Teste t para amostras independentes (Welch, ou seja, assume-se que as variâncias são diferentes)
t_stat, p_valor = stats.ttest_ind(amostra1, amostra2, equal_var=False)

print(f"T: {t_stat}")
print(f"p-valor: {p_valor}")

# exit()

# decisão (assumindo 5% de chance de cometer erro)
alpha = 0.05
if p_valor < alpha:
    print("Rejeita H0: diferença estatisticamente significativa")
else:
    print("Não rejeita H0: não há evidência suficiente")