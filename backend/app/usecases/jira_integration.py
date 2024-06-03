import requests

def get_jira_issues(jira_url, jira_token, project_key):
    headers = {
        "Authorization": f"Bearer {jira_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{jira_url}/rest/api/2/search?jql=project={project_key}", headers=headers)
    return response.json()
