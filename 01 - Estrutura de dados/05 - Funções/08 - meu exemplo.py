def capturar_nome():
    nome = input("Digite seu nome: ")  # Captura o valor
    return nome  # Retorna o valor

nome_armazenado = capturar_nome()  # Armazena o valor retornado
print(f"Nome armazenado: {nome_armazenado}")

print(nome_armazenado)