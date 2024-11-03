import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

urlprefix = "https://vincentarelbundock.github.io/Rdatasets/csv/"
dataname = "datasets/iris.csv"
iris = pd.read_csv(urlprefix + dataname)
# (b)  Using matplotlib.pyplot, produce boxplots of 'Petal.Length' for each the three species, in one figure.
pet_len = iris["Petal.Length"]
sep_len = iris["Sepal.Length"]
species = iris["Species"]
crossTab = pd.crosstab(pet_len, species)
plt.boxplot(crossTab)
plt.show()

# (c)  Make a histogram with 20 bins for 'Petal.Length'.
plt.hist(bins=20, x=pet_len)
plt.show()
# (d)  Produce a similar scatterplot for 'Sepal.Length' against 'Petal.Length' to that of the left plot in Figure 1.9. Note that the points should be colored according to the 'pecies' feature as per the legend in the right plot of the figure.
colors = {"setosa": "purple", "versicolor": "green", "virginica": "red"}
colorvals = [colors[i] for i in species]
plt.scatter(
    x=pet_len,
    y=sep_len,
    c=colorvals,
)
for species_name, color in colors.items():
    plt.scatter([], [], color=color, label=species_name)
plt.legend(title="Species")

plt.xlabel("Petal.Length")
plt.ylabel("Sepal.Length")
plt.show()
# (e)  Using the kdeplot method of the seaborn package, reproduce the right plot of Figure 1.9, where kernel density plots for 'Petal.Length' are given.
for pecies in species:
    sns.kdeplot(
        x=pet_len[species == pecies],
        color=colors[pecies],
        fill=True,
    )

for species_name, color in colors.items():
    plt.scatter([], [], color=color, label=species_name)
plt.legend(title="")
plt.ylabel("Density")
plt.xlabel("Petal.Length")
plt.show()
