import requests,os
os.system('cls' if os.name == 'nt' else 'clear')
cep = input("Insira o CEP: ")
req = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
print(f'''
\033[1;33m	
CEP: {cep}
Rua: {req['logradouro']}
Complemento: {req['complemento']}
Bairro: {req['bairro']}
Localidade: {req['localidade']}
Estado: {req['uf']}
Ibge: {req['ibge']}
Gia: {req['gia']}
DDD: {req['ddd']}
Siafi: {req['siafi']}
''')