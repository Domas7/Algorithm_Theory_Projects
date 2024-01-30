import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import clear_output


def insertion_sort(arr):
    steps=0
    n = len(arr)
    
    for x in range(1, n):
        key = A[x]
        i = x - 1
        steps+=2
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
            steps+=2
        A[i+1]=key
        steps+=1
    return steps



mpl.rcParams['figure.figsize'] = [16,4]
#mpl.rcParams.update({'font.size': 12})

fig, ax = plt.subplots(1, 2)
fig.suptitle('Counted steps and Asymptotic running time')


B=[5,2,4,6,1,3]
points=13 # plotting points
x=[]
y=[]
ref=[]
c=[]

for i in range(0,points):
    clear_output(wait=True)
    print(i+1,"/", points)
    steps=insertion_sort(B) 
    # double the size of the list to sort
    B=B*2
    x.append(len(B))
    y.append(steps)    
    c.append(steps/len(B)**2)# quick and dirty estimation of c--> T(sort)=c.N^2
    
for v in x:
    ref.append([v**2 *c[6]])
ax[0].plot(x,y, color="red", label="counted steps")
ax[0].plot(x,ref, color="green", label= str(round(c[6],2)) + ".n^2 --> O(n^2)")
ax[0].set_xlabel("size of n")
ax[0].set_ylabel("computation steps")
ax[0].legend()

ax[1].scatter(x,c, label= "approximation of c" )
ax[1].set_xlabel("size of n")
ax[1].set_ylabel("c factor")


plt.show()