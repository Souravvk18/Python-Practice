  
def print_formatted(number):
    align = len(bin(number)[2:])
    for num in range(1, number + 1):
        n_dec = str(num)
        n_oct = oct(num)[2:]
        n_hex = hex(num)[2:].upper()
        n_bin = bin(num)[2:]
        print(n_dec.rjust(align), n_oct.rjust(align), n_hex.rjust(align), n_bin.rjust(align))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

"""
i/p- 17

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
   """