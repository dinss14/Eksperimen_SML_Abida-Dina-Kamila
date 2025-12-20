import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


def run_preprocessing(
    input_path: str,
    output_path: str,
    test_size: float = 0.2,
    random_state: int = 42
):

    # 1. Load Dataset
    df = pd.read_csv(input_path)

    # 2. Copy & Konversi Tipe Data
    df_prep = df.copy()
    df_prep["Weekend"] = df_prep["Weekend"].astype(int)
    df_prep["Revenue"] = df_prep["Revenue"].astype(int)

    # 3. Pisahkan Feature & Target
    X = df_prep.drop(columns=["Revenue"])
    y = df_prep["Revenue"]

    # 4. Definisikan Kolom
    categorical_cols = [
        "Month",
        "VisitorType"
    ]

    boolean_cols = [
        "Weekend"
    ]

    numerical_cols = [
        "Administrative",
        "Administrative_Duration",
        "Informational",
        "Informational_Duration",
        "ProductRelated",
        "ProductRelated_Duration",
        "BounceRates",
        "ExitRates",
        "PageValues",
        "SpecialDay",
        "OperatingSystems",
        "Browser",
        "Region",
        "TrafficType"
    ]

    # 5. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )

    # 6. Preprocessing Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_cols),
            ("bool", "passthrough", boolean_cols),
        ]
    )

    # 7. Fit & Transform
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    feature_names = preprocessor.get_feature_names_out()

    # 8. Build Final DataFrame
    X_train_df = pd.DataFrame(X_train_processed, columns=feature_names)
    X_train_df["Revenue"] = y_train.values
    X_train_df["dataset_split"] = "train"

    X_test_df = pd.DataFrame(X_test_processed, columns=feature_names)
    X_test_df["Revenue"] = y_test.values
    X_test_df["dataset_split"] = "test"

    final_df = pd.concat([X_train_df, X_test_df], axis=0)

    # 9. Save Output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_df.to_csv(output_path, index=False)

    print("Preprocessing selesai.")
    print(f"Output disimpan di: {output_path}")
    print("Shape akhir:", final_df.shape)


# ENTRY POINT
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    INPUT_PATH = os.path.join(
        BASE_DIR,
        "online_shoppers_intention_raw.csv"
    )

    OUTPUT_PATH = os.path.join(
        BASE_DIR,
        "preprocessing",
        "online_shoppers_intention_preprocessing.csv"
    )

    run_preprocessing(INPUT_PATH, OUTPUT_PATH)

print("CI preprocessing triggered")
