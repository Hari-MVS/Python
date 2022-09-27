amount=int(input())
note100=note50= note10=note2=note1 =0

note100=amount//100
amount-=note100*100
    

note50=amount//50
amount-=note50*50
        

note10=amount//10
amount-=note10*10
            
note1=amount
print(f"100:{note100}")
print(f"50:{note50}")
print(f"10:{note10}")
print(f"1:{note1}")
