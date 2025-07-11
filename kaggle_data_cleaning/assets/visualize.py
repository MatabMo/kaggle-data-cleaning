import os
import pandas as pd
from dagster import AssetExecutionContext, MaterializeResult, MetadataValue, asset

@asset(group_name="credit_score", compute_kind="Kaggle API")
def visualize_credit_score_data(context: AssetExecutionContext) -> MaterializeResult:
    os.environ["KAGGLE_USERNAME"] = "mahtabmoghadam"
    os.environ["KAGGLE_KEY"] = "8fe50e2f3d69d841f6073ce5b3c73897"
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    dataset = "parisrohan/credit-score-classification"
    os.makedirs("data", exist_ok=True)
    api.dataset_download_files(dataset, path="data", unzip=True)

    # Prepare previews for train and test
    previews = {}
    for file in os.listdir("data"):
        if file.endswith(".csv"):
            csv_path = os.path.join("data", file)
            df = pd.read_csv(csv_path, nrows=10)
            if "train" in file.lower():
                previews["train_preview"] = MetadataValue.md(df.head().to_markdown())
            elif "test" in file.lower():
                previews["test_preview"] = MetadataValue.md(df.head().to_markdown())

    return MaterializeResult(metadata=previews) 