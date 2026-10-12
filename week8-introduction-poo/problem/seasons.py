import re
import sys
import datetime

""" 
1 OK - Considerando que um ano tem 365 dias, existem 365 × 24 ×60 = 525,600
minutos nesse mesmo ano (porque há 24 horas em um dia e 60 minutos em uma hora). 
2 OK - Ano Bissexto: 366 dias, de acordo com o calendário gregoriano , já que alguns deles podem ter 1 × 24 ×60 = 1,440
minutos adicionais. 
3 OK - Quantos anos minutos se passaram desde o meu nascimento ? Isso depende de quantos anos bissextos ocorreram desde entao, 
Existe um algoritmo para isso
4 OK - Em um arquivo chamado `datetime.py` seasons.py, implemente um programa que solicite ao usuário sua data de nascimento no YYYY-MM-DD formato `00:00:00` e, em seguida, imprima a idade do usuário em minutos, arredondada para o inteiro mais próximo, usando palavras em inglês em vez de numerais, assim como na música do musical ` Rent` , sem andpalavras entre os dígitos. 
5 - Como o usuário pode não saber a hora exata em que nasceu, assuma, por simplicidade, que ele nasceu à meia-noite (ou seja, 00:00:00) daquela data. 
6 - E assuma também que a hora atual é meia-noite. 
7 OK - Saia do programa sys.exitse o usuário não inserir uma data no YYYY-MM-DD formato correto. 
8 - Certifique-se de que seu programa não gere nenhuma exceção. """

def main():
    get_date_born()
    
def get_date_born():
    dataBirth = input("Date of birth: ")
    dateNow = datetime.date.today()

    if re.search(r"^\d{4}-\d{2}-\d{2}$", dataBirth):
       dateDiff = dateNow - datetime.date(int(dataBirth.split("-")[0]), int(dataBirth.split("-")[1]), int(dataBirth.split("-")[2]))
       dateBirthInMinutes = dateDiff.days * 24 * 60
       print("dateBirthInMinutes:", dateBirthInMinutes)
    else:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")
        
if __name__ == "__main__":
    main()