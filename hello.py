#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR #Linux
    set LANG=pt_BR # Windows

Execução:

    python3 hello.py
    ou 
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Jade Cavalcanti"
__license__ = "Unlicense"

import os 

# Dunder - substitui a necessidade de falar __ ; significa que e um identificador com 2 _
# Este programa imprime "Hello, World!"

current_language = os.getenv("LANG", "en_US")[:5]
#snake case - quando as palavras são todas escritas em letras minúsculas e separadas por _

#Pascal Case - ex: CurrentLanguage

msg = { 
    "pt_BR": "Olá, Mundo!",
    "en_US": "Hello, World!",
    "es_SP": "Hola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language])