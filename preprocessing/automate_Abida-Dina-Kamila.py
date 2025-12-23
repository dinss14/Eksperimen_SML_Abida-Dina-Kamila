import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


def run_preprocessing(
    input_path: str,
    output_dir: str,
    test_size: float = 0.2,
    random_state: int = 42
):

    df = pd.read_csv(input_path)

    df = df.copy()
    df["Weekend"] = df["Weekend"].astype(int)
    df["Revenue"] = df["Revenue"].astype(int)

    X = df.drop(columns=["Revenue"])
    y = df["Revenue"]

    categorical_cols = ["Month", "VisitorType"]
    boolean_cols = ["Weekend"]
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
        "TrafficType",
    ]


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state,
    )


    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_cols),
            ("bool", "passthrough", boolean_cols),
        ]
    )

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    feature_names = preprocessor.get_feature_names_out()


    X_train_df = pd.DataFrame(X_train_processed, columns=feature_names)
    X_train_df["Revenue"] = y_train.values

    X_test_df = pd.DataFrame(X_test_processed, columns=feature_names)
    X_test_df["Revenue"] = y_test.values


    os.makedirs(output_dir, exist_ok=True)

    train_path = os.path.join(
        output_dir,
        "online_shoppers_train_preprocessed.csv"
    )
    test_path = os.path.join(
        output_dir,
        "online_shoppers_test_preprocessed.csv"
    )

    X_train_df.to_csv(train_path, index=False)
    X_test_df.to_csv(test_path, index=False)

    print("Preprocessing selesai")
    print("Output directory:", output_dir)
    print("Train shape:", X_train_df.shape)
    print("Test shape:", X_test_df.shape)


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    INPUT_PATH = os.path.join(
        BASE_DIR,
        "online_shoppers_intention_raw.csv"
    )

    OUTPUT_DIR = os.path.join(
        BASE_DIR,
        "preprocessing",
        "online_shoppers_intention_preprocessing"
    )

    run_preprocessing(INPUT_PATH, OUTPUT_DIR)

    print("CI preprocessing triggered")