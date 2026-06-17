import os
import urllib.request
import json

token = os.environ.get("GITHUB_TOKEN")
if not token:
    print("No GITHUB_TOKEN found in environment.")
    exit(0)

query = """
query {
  user(login: "nigampalash") {
    repositories(first: 100, ownerAffiliations: OWNER) {
      nodes {
        name
        isFork
        stargazerCount
        defaultBranchRef {
          target {
            ... on Commit {
              history {
                totalCount
              }
            }
          }
        }
      }
    }
    pullRequests {
      totalCount
    }
    issues {
      totalCount
    }
    repositoriesContributedTo(first: 100) {
      totalCount
    }
  }
}
"""

req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": query}).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))
    
    # Calculate total commits
    total_commits = 0
    repos = result.get("data", {}).get("user", {}).get("repositories", {}).get("nodes", [])
    print("Repos commit counts:")
    for r in repos:
        name = r.get("name")
        commits = 0
        ref = r.get("defaultBranchRef")
        if ref and ref.get("target"):
            commits = ref.get("target", {}).get("history", {}).get("totalCount", 0)
        print(f" - {name} (Fork: {r.get('isFork')}): {commits} commits")
        total_commits += commits
        
    print("\nCalculated Total Commits:", total_commits)
    
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graphql_output.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json.dumps(result, indent=2) + f"\n\nCalculated Total Commits: {total_commits}")
    print(f"Saved results to {filepath}")
except Exception as e:
    print("GraphQL query failed:", e)
