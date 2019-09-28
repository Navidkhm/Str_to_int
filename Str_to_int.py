def convert_str_to_int(a):
    try:
        if a[0] == "'":
            a = a[1:]
        if a[len(a)-1] == "'":
            a = a[:len(a)-1]
        for l in a:
            if not l.isnumeric():
                print()
                print("< A Non-numeric character was detected >")
                return
        fin = x = 0
        a = a[::-1]
        for i in a:
            num = 0
            res = 10**x
            for j in '0123456789':
                if j < i:
                    num += 1
            fin = (res*num)+fin
            x += 1
        print(fin, type(fin))
    except TypeError:
        print("< Wrong type: int >")

if __name__ == '__main__':
    convert_str_to_int(8574)
