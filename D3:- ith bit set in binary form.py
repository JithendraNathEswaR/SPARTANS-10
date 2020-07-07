n=bin(int(input('Enter binary number:- '))).replace('0b','')
i=int(input('Enter the ith position:- '))
if n[i-1]=='1':
    print('Is Set Bit')
else:
    print('Not a Set Bit')
