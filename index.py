from items import ChildsTshirt, YoungAdultTankTop, MensCoat, WomensCasualDress

boys_logo_t = ChildsTshirt(
    "Boys' Logo T", "light blue", "solid", "short-sleeve", "the store logo", "left breast", "male")
young_womens_tree_tanktop = YoungAdultTankTop(
    "Young Adult Women's Tree Tank Top", "gray", "solid", "a world tree graphic", "front", "female")
mens_peacoat = MensCoat("Men's Peacoat", "solid", "black")
womens_flower_casual_dress = WomensCasualDress(
    "Women's Flower Dress", "flower-patterned", "purple", "knee-length", "short-sleeve")

# print(boys_logo_t.target())
print(boys_logo_t)
print(young_womens_tree_tanktop)
print(mens_peacoat)
print(womens_flower_casual_dress)
