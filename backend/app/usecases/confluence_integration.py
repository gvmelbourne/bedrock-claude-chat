import requests

def get_confluence_pages(confluence_url, confluence_token, space_key):
    headers = {
        "Authorization": f"Bearer {confluence_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{confluence_url}/rest/api/space/{space_key}/content", headers=headers)
    return response.json()
