ingredients = ["vanilla extract", "milk", "butter", "sugar", "lavender liquid herbal extract", "anise extract"]
dict = {'cake flour ': '2 1/2 cups',
'vanilla instant puddding mix ': '8 tablespoons',
'baking powder ' : '1 tablespoon',
'baking soda ' : '1/4 teaspoon',
'kosher salt' : '1/2 teaspoon'}

amount = dict.values

# def recipe() :
#     print dict["The ingredients are "])
#     print dict[ingredients]
#     print dict

for items in ingredients:
    print(items)

for step in dict.items():
    print(step)
