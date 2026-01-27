
numbers = [1, 2, 3, 4, 5]
print("Lista initiala: ", numbers)


numbers.extend([6,7])
print("Lista dupa adaugarea a doua numere: ",numbers)


numbers.pop(0)
numbers.pop(3)
print("Stergerea dupa index: ",numbers)


numbers.remove(7)
print("Stergerea unui element: ",numbers)
