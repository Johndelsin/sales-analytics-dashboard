from kaggle.api.kaggle_api_extended import KaggleApi
import os
#Authenticate API
api = KaggleApi()
api.authenticate()

# Create data directory if it doesnt exist
os.makedirs("../data", exist_ok=True)

api.dataset_download_files (
    "vivek468/superstore-dataset-final",
    path="../data",
    unzip=True
)

print("Dataset downloaded successfully!")