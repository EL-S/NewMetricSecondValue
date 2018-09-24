import math

second = 0
minute = 0
hour = 0
day = 0
month = 0
year = 0

real_second = 1
real_minute = real_second * 60
real_hour = real_minute * 60
real_day = real_hour * 24
real_month = real_day * 30
real_year = real_day * 365

s = 100
m = 100
h = 10
d = 300

second = real_minute/s
minute = real_hour/m
hour = real_day/h
day = real_year/d

new_second1 = (second/real_second)
new_second2 = (minute/real_minute)
new_second3 = (hour/real_hour)
new_second4 = (day/real_day)

new1 = day/h
new2 = new1/m
new3 = new2/s

print(new1,new2,new3)

print(real_year)


print(second,new_second1)
print(minute,new_second2)
print(hour,new_second3)
print(day,new_second4)

for i in range(1,200):
    for j in range(1,200):
        for k in range(1,100):
            for z in range(1,1000):
                value = (i*j*k*z)/real_year
                if float(value).is_integer():
                    print(i,j,k,z,value)
print("done")

