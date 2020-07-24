import datetime
import os
import csv
from matplotlib import pyplot as plt

class salario():
    def __init__(self):
        self.salario = 0
        self.investimento = ""
        self.quantinvest = 0
        self.contas1 = 0
        self.total = 0
        self.data = datetime.datetime.now()

    def contas(self):
        # Recebe total de contas no mes
        try:
            self.contas1 = int(input("Qual total de contas no mes: "))
        except ValueError:
            print("Valor Invalido, precisa ser um numero")
            self.contas1 = int(input("Qual total de contas no mes: "))
            # Pergunta se ira fazer um investimento ou nao, caso sim, desconta do valor total do salario
        self.investimento = input("Deseja fazer um investimento? (Poupanca, TDI, CDB, etc...) Y para sim N para não: ")
        if self.investimento.lower() == "y":
            try:
                self.quantinvest = int(input("Quanto deseja investir? "))
            except ValueError:
                print("Valor Invalido, precisa ser um numero")
                self.quantinvest = int(input("Quanto deseja investir? "))
        else:
            print("Ok, Nenhum Investimento.")
            # Recebe total do salario do mes
        try:
            self.salario = int(input("Digite seu salario : "))
        except ValueError:
            print("Valor Invalido, precisa ser um numero")
            self.salario = int(input("Digite seu salario : "))

    def gera_rel(self):
        self.total = self.salario - self.quantinvest - self.contas1
        csv_file = "out.csv"
        fieldnames = ['Salario', 'Investimento', 'Contas', 'Data', 'Total']
        if os.stat(csv_file).st_size == 0:
            with open(csv_file, "w", newline='') as f:
                data = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
                data.writeheader()
                data.writerow({'Salario': self.salario, 'Investimento': self.quantinvest, 'Contas': self.contas1, "Data": self.data,
                               "Total": self.total})
        else:
            with open(csv_file, "a+") as f:
                data = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
                data.writerow({'Salario': self.salario, 'Investimento': self.quantinvest, 'Contas': self.contas1, "Data": self.data,
                               "Total": self.total})
        f.close()

        if self.total < 0:
            print("Voce esta em debito de "+ str(self.total))
        else:
            print(self.total)


    def gera_grafico(self):


a = salario()
a.contas()
a.gera_rel()