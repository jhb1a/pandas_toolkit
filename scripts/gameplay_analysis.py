import pandas as pd

activity = pd.DataFrame(
    {
        "player_id": [1, 1, 2, 3, 3],
        "device_id": [2, 2, 3, 1, 4],
        "event_date": [
            "2016-03-01",
            "2016-05-02",
            "2017-06-25",
            "2016-03-02",
            "2018-07-03",
        ],
        "games_played": [5, 6, 1, 0, 5],
    }
)


def game_analysis(activity: pd.DataFrame):
    df = activity.sort_values(by="event_date", ascending=True)
    df = (
        df.drop_duplicates(subset="player_id", keep="first")
        .sort_values(by="player_id", ascending=True)
        .rename(columns={"event_date": "first_login"})
    )

    return df[["player_id", "first_login"]]


# Approach 1: Sort then deduplicate - intuitive, readable
def first_by_sort(df, group_col, date_col):
    return df.sort_values(date_col).drop_duplicates(subset=group_col, keep="first")


# Approach 2: Groupby + min - declarative, better for multiple aggregations
def first_by_groupby(df, group_col, date_col):
    return df.groupby(group_col)[date_col].min().reset_index()


print(game_analysis(activity))
