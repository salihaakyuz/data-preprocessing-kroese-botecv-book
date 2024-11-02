import pandas as pd
import os

current_path = os.getcwd()

mushroom = pd.read_csv(f"{current_path}/agaricus-lepiota.data", header=None)
# “(a)  How many features are in this data set?
# shape returns a tuple that consist of dimensions of an array, by calling index 1 we get the number of
# columns so the features
feature_count = mushroom.shape[1]
print(feature_count)
# (b)  What are the initial names and types of the features?”
columns_init_names = mushroom.iloc[0, :]
columns_types = mushroom.dtypes
print(columns_init_names, "\n", columns_types)
# “(c)  Rename the first feature (index 0) to 'edibility' and the sixth feature (index 5) to 'odor' [Hint: the column names in pandas are immutable; so individual columns cannot be modified directly. However it is possible to assign the entire column names list via mushroom.columns = newcols.]
columns_init_names[0] = "edible"
columns_init_names[5] = "odor"
print(columns_init_names)
# (d)  The 6th column lists the various odors of the mushrooms: encoded as 'a', 'c', Replace these with the names 'almond', 'creosote', etc. (categories corresponding to each letter can be found on the website).'.
#  Also replace the 'edibility' categories 'e' and 'p' with 'edible' and 'poisonous
# almond = a, anise = l, creosote = c, fishy = y, foul = f, musty = m, none = (
#     n,
#     pungent,
# ) = (p, spicy) = s

mushroom.iloc[:, 5] = mushroom.iloc[:, 5].map(
    {
        "a": "almond",
        "l": "anise",
        "c": "creosote",
        "y": "fishy",
        "f": "foul",
        "m": "musty",
        "n": "none",
        "s": "spicy",
        "p": "pungent",
    }
)
mushroom.iloc[:, 0] = mushroom.iloc[:, 0].map({"e": "edible", "p": "poisonous"})
print(mushroom.iloc[:, 5], mushroom.iloc[:, 0])
# (e)  Make a contingency table cross-tabulating 'edibility' and 'odor'.
contigency_table = pd.crosstab(mushroom.iloc[:, 5], mushroom.iloc[:, 0])
print(contigency_table)
# (f)  Which mushroom odors should be avoided, when gathering mushrooms for consumption?
# poisonous mushrooms must be avoided so, the odors is:
for i in range(len(contigency_table)):
    if contigency_table.loc[contigency_table.index[i], "poisonous"] > 0:
        print(contigency_table.index[i])
# (g)  What proportion of odorless mushroom samples were safe to eat?
odor = mushroom.iloc[:, 5]
edible = mushroom.iloc[:, 0]
count = 0
for i in range(len(odor)):
    if odor[i] == "none" and edible[i] == "edible":
        count += 1
if count != 0:
    x = (count / len(odor)) * 100
    print(f"Edibility percentage of mushrooms that odorless is: {x}%")
else:
    print("Count is zero, cannot calculate percentage.")
