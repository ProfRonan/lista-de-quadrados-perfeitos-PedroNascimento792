def calculate_squares(número):
    squares = []
    for i in range(1, número+1):
        squares.append(str(i*i))
    return squares

num = int(input("Digite um número: "))
result = calculate_squares(num)
for square in result:
    print(square)