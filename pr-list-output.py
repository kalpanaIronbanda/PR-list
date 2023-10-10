import requests
from datetime import datetime, timedelta

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
    for pr in pull_requests:
        pr_number = pr["number"]
        pr_title = pr["title"]
        # Encode Unicode characters to a safe encoding (e.g., utf-8)
        pr_title_encoded = pr_title.encode('utf-8', 'ignore').decode('utf-8')
        print(f'PR #{pr_number}: {pr_title_encoded}')
else:
    print(f'Error: {response.status_code} - {response.text}')

