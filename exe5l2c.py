total_liquido = 0

while True:
    salario_bruto = float(input("Digite o salário bruto (0 para sair): "))
    if salario_bruto == 0:
        break
    horas_trabalhadas = float(input("Digite as horas trabalhadas no mês: "))

    if salario_bruto < 800:
        desconto = 0
    elif salario_bruto <= 1600:
        desconto = salario_bruto * 0.08 + salario_bruto * 0.05
    else:
        desconto = salario_bruto * 0.15 + salario_bruto * 0.07

    adicional = 0
    if horas_trabalhadas > 160:
        valor_hora = salario_bruto / 160
        horas_extras = horas_trabalhadas - 160
        adicional = horas_extras * valor_hora * 0.5

    salario_liquido = salario_bruto - desconto + adicional
    total_liquido += salario_liquido

    print(f"Salário líquido: R$ {salario_liquido:.2f}")

print(f"Total geral dos salários líquidos: R$ {total_liquido:.2f}")
