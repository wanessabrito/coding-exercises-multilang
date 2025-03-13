# Testando implementar uma busca binária

def binary_search(array, target):
    min = 0  # Início da lista 
    max = len(array) - 1  # Final da lista
    counter = 0  # Nosso contador de tentativas 
    while max >= min:
        guess = int((min + max) / 2)  # Índice no meio do intervalo na nossa lista (array)
        counter += 1 
        if array[guess] == target:  # Se o alvo for encontrado, retorna o índice e o número de tentativas
            return {'result': guess, 'counter': counter}
        elif array[guess] > target:  # Se o alvo for menor que o valor em guess, busca na metade esquerda
            max = guess - 1 
        elif array[guess] < target:  # Se o alvo for maior que o valor em guess, busca na metade direita
            min = guess + 1 
    
    # Se o alvo não for encontrado, retorna -1
    return -1

# Criamos nossa lista com os quadrados de 1 a 9999 e chamamos a função 
array = [x**2 for x in range(1, 10000)]
result = binary_search(array, int(input('Target number: ')))

# Imprime a posição e o número de tentativas, ou informa se o número não foi encontrado
if result != -1:
    print(f"Found at position {result['result']} after {result['counter']} guesses.")
else:
    print("Number is not in the array.")