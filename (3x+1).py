print("This is 3x+1 problem! (Collatz Conjecture)")
x=int(input("Enter a random positive integer greater than 1:"))
print(x,end=",")
no_of_steps=0
while x!=1:
    if x%2==0:
        x=int(x/2)
        if x==1:
            print(x)
        else:
            print(x,end=",")
        no_of_steps +=1
    else:
        x=3*x+1
        print(x,end=",")
        no_of_steps +=1
print("")
print("Number of steps taken to get to 1 is", no_of_steps)
