import requests
from datetime import datetime, timedelta
import pandas as pd

api_url = 'https://api.github.com/repos/metabase/metabase/pulls'

one_week_ago = (datetime.now() - timedelta(weeks=1)).isoformat()

params = {
    'state': 'all',
    'sort': 'created',
    'direction': 'desc',
    'since': one_week_ago
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    pull_requests = response.json()
    
    # Create a DataFrame from the pull request data
    df = pd.DataFrame(pull_requests)
    
    # Extract and keep only the relevant columns
    df = df[['title', 'created_at', 'updated_at', 'state']]
    
    # Add a new 'S.No' column with sequential numbers
    df['S.No'] = range(1, len(df) + 1)
    
    # Reorder the columns to have 'S.No' as the first column
    df = df[['S.No', 'title', 'created_at', 'updated_at', 'state']]
    
    # Save the DataFrame to an Excel file
    excel_file = 'pull_requests.xlsx'
    df.to_excel(excel_file, index=False)
    
    print(f'Pull requests data saved to {excel_file}')
else:
    print(f'Error: {response.status_code} - {response.text}')

