import os
import requests
from prettytable import PrettyTable
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    # Retrieve API key from environment variable
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("Please set API_KEY in the .env file.")

    return api_key

def get_api_url():
    # Retrieve API URL from environment variable
    api_url = os.getenv("API_URL")

    if not api_url:
        raise ValueError("Please set API_URL in the .env file.")

    return api_url

def make_api_request(api_url, api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(api_url, headers=headers)

        
        if response.status_code == 200:
            data = response.json()

            # Displays results in PrettyTable
            display_results_in_table(data)

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def display_results_in_table(data):
    if 'result' in data:
        result = data['result']
        if 'local_shards' in result:
            local_shards = result['local_shards']

            if local_shards:
                table = PrettyTable()
                table.field_names = ['shard_id', 'points_count', 'state']

                for shard in local_shards:
                    table.add_row([shard['shard_id'], shard['points_count'], shard['state']])

                print(table)

            else:
                print("No local shards to display.")

        else:
            print("No 'local_shards' found in the result.")

    else:
        print("No 'result' found in the response.")

# Fetch API key and URL from .env file
api_key = get_api_key()
api_url = get_api_url()

make_api_request(api_url, api_key)