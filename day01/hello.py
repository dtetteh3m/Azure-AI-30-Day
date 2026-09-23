# azure_test.py

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
import os
from dotenv import load_dotenv

load_dotenv()

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

if not subscription_id:
    raise ValueError("AZURE_SUBSCRIPTION_ID is not set in the .env file")

credential = DefaultAzureCredential()

client = ResourceManagementClient(
    credential,
    subscription_id
)

print("Azure authentication successful!")

for resource_group in client.resource_groups.list():
    print(resource_group.name)