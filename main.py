url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

#Sanitzazção da URL
url = url.strip()
#Validação da URL
if url == "":
    raise ValueError("A url está vazia")

#Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]


url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_paramentro = url_parametros.find(parametro_busca)
indice_valor = indice_paramentro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
valor = url_parametros[indice_valor:]
if indice_e_comercial ==-1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)


