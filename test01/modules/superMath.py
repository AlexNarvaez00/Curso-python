def sumAll(*numbers):
    acum = 0
    for number in numbers:
        acum+=number
    return acum

def restAll(*numbers):
    acum = 0
    for number in numbers:
        acum-=number
    return acum