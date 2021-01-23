import pandas

data = pandas.read_csv("squirrels.csv")
# data_dict = data.to_dict()
print(data["Primary Fur Color"].unique())
gray_sq = len(data[data["Primary Fur Color"]=="Gray"])
red_sq = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_sq = len(data[data["Primary Fur Color"]=="Black"])

sq_dict = {
    "Fur_color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_sq, red_sq, black_sq]

}

df = pandas.DataFrame(sq_dict)
df.to_csv("Squirrels_fur_color.csv")

