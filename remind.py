n = 0
def hanoi(num, start, end, bridge):
    global n
    n += 1
   
    if num == 1:     
        print(f"{num}번 {start} -> {end}")
        
    else:
        hanoi(num-1, start, bridge, end)
        print(f"{num}번 {start} -> {end}")
        
        hanoi(num-1, bridge, end, start)

hanoi(4,1,3,2)
print(f"이동횟수 {n}번")

