# %%
def main():
    li=input("please put a list num by comas ")
    print(maxnum(li))

    strr=input("pls put string :").strip().lower()
    cvowels(strr)
    cprime()
    print(fibbo(5))
def maxnum(li):
    lii=li.split(",")
    maxi=-1000000

    for i in lii:
        num=int(i)
        if num >maxi:
            maxi=num
    return maxi 


def cvowels(strr):
        vowels="aioeu"
        
        count=0
        for r in strr:
            if r in vowels:
                count=count+1
        print(count)

def cprime():
    count=0
    for i in range(2,101):
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            print(i)
def fibbo(numm):
    if numm==1 or numm==0:
        return 1
    else:
        return fibbo(numm-1)+fibbo(numm-2)
def atm(amuntofwithdrawed):
    balance=100000
    if amuntofwithdrawed <= 0 or amuntofwithdrawed > balance:
       return "invaild ...."
    else:
         return f" your balance know is :{balance-amuntofwithdrawed}"

def intersectionintwolists(l1,l2):
    l1=set(l1)
    l2=set(l2)
    return list(l1 & l2)
            
def factorial(num):
    if num==1 or num==0 :
        return 1
    else:
        return num*factorial(num-1)
def validate():
    while True:
       text = input("Enter a number > 10: ")
       if text.isdigit():
         num=int(text)
         if num>10:
            print("true")
            break
         else:
            print("try again")

def sumnumofdigits(numm):
    total=0
    for digit in str(numm):
        total+= int(digit)
    print (total)
def plaindroom(text):

    reversedd=text[::-1]
    if text==reversedd:
        print("plaindroom")
    else:
        print("not plaindroom")
    
def createdifrontwolists(l1,l2):
    d={
    }
    if len (l1) < len(l2):
        for i in range(len(l1)):
            d[l1[i]]=l2[i]
    else:
        for i in range(len(l2)):
            d[l1[i]] = l2[i]

    return d

def checkpass():
    correctpass="Alaa123"
    attempt=3
    while attempt>0 : 
        text=input("put your pass :")
        if text ==correctpass:
            print("correct")
            break
        else:
            print ("wrong")
            attempt=attempt-1
        if attempt==0:
            print("you reach your limit")
        
        
        




          

   
       



if __name__=="__main__":
    main()
