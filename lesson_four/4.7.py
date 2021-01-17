

def fact_gen(numbur):
        f_num = 1
        if numbur == 0:
            yield f'{numbur}! = 1'
        for i in range(1, numbur + 1):
            f_num *= 1
            yield f'{i}! = {f_num}'

for el in fact_gen(int(input('Factoril numbur: '))):
        print(el)
