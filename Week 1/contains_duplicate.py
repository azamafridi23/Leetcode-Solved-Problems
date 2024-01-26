def solution(arr):
    prod_a = 1
    prod_b = 1

    for index in range(len(arr)):
        if index>0 and prod_a<0:
            prod_b = max(prod_b*arr[index],1)
        prod_a = max(1, prod_a*arr[index])
    
    return max(prod_a,prod_b)

solution([2,3,-2,4])
        

