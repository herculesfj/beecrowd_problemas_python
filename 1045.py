# Leitura dos três valores A, B e C
A, B, C = sorted(map(float, input().split()), reverse=True)

# Verificação das condições
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("TRIANGULO ISOSCELES")