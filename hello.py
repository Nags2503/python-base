

"""Hello World Multi Linguas.

Dependendo da lingua configurada no 
ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel configuarada ex:

    $env:LANG = "pt_BR"
    
execução:

    python hello.py

"""

import os

__version__ = "0.0.1"
__autor__ = "Noemi Sandes"
__license__ = "unlicense"

import os

# Dunder

# Este programa imprime Hello World

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"
    
print(msg)
