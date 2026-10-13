from datetimeseasons import DateTimeSeasons

""" 
1 OK - Considerando que um ano tem 365 dias, existem 365 × 24 ×60 = 525,600
minutos nesse mesmo ano (porque há 24 horas em um dia e 60 minutos em uma hora).
2 OK - Ano Bissexto: 366 dias, de acordo com o calendário gregoriano , já que alguns deles podem ter 1 × 24 ×60 = 1,440
minutos adicionais.
3 OK - Quantos anos minutos se passaram desde o meu nascimento ? Isso depende de quantos anos bissextos ocorreram desde entao, 
Existe um algoritmo para isso
4 OK - Em um arquivo chamado `datetime.py` seasons.py, implemente um programa que solicite ao usuário sua data de nascimento no YYYY-MM-DD formato `00:00:00` imprima a idade do usuário em minutos, arredondada para o inteiro mais próximo,
5 - imprima a idade do usuário usando palavras em inglês em vez de numerais, assim como na música do musical ` Rent` , sem and palavras entre os dígitos.
6 - Como o usuário pode não saber a hora exata em que nasceu, assuma, por simplicidade, que ele nasceu à meia-noite (ou seja, 00:00:00) daquela data.
7 - E assuma também que a hora atual é meia-noite.
8 OK - Saia do programa sys.exitse o usuário não inserir uma data no YYYY-MM-DD formato correto.
9 - Certifique-se de que seu programa não gere nenhuma exceção. """

def main():
    dataBirth = input("Date of birth: ")
    print(DateTimeSeasons(dataBirth).get_date_born_minutes())
    print(DateTimeSeasons(dataBirth).get_date_born_minutes_in_words())
        
if __name__ == "__main__":
    main()