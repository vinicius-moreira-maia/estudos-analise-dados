from scipy import stats
from sys import exit

# dados da amostra
amostra = [12, 15, 14, 10, 13, 12, 16]

# H0 é a hipótese de que a média da amostra é estatisticamente igual a média populacional (ou o valor que se julga correto)
media_hipotese = 13

# o método retorna o valor T e o p-valor
t_stat, p_valor = stats.ttest_1samp(amostra, media_hipotese)

print(f"T: {t_stat}")
print(f"p-valor: {p_valor}")

# exit()

# decisão (assumindo 5% de chance de cometer erro)
alpha = 0.05
if p_valor < alpha:
    print("Rejeita H0: diferença estatisticamente significativa")
else:
    print("Não rejeita H0: não há evidência suficiente")