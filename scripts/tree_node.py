import pandas as pd

tree = pd.DataFrame({"id": [1, 2, 3, 4, 5], "p_id": [None, 1, 1, 2, 2]})


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    df = tree.copy()
    df["type"] = "Leaf"
    df.loc[df["id"].isin(df["p_id"]), "type"] = "Inner"
    df.loc[df["p_id"].isna(), "type"] = "Root"

    return df[["id", "type"]]


print(tree_node(tree))
