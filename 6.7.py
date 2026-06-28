#Faca um programa que leia uma expressao com parenteses
#usando pilhas verifique se os parateses foram aberto e fechados na ordem correta
#Voce pode adicionar elementos a pilha sempre que encontrar abre parenteses
# e desimpilhalho a cada fecha parenteses.Ao desempilhar verifique  se o topo da pilha
#eh um abre parenteses. Se a expressao estiver correta sua pilha estara vazia no final

# 🥞 Estrutura LIFO (Last In, First Out)

# 1. Criar a pilha e o sinalizador
pilha = []
correta = True

# 2. Usuário digita a expressão
expressao = input("Digite a expressão matemática: ")

# 3. Percorrer a expressão
for i in range(len(expressao)):
    # Se for '(', empilhamos
    if expressao[i] == '(':
        pilha.append('(')
        
    # Se for ')', precisamos desempilhar com segurança
    elif expressao[i] == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            # Encontrou ')' mas a pilha estava vazia!
            correta = False
            break

# 4. Verificação final
# Como você bem disse, a pilha tem que estar vazia no final!
if correta and len(pilha) == 0:
    print("Parabéns! A expressão está correta.")
else:
    print("Erro! Os parênteses não foram fechados corretamente.")