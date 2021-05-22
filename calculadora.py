from time import sleep
#Só para deixar o código mais humano
Operador=input('Qual o nome do operador:')
print('Bom dia {}'.format(Operador))

moeda = 0
while moeda != 7:
    print('''Qual moeda deseja converter:
    [1] Real (R$) para Dolar (USD)
    [2] Real (R$) para Euro (EUR)
    [3] Real (R$) para Peso argentino (ARS)
    [4] Dolar (USD) para Real (R$)
    [5] Euro (EUR) para Real (R$)
    [6] Peso argentino (ARS) para Real (R$)
    [7] SAIR''')
    moeda = int(input('Selecione a Moeda:'))

    if moeda == 1:
        #rd é onde faz a conversão e rdp onde acrescenta os 10% de taxas
        dolar = float(input('Digite o quantidade de Dolar a ser comprado e pago com Reais:'))
        rd = (5.26 * dolar)
        rdp = (rd * 0.1) + rd
        print('valor a ser pago em Reais é de R${:.2f} para receber US${:.2f}'.format(rdp,dolar))
    elif moeda == 2:
        # re é onde faz a conversão e rep onde acrescenta os 10% de taxas
        euro = float(input('Digite o quantidade de Euro a ser comprado e pago com Reais:'))
        re = (6.43 * euro)
        rep = (re * 0.1) + re
        print('valor a ser pago em Reais é de R${:.2f} para receber €{:.2f}'.format(rep,euro))
    elif moeda == 3:
        # rp é onde faz a conversão e rpp onde acrescenta os 10% de taxas
        peso = float(input('Digite o quantidade de Peso argentino a ser comprado e pago com Reais:'))
        rp = (0.056 * peso)
        rpp = (rp * 0.1) + rp
        print('valor a ser pago em Reais é de R${:.2f} para receber ${:.2f}'.format(rpp,peso))
    elif moeda == 4:
        # ddr é onde faz a conversão e ddrt onde remove os 10% de taxas
        ddolar = float(input('Digite o quantidade de Reais a ser comprado e pago com Dolar:'))
        ddr = (ddolar / 5.26)
        ddrt = ddr - (ddr/10)
        print('valor a ser pago em Dolar é de US${:.2f} para receber R${:.2f}'.format(ddrt,ddolar))
    elif moeda == 5:
        # eer é onde faz a conversão e eert onde remove os 10% de taxas
        eeuro = float(input('Digite o quantidade de Reais a ser comprado e pago com Euro:'))
        eer = (eeuro / 6.43)
        eert = eer - (eer / 10)
        print('valor a ser pago em Euro é de €{:.2f} para receber R${:.2f}'.format(eert, eeuro))
    elif moeda == 6:
        # ppr é onde faz a conversão e pprt onde remove os 10% de taxas
        ppeso = float(input('Digite o quantidade de Reais a ser comprado e pago com Peso argentino:'))
        ppr = (ppeso / 0.056)
        pprt = ppr - (ppr / 10)
        print('valor a ser pago em Peso argentino é de ${:.2f} para receber R${:.2f}'.format(pprt, ppeso))
    elif moeda == 7:
        print('finalizando....')
    else:
        print('Moeda inválida, tente novamente')
    print('=-=' * 20)
    sleep(2)
print('Fim da transação!')

