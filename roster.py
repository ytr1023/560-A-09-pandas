#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
player = {"Last Name": ["High", "Cadeau", "Ryan", "Davis", "Bacot", "Trimble", "Wojcik", "Washington", "Lebo", "Landry"],
          "First Name": ["Zayden", "Elliot", "Cormac", "RJ", "Armando", "Seth", "Paxson", "Jalen", "Creighton", "Rob"],
          "height": [81, 73, 77, 72, 83, 75, 77, 82, 73, 76],
          "weight": [225, 180, 195, 180, 240, 195, 195, 230, 180, 190],
          }
data = pd.DataFrame(player)

data["bmi"] = (data["weight"] / (data["height"] ** 2) * 703).round(2)
print(data)

data.to_csv("bmi.csv")