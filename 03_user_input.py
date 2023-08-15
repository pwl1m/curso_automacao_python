nome=input('entre com seu nome: ')
print(nome)

# fazendo matematica com a entrada do usuario
size_input=input('qual tamanho da sua casa (em pe quadrado): ')
# convertendo para numero o size_input

pe_quadrado=int(size_input)

metros_quadrados=pe_quadrado / 10.8

print(f'{pe_quadrado} pe_quadrado é {metros_quadrados:.2f} metros quadrados.')
