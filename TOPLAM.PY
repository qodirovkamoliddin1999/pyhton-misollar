# a= input(" matin kiriting: ")
# h= a.split()
# r = int(input("nechta so'zni chiqarmoqchiszi: "))
# j = h[r:4]
# print(j)

a= input(" matin kiriting: " )
p = a.split()
n = int(input("nechtadan kam harfli so'zlarni chiqarmoqchisiz "))
for i in p:
    if len(i)<n:
        print(i)