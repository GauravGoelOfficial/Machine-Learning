L = []
n = int(input("Enter no. of elements you want to insert in a list = "))
for i in range(1, n + 1):
    print("Enter element =", i)
    ins = int(input())
    L.append(ins)
print("Input List", L)
large = L[0]
small = L[0]
for i in range(1, n):
    if large < L[i]:
        large = L[i]
    if small > L[i]:
        small = L[i]
print("Largest =", large)
print("Smallest =", small)
