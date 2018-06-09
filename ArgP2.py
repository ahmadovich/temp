import argparse

par1 = argparse.ArgumentParser('This is a detailed ArgParse test')
par1.add_argument('-x','--Xarg', type=int, metavar = '', help = 'Count of x, -x count', choices = [ 1,2,3,4,5])
Mutz1 = par1.add_mutually_exclusive_group()

# At least one of the next mutually exclusive arguments is required
Mutz2 = par1.add_mutually_exclusive_group(required = True)

Mutz3 = par1.add_mutually_exclusive_group()

Mutz1.add_argument('-1', '--one', action= 'store_true',help = "one")
Mutz1.add_argument('-2', '--two', action= 'store_true',help = "two")
Mutz2.add_argument('-3', '--three', action= 'store_true',help = "three")
Mutz2.add_argument('-4', '--four', action= 'store_true',help = "four")
Mutz3.add_argument('-5', '--five', action= 'store_true',help = "five")
Mutz3.add_argument('-6', '--six', action= 'store_true',help = "six")



argz = par1.parse_args()


print(argz.Xarg)