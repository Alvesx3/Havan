from time import sleep
from datetime import date
import sqlite3

conn = sqlite3.connect("BancoHavan.db")

cursor = conn.cursor()

# cria uma tabela, Lembre de comentar após a primeira vez para evitar mais Bugs =D
cursor.execute("""CREATE TABLE mundomoeda
                (operador text, data real, cliente text,
                 moeda_de_origem text, moeda_de_destino text, valor_orginal text,
                 valor_convertido text, taxa_cobrada text)
                 """)
#primeiras linhas da tabela
d = date.today()
Operador=input('Qual o nome do operador:')
print('Bom dia {}, tenha um bom trabalho hoje {}'.format(Operador,d))
base = 0
while base != 3:
    print('''Qual função deseja:
        [1] Conversão de moedas
        [2] Informações de transações
        [3] SAIR''')
    base = int(input('Selecione a Moeda:'))
    if base == 1:
        cliente = input('Nome completo do Cliente:')
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
                taxad = rdp - rd
                print('valor a ser pago em Reais é de R${:.2f} para receber US${:.2f}'.format(rdp,dolar))
                # insere dados
                cursor.execute("INSERT INTO mundomoeda VALUES ('"+Operador+"', '"+str(d)+"', '"+cliente+"', 'Real', 'Dolar', '"+str(dolar)+"', '"+str(rd)+"', '"+str(taxad)+"')")

                # salva dados no banco
                conn.commit()
            elif moeda == 2:
            # re é onde faz a conversão e rep onde acrescenta os 10% de taxas
                euro = float(input('Digite o quantidade de Euro a ser comprado e pago com Reais:'))
                re = (6.43 * euro)
                rep = (re * 0.1) + re
                taxae = rep - re
                print('valor a ser pago em Reais é de R${:.2f} para receber €{:.2f}'.format(rep,euro))
            # insere dados
                cursor.execute("INSERT INTO mundomoeda VALUES ('"+Operador+"', '"+str(d)+"', '"+cliente+"', 'Real', 'Euro', '"+ str(euro)+"', '"+str(re)+"', '"+str(taxae)+"')")

            # salva dados no banco
                conn.commit()
            elif moeda == 3:
            # rp é onde faz a conversão e rpp onde acrescenta os 10% de taxas
                peso = float(input('Digite o quantidade de Peso argentino a ser comprado e pago com Reais:'))
                rp = (0.056 * peso)
                rpp = (rp * 0.1) + rp
                taxap = rpp - rp
                print('valor a ser pago em Reais é de R${:.2f} para receber ${:.2f}'.format(rpp,peso))
            # insere dados
                cursor.execute("INSERT INTO mundomoeda VALUES ('"+Operador+"', '"+str(d)+ "', '"+cliente+"', 'Real', 'Peso', '"+str(peso)+"', '"+str(rp)+"', '"+str(taxap)+"')")

            # salva dados no banco
                conn.commit()
            elif moeda == 4:
            # ddr é onde faz a conversão e ddrt onde remove os 10% de taxas
                ddolar = float(input('Digite o quantidade de Reais a ser comprado e pago com Dolar:'))
                ddr = (ddolar / 5.26)
                ddrt = ddr - (ddr/10)
                taxadd = ddr - ddrt
                print('valor a ser pago em Dolar é de US${:.2f} para receber R${:.2f}'.format(ddrt,ddolar))
            # insere alguns dados
                cursor.execute("INSERT INTO mundomoeda VALUES ('"+Operador+"', '"+str(d) + "', '"+cliente+"', 'Dolar', 'Real', '"+str(ddolar)+"', '"+str(ddr)+"', '"+str(taxadd)+"')")

            # salva dados no banco
                conn.commit()
            elif moeda == 5:
            # eer é onde faz a conversão e eert onde remove os 10% de taxas
                eeuro = float(input('Digite o quantidade de Reais a ser comprado e pago com Euro:'))
                eer = (eeuro / 6.43)
                eert = eer - (eer / 10)
                taxaee = eer - eert
                print('valor a ser pago em Euro é de €{:.2f} para receber R${:.2f}'.format(eert, eeuro))
            # insere dados
                cursor.execute("INSERT INTO mundomoeda VALUES ('"+Operador+"', '"+str(d)+"', '"+cliente+"', 'Euro', 'Real', '"+str(eeuro)+"', '"+str(eer)+"', '"+str(taxaee)+"')")

            # salva dados no banco
                conn.commit()
            elif moeda == 6:
            # ppr é onde faz a conversão e pprt onde remove os 10% de taxas
                ppeso = float(input('Digite o quantidade de Reais a ser comprado e pago com Peso argentino:'))
                ppr = (ppeso / 0.056)
                pprt = ppr - (ppr / 10)
                taxapp = ppr - pprt
                print('valor a ser pago em Peso argentino é de ${:.2f} para receber R${:.2f}'.format(pprt, ppeso))
            # insere dados
                cursor.execute("INSERT INTO mundomoeda VALUES ('"+Operador+ "', '"+str(d)+"', '"+cliente+"', 'Real', 'Dolar', '"+str(ppeso)+"', '"+str(ppr)+"', '"+str(taxapp)+"')")

            # salva dados no banco
                conn.commit()
            elif moeda == 7:
                print('finalizando....')
            else:
                print('Moeda inválida, tente novamente')
            print('=-=' * 20)
            sleep(2)
            print('Fim da transação!')
    if base == 2:
        select = 0
        while select != 3:
            print('''Qual moeda deseja converter:
            [1] Data 
            [2] Nome do Cliente 
            [3] SAIR''')
            select = int(input('Selecione o tipo de Pesquisa:'))

            if select == 1:
                #Procura pela data
                dia = input('Qual o dia deseja pesquisa (Ex: 2021/05/22):')
                sql = "SELECT * FROM mundomoeda Where "+dia+""
                cursor.execute(sql)
                print(cursor.fetchall())


            elif select == 2:
                #Procura na por nome
                nome = input('Qual o nome completo do Cliente:')
                sql = "SELECT * FROM mundomoeda Where cliente LIKE '%"+nome+"%'"
                cursor.execute(sql)
                print(cursor.fetchall())
            elif select == 3:
                print('Saindo da Pesquisa....')
            else:
                print('Pesquisa inválida, tente novamente')
    elif base == 3:
        print('finalizando....')
    else:
        print('=-=' * 20)
        print('opção inválida, tente novamente')
    print('=-=' * 20)
    sleep(1)
print('Tenha um bom final de dia {}!'.format(Operador))


