# def linear_search(the_list, target):
#     for x in range(len(the_list)):
#         if the_list[x] == target:
#             print("Found at index", x)
#             return x 
#     print("Target is not in the list") 
#     return -1 

# my_list = [5,4,3,6,7]

# linear_search(my_list, 5)
# linear_search(my_list, 3)
# linear_search(my_list, 8)

def binary_search(the_list, target):
    lower_bound = 0 
    upper_bound = len(the_list) - 1 
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2 
        pivot_value = the_list[pivot]

unsorted_list = [101, 50, 5, 12, 52]

def bubblesort(the_list):
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        list_changed = False 
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j + 1]

            if item > next:
                the_list[j] = next 
                the_list[j+1] = item 

            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break 

            
bubblesort(unsorted_list)