# Read an integer that denotes the the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here

final_list = [circular_linked_list[i] for i in range(3)]
for i in range(5,length_of_circular_linked_list,3):
    if i == final_list[0]:
        break
    final_list.append(circular_linked_list[i])
    
final_list.pop()

print(len(final_list))
for i in final_list:
    print(i,end=" ")
