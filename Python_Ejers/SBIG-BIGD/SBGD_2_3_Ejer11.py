import matplotlib.pyplot as plt
import seaborn as sns

data=[9, 12, 6, 11, 19, 5, 8, 13, 2, 8, 5, 12, 0, 9, 4, 15, 18, 10, 6, 16]
style = {'facecolor': 'blue', 'edgecolor': '#000000', 'linewidth': 1}
sns.histplot(data=data,bins=[0,5,10,15,20],**style).set_xticks([0,5,10,15,20])
plt.show()
