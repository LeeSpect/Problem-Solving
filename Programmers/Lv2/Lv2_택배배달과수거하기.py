from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    #init. 두 배열 다 0이 아닐 때까지 pop
    #1. max(len(deliveries), len(pickups))
    
    #init
    deliveries = deque(deliveries)
    pickups = deque(pickups)
    while(deliveries and not deliveries[-1]):
        deliveries.pop()
    while(pickups and not pickups[-1]):
        pickups.pop()

    while(deliveries or pickups):
        answer += max(len(deliveries), len(pickups)) * 2
        temp_cap = cap
        while(temp_cap and deliveries):
            if(not deliveries[-1]):
                deliveries.pop()
            elif(temp_cap > deliveries[-1]):
                temp_cap -= deliveries.pop()
            elif(temp_cap < deliveries[-1]):
                deliveries[-1] -= temp_cap
                temp_cap=0
            else:
                temp_cap = 0
                deliveries[-1] = 0
                while(deliveries and not deliveries[-1]):
                    deliveries.pop()
        temp_cap = cap
        while(temp_cap and pickups):
            if(not pickups[-1]):
                pickups.pop()
            elif(temp_cap > pickups[-1]):
                temp_cap -= pickups.pop()
            elif(temp_cap < pickups[-1]):
                pickups[-1] -= temp_cap
                temp_cap=0
            else:
                temp_cap = 0
                pickups[-1] = 0
                while(pickups and not pickups[-1]):
                    pickups.pop()
        # print(deliveries)
        # print(pickups)

    return answer


print(solution(2, 2, [0,0], [0, 4]))


