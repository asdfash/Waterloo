#xor functions
def xor(*args:str):
    x=0
    for i in args:
        x += int(i)
    return str(x%2)

def xors(a,b):
    out = ''
    for i,j in zip(a,b):
        out += xor(i,j)
    return out


# anaylsis function
def analysep(guess1,guess2,cipherls,plainls):
    sboxmap = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]


    #import files, convert to list
    
    
    sum = 0
    for cipher,plain in zip(cipherls,plainls):
        v4_select1 = xors(cipher[4:8],guess1)
        v4_select2 = xors(cipher[12:],guess2)
        u4select1 = '{0:04b}'.format(sboxmap.index(int(v4_select1,2)))
        u4select2 = '{0:04b}'.format(sboxmap.index(int(v4_select2,2)))
        sum += int(xor(u4select1[1],u4select1[3],u4select2[1],u4select2[3],plain[4],plain[6],plain[7]))

    return sum/len(cipherls) - 1/2

with open('a2q1ciphertexts.txt') as cipheraw: 
        cipherls = cipheraw.read().splitlines()
        cipheraw.close()
with open('a2q1plaintexts.txt') as plainraw: 
        plainls = plainraw.read().splitlines()
        plainraw.close()

#qn 1ai
print("1ai")
carolguess1 = '0111'
carolguess2 = '0110'
print(analysep(carolguess1,carolguess2,cipherls,plainls))

#qn 1b
print('1b')
best = ''
bestbias = 0
for i in range(256):
    guess12 = f'{i:08b}'
    guess1=guess12[:4]
    guess2=guess12[4:]
    bias = analysep(guess1,guess2,cipherls,plainls)
    if abs(bias)>abs(bestbias):
        best = guess12
        bestbias = bias
print(bestbias)
print(best)

#qn 1d


#qn 2a
print('2a')
with open('a2q2ciphertexts.txt') as raw: 
    ls = raw.read().splitlines()
    raw.close()
cipherls2 = []
plainls2 = []
for i in ls:
    x = i.split(',')
    plainls2.append(x[0])
    plainls2.append(x[1])
    cipherls2.append(x[1])
    cipherls2.append(x[2])

for i in range(256):
    guess12 = f'{i:08b}'
    guess1=guess12[:4]
    guess2=guess12[4:]
    bias = analysep(guess1,guess2,cipherls2,plainls2)
    if abs(bias)>abs(bestbias):
        best = guess12
        bestbias = bias
print(bestbias)
print(best)