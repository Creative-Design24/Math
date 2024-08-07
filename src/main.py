import Modules.Basic as ope

SIGNS = ['+', '-', 'x', '/', '^']

def detect_signs(sig, param):
    if sig == '+':
        return ope.addition(param[0], param[1])
    elif sig == '-':
        return ope.subtraction(param[0], param[1])
    elif sig == 'x':
        return ope.multiplication(param[0], param[1])
    elif sig == '/':
        return ope.division(param[0], param[1])
    elif sig == '^':
        return ope.empowerment(param[0], param[1])

def process(txt):
    txt = txt.split()
    res = []
    sig = ''
    for i in txt:
        if i not in SIGNS:
            res.append(int(i))
        else:
            sig = i
    return detect_signs(sig, res)

if __name__ == '__main__':
    print('Bienvenido a Math')
    while True:
        x = input('>> ')
        if x == 'quit':
            break
        print(process(x))
