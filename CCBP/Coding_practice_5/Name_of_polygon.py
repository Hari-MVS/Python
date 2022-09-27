a = int(input())
print("Not Polygon" if a<3 else("Triangle" if a==3 else ("Quadrilateral" if a==4 
else ("Pentagon" if a==5 else "Big Polygon"))))
