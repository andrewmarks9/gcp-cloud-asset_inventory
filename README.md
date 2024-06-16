# GCP Asset Inventory

This Python script uses the Google Cloud Asset Inventory API to search for and export GCP project resources to a CSV file in a Google Cloud Storage bucket.
The script was created to get an inventory of tagged GCP projects by cost_type
I have run this script successfully as a cron job.  

Feel free to modify this script for your use case.

## Overview

The script performs the following steps:

1. Authenticates with the Google Cloud API using a service account.
2. Searches for all GCP projects with a 'cost_type' label using the `search_all_resources` method.
3. Writes the project details (name, display name, project ID, state, asset type, and labels) to a CSV file.
4. Uploads the CSV file to a Google Cloud Storage bucket.

## Prerequisites

- Python 3.x
- Google Cloud SDK installed and authenticated
- A service account key file with the appropriate permissions

## Installation

1. Clone the repository:

git clone https://github.com/your-username/gcp-asset-inventory.git


2. Navigate to the project directory:

cd gcp-asset-inventory


3. Install the required Python packages:

pip install -r requirements


## Usage

1. Replace the placeholders in the `cloudasset_inventory.py` file with your actual values:
- `SERVICE_ACCOUNT_KEY_FILE`: Path to your service account key file
- `YOUR_PROJECT_ID`: Your Google Cloud Platform project ID
- `YOUR_ORGANIZATION_ID`: Your organization ID
- `GCP_ASSET_INVENTORY_BUCKET`: The name of the Google Cloud Storage bucket where the CSV file will be uploaded

2. Run the script:

python cloudasset_inventory.py

