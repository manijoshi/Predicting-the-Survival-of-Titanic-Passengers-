n=int(input())
t=n
s=str(n)
sum=0
while(t!=0):
    sum+=(t%10)**len(s)
    t=t//10
if n==sum:
    print(n,"is an armstrong no.")
else:
    print(n,"is not an armstrong no.")