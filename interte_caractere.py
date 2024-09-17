# Função para inverter os caracteres de uma string sem usar funções prontas
def inverter_string(texto):
    invertida = ""
    # Percorre a string de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

# Entrada do usuário (pode ser definida diretamente também)
texto_original = input("Informe uma string para inverter: ")

# Chama a função e exibe a string invertida
texto_invertido = inverter_string(texto_original)
print(f"String invertida: {texto_invertido}")
