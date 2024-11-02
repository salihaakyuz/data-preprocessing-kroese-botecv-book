import pandas as pd

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls' 
nutri = pd.read_excel(xls) 


nutri.iloc[:,0]=nutri.iloc[:,0].replace({1: "Male", 2:"Female"})

fam_DICT={1:"Single",2:"Living with spouse", 3:"Living with family",4:"Living with someone else"}
nutri.iloc[:,1]=nutri.iloc[:,1].replace(fam_DICT)

nutri.iloc[:,4]=nutri.iloc[:,4].astype(float)


nutri.iloc[:,5]=nutri.iloc[:,5].astype(float)

frequency_scale = {
    0: "Never",
    1: "Less than once a week",
    2: "Once a week",
    3: "2–3 times a week",
    4: "4–6 times a week",
    5: "Every day"
}

nutri.iloc[:,6:12]=nutri.iloc[:,6:12].replace(frequency_scale)
oil_types = {
    1: "Butter",
    2: "Margarine",
    3: "Peanut oil",
    4: "Sunflower oil",
    5: "Olive oil",
    6: "Mix of vegetable oils (e.g., Isio4)",
    7: "Colza oil",
    8: "Duck or goose fat"
}
nutri.iloc[:,12]=nutri.iloc[:,12].replace(oil_types)
print(nutri.dtypes)
# gender               object
# situation            object
# tea                   int64
# coffee                int64
# height              float64
# weight              float64
# age                   int64
# meat                 object
# fish                 object
# raw_fruit            object
# cooked_fruit_veg     object
# chocol               object
# fat                  object
# dtype: object