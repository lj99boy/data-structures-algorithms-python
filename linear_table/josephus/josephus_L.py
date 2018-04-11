def josephus_L(n,k,m):
    people = list(range(1,n+1))

    i = k
    for num in range(n,0,-1):
        i = (i+m-1) % num
        print(people.pop(i)," ," if num>1 else "\n")
    return

josephus_L(10,3,2)