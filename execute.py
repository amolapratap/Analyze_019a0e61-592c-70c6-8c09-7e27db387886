import json
import pandas as pd

def main():
    # Read the data
    dfi = pd.read_excel("data.xlsx")
    # Compute revenue
    df = dfi[dfi["revenue"]]
    # Results
    result = {
        "row_count": len(df),
        "regions": df["region"].unique().tolist(),
        "top_n_products_by_revenue": df.groupby("product").sum()[['revenue']].nlargest(3)
    }

    # Write to JSON
    with open("result.json", "w") as f:
        json.dump(result, f)
        print("Result saved to result.json")

if __name__ == "__main__":
    main()