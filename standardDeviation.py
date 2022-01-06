import csv
import math
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data =file_data[0]
print(data)
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)

    mean=total/n
    return mean

squarelist=[]
for number in data:
    a= int(number)-mean(data)
    a=a**2
    squarelist.append(a)

sum=0
for i in squarelist:
    sum=sum+i
print(sum)
result=sum/(len(data)-1)
print(result)
standardDeviation=math.sqrt(result)
print(standardDeviation)















