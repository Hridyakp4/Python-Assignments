#Use filter function to filter out the elements from a list that are divisible by 3 & 5
def divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        return num

list_input = []
 
n = int(input("Enter number of elements : "))
print("Enter elements, press enter after every element ")

for i in range(0, n):
    ele = int(input())
 
    list_input.append(ele)

print(list(filter(divisibility, list_input)))