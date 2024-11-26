import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

avg=1.9
std=0.1

prob2_00m=round(st.norm.cdf(2, avg, std),3)
prob1_85m=round(st.norm.cdf(1.85, avg, std),3)
prob1_85m_2m=prob2_00m-prob1_85m

print("prob2_00m:",prob2_00m)
print("prob1_85m:",prob1_85m)
print("prob1_85m_2m:",prob1_85m_2m)

x_axis = np.arange(avg-3*std, avg+3*std, 0.01) 
y_axis=st.norm.pdf(x_axis, avg, std)

plt.plot(x_axis, y_axis) 
plt.show() 
