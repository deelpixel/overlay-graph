from matplotlib import pyplot as plt
import pandas as pd
file =('C:/Users/user/Videos/Downloads/graphs_.xlsx')
data=pd.read_excel(file)
overlapping = 0.7
line1 = plt.plot(data[data.columns[0]],data[data.columns[1]],alpha=overlapping, c='red', lw=5,label="01.V")
line2=plt.plot(data[data.columns[2]],data[data.columns[3]],alpha=overlapping, c='green', lw=5,label="1V")
line3 = plt.plot(data[data.columns[4]],data[data.columns[5]], alpha=overlapping,c='black', lw=5,label="10V")
line4=plt.plot(data[data.columns[6]],data[data.columns[7]],alpha=overlapping, c='blue', lw=5,label="100V")
line5 = plt.plot(data[data.columns[8]],data[data.columns[9]], alpha=overlapping,c='yellow', lw=5,label="1000V")
plt.xlabel("Potential (V)")
plt.ylabel("Ampere (A)")
plt.title("title")
plt.legend()
plt.savefig("save.png")
plt.show()