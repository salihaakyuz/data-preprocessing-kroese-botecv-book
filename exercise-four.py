import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

xls = "http://www.biostatisticien.eu/springeR/nutrition_elderly.xls"
nutri = pd.read_excel(xls)
contingency_table = pd.crosstab(nutri["situation"], nutri["gender"])
proportion_table = contingency_table.div(contingency_table.sum(axis=0), axis=1)
proportion_table.plot(
    kind="bar", stacked=True, color=["SkyBlue", "Pink"], edgecolor="black"
)
plt.legend(title="Gender", loc="upper center", labels=["Male", "Female"])
plt.xlabel("Situation")
plt.ylabel("Proportion")
plt.show()
