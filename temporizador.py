import time

# Objetivo contar de trás para frentes
# O oposto do cronômetro

# Valor inserido pelo usuário em segundos
t = input("Digite o tempo ( em segundos ): ")

# Verificar se o valor digitado é número ( Segundos )
if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()
    

# Por exemplo 120 / 60
# 150 / 60 = 2 |Resto = 30

# Function divmod- basicamente ela tem dois retorno o coeficiente e o resto, como estamos passando o coeficiente o digito do usuário
# Ele ira calcular o valor para minutos se o valor for ter resto vai garvar na variavel second

#while t != 0: ---- Opcional e válido
while t: 
    minutes, second = divmod(t, 60)
    # 0=Considerar 0 a esquerda caso seja um valor unitário | 2=2 digitos| d=inteiro  
    timer = "{:02d}:{:02d}".format(minutes, second)
    print(timer, end="\r") # Reescrever
    time.sleep(1) # Dar uma lentidão no temporizador em segundos
    t = t - 1
    
print("TEMPO ACABOU !!!")