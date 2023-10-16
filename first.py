d=[]
def create(k):
    for i in range (k):
        p=int(input("enter the element:"))
        d.append(p)
    print(d)
def add(a):
    # for i in range(a):
        s=int(input("added number:"))  
        d.insert(a,s)
        print(d)
def remove(self,e):
     self.n.remove(e)
def sort(so):
     o=int(input("sorted:"))
     d.sort()
     print(d)
def replace(r):
     txt=int(input("replaced"))
     d[1]="9"   
     print(d)
     
     



while True:
    n=int(input("enter the choice:"))
    if n==1:
        k=int (input("enter the limit:"))
        create(k)   
    elif n==2:
        a=int(input("add element position"))
        add(a)
    elif n==3:
         e=int(input("enter number to remove:"))
         d.remove(n)
         print("list:",d)
         
    elif n==4:
    
         d.sort()
         print(d)
         
    elif n==5 :
         r=int(input("enter replaced number"))
         replace(r)
             
    elif n==6:
            print("exit")
            break