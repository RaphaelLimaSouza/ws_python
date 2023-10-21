# Importando os módulos necessários
import random # Para escolher caracteres aleatórios
import string # Para acessar os conjuntos de caracteres

# Definindo o tamanho da senha (número de caracteres)
tamanho = 10

# Definindo os caracteres que podem compor a senha
# Podemos usar letras maiúsculas, minúsculas, números e símbolos especiais
caracteres = string.ascii_letters + string.digits + string.punctuation

# Criando uma variável vazia para armazenar a senha
senha = ""

# Usando um loop for para gerar a senha
# A cada iteração, escolhemos um caractere aleatório dos caracteres e adicionamos à senha
for i in range(tamanho):
    senha += random.choice(caracteres)

# Imprimindo a senha gerada
print("A senha gerada é:", senha)
