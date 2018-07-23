N = 100000
n2 = 1000000
n3 = 10000000
s = 21500
# y = []
# y2 = []
# y3 = []
# for x in range(s + 700, s + N, N / 700):
#     y.append(x)
#     print()
#
# print(y)
#
# for x in range(s + 500, s + n2, n2 / 700):
#     y2.append(x)
# print(y2)
#
# for x in range(s + 500, s + n3, n3 / 700):
#     y3.append(x)
# print(y3)
#
# print("length", len(y))
# print("length", len(y2))
# print("length", len(y3))
# y4 = []
# y5 = []
# for x in range(100, s, s / 150):
#     y4.append(x)
# print("length", len(y4))
#
# for x in range(N + 100, N + s, s / 150):
#     y5.append(x)
#
# print("length", len(y5))
# y6 = []
# for x in range(n2 + 100, n2 + s, s / 150):
#     y6.append(x)
#
# print("length", len(y6))
#
# y7 = []
# for x in range(n2 + 100, n2 + s, s / 150):
#     y7.append(x)
#
# print("length", len(y7))

elementArray = []
# for x in range(100, s, s / 150):
#     elementArray.append(x)
# for x in range(s + 700, s + N, N / 700):
#     elementArray.append(x)
# for x in range(N + 100, N + s, s / 150):
#     elementArray.append(x)

elementArray1 = []
elementArray2 = []
elementArray3 = []

i = 0
while (i < 1000):
    if (i < 150):
        for x in range(100, s, s / 150):
            elementArray1.append(x)
            i += 1
    elif (i < 700 and i > 150):
        for x in range(s + 700, s + N, N / 700):
            elementArray2.append(x)
            i += 1
    else:
        for x in range(N + 100, N + s, s / 150):
            elementArray3.append(x)
            i += 1


print(len(elementArray1))
print(len(elementArray2))
print(len(elementArray3))
print(elementArray3)
print(elementArray1)
print(elementArray2)