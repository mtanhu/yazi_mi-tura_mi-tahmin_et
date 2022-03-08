#coded_by_murattanhu\Terme

from random import randint

yaziTura = input('Yazi mi (y) Tura mi (t):')

olasilik = randint(0,1)

def parayi_at():

    if olasilik == 0:
        print('YAZI GELDI')
    if olasilik == 1:
        print('TURA GELDI')

parayi_at()

if 'y'== yaziTura and olasilik == 0:
    print('Tebrikler YAZI geldi...Bildiniz!')
elif 't'== yaziTura and olasilik == 1:
    print('Tebrikler TURA geldi...Bildiniz!')
else:
    print('Bir dahaki sefere, pes etmeyin!')




