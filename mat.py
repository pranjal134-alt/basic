import matplotlib.pyplot as plt 
# data
x = [1,2,3,4,5]
y1 = [10, 20, 25, 35, 45]
y2 = [20, 30, 35, 45, 55]

plt.plot(x, y1, label='Sales 2024') # ploting y1 data
plt.plot(x, y2, label='Sales 2025') # ploting y2 data

plt.title("YoY Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend() # show legends
plt.show()
plt.pie(y1,labels=x,autopct='%3.2f%%',startangle=90) # pie chart for y1 data
plt.title("Sales Distribution 2024")
plt.show()
x = [1,2,3,4,5]
y1 = [10, 20, 25, 35, 45]
x3 = [1,2,3,4,5]
y3 = [20, 30, 35, 45, 55]
plt.subplot(1, 2, 1) # first subplot
plt.plot(x, y1, label='Sales 2024')
plt.bar(x,y2)
plt.title("Sales 2024")
plt.subplot(1, 2, 2) # second subplot
plt.plot(x3, y3, label='Sales 2025')
plt.bar(x3, y3)
plt.title("Sales 2025")
plt.show()
plt.subplot(2,1,1)
plt.plot(x, y1, label='Sales 2024')
plt.title("Sales 2024")
plt.subplot(2,1,2)
