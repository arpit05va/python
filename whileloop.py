#  we use this loop when we donot know before,the number of time to iterate.

n=7
while n>0:
    print(n)
    n-=1

# break statement terminates the loop containing it

for i in range(10):
    if i>6:
        break
    print(i)

# continue statement is used to skip rest of the code inside a loop for the current iteration only.Loop does not terminate but continue on with the next iteration.


for i in range(10):
    if i==8:
        continue
    print(i)
