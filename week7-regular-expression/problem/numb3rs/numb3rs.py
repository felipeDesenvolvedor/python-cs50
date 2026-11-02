# 
# Um uso comum da notação decimal pontuada é na tecnologia da informação, onde é um método de escrever números em números decimais agrupados em octetos . [ 2 ] Em redes de computadores , os endereços do Protocolo de Internet versão 4 (IPv4) são comumente escritos usando a notação pontilhada de quatro inteiros decimais, variando de 0 a 255 cada.

import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
   try:
      octet = r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
      pattern = rf"^(?:{octet}\.){{3}}{octet}$"   
      if re.search(pattern, ip):
          return True
      else:
          return False
   except Exception as e:
       sys.exit("error", e) 

if __name__ == "__main__":
    main()