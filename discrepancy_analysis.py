import streamlit as st
import pandas as pd

st.title("Stock/Inventory Discrepancy (Analytics)")

expected_file = st.file_uploader("Upload expected csv file", type="csv", key="expected")
counted_file = st.file_uploader("Upload counted csv file", type="csv", key="counted")


if expected_file is not None and counted_file is not None:
    df_expected = pd.read_csv(expected_file, encoding="latin-1", dtype=str)
    df_counted = pd.read_csv(counted_file, encoding="latin-1", dtype=str)

    df_counted = df_counted.drop_duplicates("RFID")

    df_B = (
        df_counted.groupby("Retail_Product_SKU")
        .count()[["RFID"]]
        .reset_index()
        .rename(columns={"RFID": "Retail_CCQTY"})
    )

    selected_cols = [
        "Retail_Product_SKU",
        "Retail_Product_Name",
        "Retail_Product_Level1Name",
        "Retail_SOHQTY",
    ]

    df_A = df_expected[selected_cols]

    df_discrepancy = pd.merge(
        df_A,
        df_B,
        how="outer",
        left_on="Retail_Product_SKU",
        right_on="Retail_Product_SKU",
        indicator=True,
    )

    # Renaming columns
    df_discrepancy.columns = df_discrepancy.columns.str.replace("Retail_", "")
    df_discrepancy.rename(columns={"_merge": "SKUSide"}, inplace=True)

    df_discrepancy.replace(
        {
            "SKUSide": {
                "right_only": "CC Only",
                "left_only": "SOH Only",
                "both": "SOH & CC",
            },
        },
        inplace=True,
    )

    # Filling empty values
    df_discrepancy["CCQTY"] = df_discrepancy["CCQTY"].fillna(0).astype(int)
    df_discrepancy["SOHQTY"] = df_discrepancy["SOHQTY"].fillna(0).astype(int)

    # Discrepancy enrichment
    df_discrepancy["Diff"] = df_discrepancy["CCQTY"] - df_discrepancy["SOHQTY"]
    df_discrepancy["Match"] = df_discrepancy["SKUSide"] == "SOH & CC"
    df_discrepancy["Unders"] = df_discrepancy["Diff"].map(lambda x: -x if x < 0 else 0)
    df_discrepancy["Overs"] = df_discrepancy["Diff"].map(lambda x: x if x > 0 else 0)

    df_discrepancy.loc[:, df_discrepancy.dtypes == object] = df_discrepancy.loc[
        :, df_discrepancy.dtypes == object
    ].fillna("-")

    st.write("Discrepancy Enrichment")
    st.dataframe(df_discrepancy)

    # Accuracy Calculation
    st.write("Dynamic Aggregation by Product lvl 1 Name")

    # filter out no category
    df_discrepancy = df_discrepancy[df_discrepancy["Product_Level1Name"] != "-"]

    df_aggregation = df_discrepancy.groupby("Product_Level1Name").sum()
    df_aggregation.loc["TOTAL"] = df_aggregation.sum()

    st.dataframe(df_aggregation)
    # st.dataframe()

    # Accuracy Calculation
    st.write("Accuracy Calculation")

    df_aggregation["SKU Accuracy"] = df_aggregation["Match"] / df_aggregation["SOHQTY"]
    df_aggregation["Item Accuracy"] = df_aggregation["CCQTY"] / df_aggregation["SOHQTY"]
    df_aggregation["Unit Level Accuracy"] = (
        df_aggregation["SOHQTY"]
        - df_aggregation["Unders"]
        - df_aggregation["Overs"] / df_aggregation["SOHQTY"]
    )

    st.dataframe(df_aggregation)
