"""
Podemos aprimorar a funcionalidade do nosso programa. No entanto, precisamos expandir nosso vocabulário em relação à validação. Acontece que, no mundo das expressões regulares, existem certos símbolos que nos permitem identificar padrões. Até agora, estávamos verificando apenas trechos de texto específicos, como @. Acontece que muitos símbolos especiais podem ser passados ​​para o interpretador com o objetivo de realizar a validação. Uma lista não exaustiva desses padrões é a seguinte:

.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions

^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string

[]    set of characters
[^]   complementing the set

[^@]+ significa qualquer caractere, exceto um @.

# Observe que [a-zA-Z0-9_] a validação indica que os caracteres devem estar entre a e z, entre A e Z, entre 0 e 9 e, podendo incluir um _ símbolo. Ao testar a entrada, você verá que muitos erros potenciais do usuário podem ser identificados.

d    decimal digit
D    not a decimal digit
s    whitespace characters
S    not a whitespace character
w    word character, as well as numbers and the underscore
W    not a word character

A | B     either A or B
(...)   a group
(?:...) non-capturing version

"""
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+(\.)?\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
