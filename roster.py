#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
player = {"Last Name": ["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [82, 72, 73],
          "weight": [240, 180, 180],
          }
data = pd.DataFrame(player)
print(data)

