"""
This script uses the Google Cloud Asset Inventory API to search for and export
GCP project resources to a CSV file in a Google Cloud Storage bucket.

The script performs the following steps:
1. Authenticates with the Google Cloud API using the
   GOOGLE_APPLICATION_CREDENTIALS environment variable.
2. Searches for all GCP projects with a 'cost_type' label using the
   `search_all_resources` method.
3. Writes the project details (name, display name, project ID, state,
   asset type,and labels) to a CSV file.
4. Uploads the CSV file to a Google Cloud Storage bucket.
"""

import datetime
import os
from google.cloud import storage
from google.cloud import asset_v1
from google.cloud.asset_v1 import AssetServiceClient

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/credentials.json"

client = asset_v1.AssetServiceClient()

parent = "organizations/YOUR_ORGANIZATION_ID"
content_type = asset_v1.ContentType.RESOURCE
read_time = None

TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
BUCKET_NAME = "GCP_ASSET_INVENTORY_BUCKET"
OUTPUT_FILE = f"gcpinventory_{TIMESTAMP}.csv"

storage_client = storage.Client(project='YOUR_PROJECT_ID')
bucket = storage_client.bucket(BUCKET_NAME)
blob = bucket.blob(OUTPUT_FILE)

# Export and filter assets to csv file using python client library
asset_client = AssetServiceClient()
parent = "organizations/YOUR_ORGANIZATION_ID"
content_type = "RESOURCE"
read_options = {"content_type": content_type}

client = asset_v1.AssetServiceClient()

# Search assets
response = client.search_all_resources(
    scope=parent,
    # Update label value
    query='labels.cost_type:*',
    asset_types=["cloudresourcemanager.googleapis.com/Project"]
)

# Write to CSV
with blob.open("w") as file:
    headers = "name,display_name,project_id,state,asset_type,labels\n"
    file.write(headers)
    for resource in response:
        project_id = resource.additional_attributes.get("projectId", "")
        file.write(f"{resource.name},{resource.display_name},{project_id},"
                   f"{resource.state},{resource.asset_type},{resource.labels},\n")
