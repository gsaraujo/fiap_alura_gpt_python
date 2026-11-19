import tiktoken


modelo = "o200k_base"
codificador = tiktoken.get_encoding(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo do modelo gpt-6.2-astra: {modelo} é de ${(len(lista_tokens)/1000000)*8}")


modelo = "o200k_base"
codificador = tiktoken.get_encoding(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo do modelo gpt-6-astra: {modelo} é de ${(len(lista_tokens)/1000000)*10}")

print(f"O custo do Astra6 é {10/8} maior que o Astra6.2")
