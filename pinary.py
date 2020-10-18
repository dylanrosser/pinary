# binary operations in python


def badd(a, b):
    """binary add """
    return bin(int(str(a),2)+int(str(b),2))


def bsub(a, b):
    """binary subtract"""
    return bin(int(str(a),2)-int(str(b),2))

def tc(val_str, bytes):
    """ twos complement"""
    import sys
    val = int(val_str, 2)
    b = val.to_bytes(bytes, byteorder=sys.byteorder, signed=False)
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)


def rd(a, b, p):
    """ one step of the restoring division algorithm"""
    return(bin(int(str(a),2)-int(str(b),2)*2**p))

def nrd(a, b, p):
    """ one step of non restoring division algorithm """
    return(bin(int(str(a),2)+int(str(b),2)*2**p))

def restoring_division(dividend, divisor):
    p = len(str(dividend))
    q=''

    for i in reversed(range(p)):
        r = rd(dividend, divisor, i)

        if int(r,2) < 0:
            q = q+'0'

        else:
            dividend = r
            q = q+'1'

        print(q, r, i)

    return q, r

def non_restoring_division(dividend, divisor):
    p = len(str(dividend))+1
    q=''
    add = False

    for i in reversed(range(p)):
        if add:
            r = nrd(dividend, divisor, i)
        else:
            r = rd(dividend, divisor, i)

        if int(r,2) < 0:
            qb = '0'
            q = q+'0'
            next_add = True


        else:
            qb = '1'
            q = q+'1'
            next_add = False

        print("\n",dividend, add, divisor, i, r, qb)

        dividend = r
        add = next_add

    return q, r
