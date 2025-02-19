# Leitura das notas
N1, N2, N3, N4 = map(float, input().split())

# Cálculo da média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

# Impressão da média inicial
print(f"Media: {media:.1f}")

# Verificação da situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Leitura da nota do exame
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # Cálculo da média final
    media_final = (media + nota_exame) / 2
    
    # Verificação da aprovação após o exame
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    # Impressão da média final
    print(f"Media final: {media_final:.1f}")
