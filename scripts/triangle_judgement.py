import pandas as pd

triangle = pd.DataFrame({"x": [13, 10], "y": [15, 20], "z": [30, 15]})


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    df = triangle.copy()
    df["triangle"] = (
        (df["x"] + df["y"] > df["z"])
        & (df["y"] + df["z"] > df["x"])
        & (df["x"] + df["z"] > df["y"])
    ).map({True: "Yes", False: "No"})

    return df


print(triangle_judgement(triangle))
