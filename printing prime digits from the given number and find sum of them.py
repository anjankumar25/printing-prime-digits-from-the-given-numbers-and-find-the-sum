def add(a):
    v=0
    while a>0:
        e=a%10
        c=0
        if e>1:
              for i in range(2,e):
                   if e % i ==0:
                        c=1
                        break
              if c ==0:
                  print(e)
                  v=v+e
        a=a//10
    print(v)
add(a=335463)