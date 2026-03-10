x=5#the	initial	number of infected students
k=0.4#the growth rate over 24 hrs
m=1#Day 1
print("Day",m,":",x)#print the number of infected students on day 1
#Use a while loop to calculate the number of infected students on each day until all 91 students are infected.
while x<=91:
    x=x*(1+k)
    m=m+1
    #If the number of infected students exceeds 91, break the loop and print the number of days taken to infect all students.
    if x>91:
        break
    print("Day",m,":",int(x))
#when x exceeds 91, the loop will break print the number of infected students as 91
print("Day",m,":",91)
print(m,"days were taken to infect all")




