#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    python3 hello.py
    ou ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Jade Cavalcanti"
__license__ = "Unlicense"

import os 

# Dunder - substitui a necessidade de falar __ ; significa que e um identificador com 2 _
# Este programa imprime "Hello, World!"

current_language = os.getenv("LANG", "en_US")[:5]
#snake case - quando as palavras são todas escritas em letras minúsculas e separadas por _

#Pascal Case - ex: CurrentLanguage

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)