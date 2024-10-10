''' 6.  Lists, tuples, and dictionaries are just some of Python's built-in containers.
        Do some research on Python's sets (a type of container).
        When would you use a set?    '''

#   Sets in Python are unordered collections of unique elements. They are very useful when you need to ensure that there are no duplicates in a collection of items and when you need to perform mathematical operations such as union, intersection, and difference.
#   Os conjuntos (ou sets) em Python são coleções não ordenadas de elementos únicos. Eles são muito úteis quando você precisa garantir que não há duplicados em uma coleção de itens e quando você precisa realizar operações matemáticas como união, interseção e diferença.

#   WHEN TO USE SETS?
#   QUANDO USAR CONJUNTOS?

#       1.  Remove duplicates: If you have a list with duplicates and want to create a new list without duplicates, you can convert the list to a set and then back to a list.
#       1.  Remover duplicados: Se você tem uma lista com duplicados e quer criar uma nova lista sem duplicados, pode converter a lista em um conjunto e depois de volta para uma lista.
lista = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto = set(lista)
lista_sem_duplicados = list(conjunto)
print(lista_sem_duplicados) #  Saída: [1, 2, 3, 4, 5]

#       2.  Mathematical operations: Sets are ideal for performing mathematical operations such as union, intersection and difference.
#       2.  Operações matemáticas: Conjuntos são ideais para realizar operações matemáticas como união, interseção e diferença.
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)  #   {1, 2, 3, 4, 5}
intersecao = conjunto1.intersection(conjunto2)  #   {3}
diferenca = conjunto1.difference(conjunto2) #   {1, 2}

#       3.  Check Membership: You can quickly check whether an item is present in a set.
#       3.  Verificar a pertinência: Você pode verificar rapidamente se um item está presente em um conjunto.
conjunto = {1, 2, 3, 4, 5}
print(3 in conjunto)    #   Saída: True
print(6 in conjunto)    #   Saída: False

#       4.  Efficiency: Sets are implemented as hash tables, which makes search operations very fast.
#       4.  Eficiência: Conjuntos são implementados como tabelas de hash, o que torna as operações de busca muito rápidas.