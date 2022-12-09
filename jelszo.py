felhasznalonev = "bori99"
jelszo = "Szivecske<3"

kerd1 = None
kerd2 = None

while kerd1 != felhasznalonev and kerd2 != jelszo:
    kerd1 = input('Add meg a felhasználóneved! ')
    kerd2 = input('Add meg a jelszavad! ')
    if kerd1 != felhasznalonev and kerd2 != jelszo:
        print('Hibás felhasználónév vagy jelszó')
    else:
        print('Sikeres belépés!')
        break    































