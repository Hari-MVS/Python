T = input()


S = T[-1]
T = T[0:len(T)-1]
T = float(T)





if S == 'C':
   F = (9/5)*(T) + 32
   print(str(round(T,2))+"C")
   print(str(round(F,2))+'F')
   print(str(round((T)+273,2))+'K')



elif S == 'F':
   C = (float(T)-32)*(5/9)
   K = C+273
   print(str(round(C,2))+'C')
   print(str(round(T,2))+'F')
   print(str(round(K,2))+'K')



elif S == 'K':
   C = float(T)-273
   F = (9/5)*float(C) + 32
   print(str(round(C,2))+'C')
   print(str(round(F,2))+'F')
   print(str(round(T,2))+'K')


