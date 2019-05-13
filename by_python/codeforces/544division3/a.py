def lessthanten(num1):
    if num1 < 10:
        return "0"+str(num1)
    else:
        return str(num1)

h1, m1 = map(int,input().split(":"))
h2, m2 = map(int,input().split(":"))

time1 = h1 * 60 + m1
time2 = h2 * 60 + m2
mid_t = (time1 + time2) // 2
mid_h = mid_t //60
mid_m = mid_t % 60

mid_h = lessthanten(mid_h)
mid_m = lessthanten(mid_m)

print(mid_h+":"+mid_m)