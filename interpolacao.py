
import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)
    
filename = arguments[0] #emails.txt
templatname = arguments[1] #email_tmpl.txt

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatname)


for line in open(filepath):
    name, email = line.split(",")  

    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read()
        % {
             "nome": name, 
             "produto": "caneta",
             "texto": "Escrever muito bem",
             "link": "https://canetaslegais.com", 
             "quantidade": 1, 
             "preco": 50.5,
        }
    )

print("-" * 50)
