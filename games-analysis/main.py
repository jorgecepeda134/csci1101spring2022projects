import pandas as pd
import matplotlib.pyplot as plt

df_main = pd. read_csv("game-ratings-by-release-dates.csv")

df_main["first_release_date"] =
pd.to_datetime(df_main["first_release_date"}])

plt.scatter(fr_main["first_release_date"]),
df_main["critic_rating_value"], color = "blue",
label = "Crtic Ratings")

plt.scatter(df_main["first_release_date"])
df_main["user_Rating_value"], color = "red",
label = "User Ratings")

plt.legend(loc = "upper left")

plt.show()

BAR_WIDTH = 0.4

df_main = pd.read_csv("game-ratings-by-top-10-platforms.csv")

df_follow =
df_main.groupby(["platform_name"])
["follow_count"].sum().reset_index()

df_follow = df_main.groupby(["platform_name"])
["hype_count"].sum().reset_index()

df_hype = df_hype.rename(columns = {"hype_count": "total_hypes" })

plt.bar(df_follow.index - BAR_WIDTH / 2, df_follow["total_follows"], color = "blue", label = "Number of Follows", width = BAR_WIDTH)

plt.bar(df_hype.index + BAR WIDTH / 2, df_hype["total_hypes"]), color = "red", label = "Number of Hypes", width = BAR_WIDTH)

plt.xticks(df_follow.index, df_follow["platform_name"])

plt.legend(loc = "upper left")

plt.show()