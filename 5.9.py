def divisao(n1, n2):
  if n2 == 0:
    print('Nao pode dividir por 0')

  q = 0
  while n1 >= n2:
    n1 -= n2
    q += 1
  resto = 0

  if n1 != 0:
    resto = n1
  return q, resto
def main():
  n1 = int(input("Escreva um numero "))
  n2 = int(input("Escreva um numero  "))

  q, resto = divisao(n1,n2)

  print(f'{n1} / {n2} =  {q} com resto {resto}')


if __name__ == "__main__":
  main()