N = int(input())

li = ['']*N

def re_ans(n,li):
    if n == 1:
        li[n-1] = str(n)
        return li[n-1]
    else:
        li[n-1] = re_ans(n-1,li)+' '+str(n)+' '+re_ans(n-1,li)
        return  li[n-1]

print(re_ans(N,li))
