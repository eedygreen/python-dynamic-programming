import os, sys, logging, traceback
from github import Github


# Get the token
access_token = os.getenv("GITHUB_TOKEN") 
file = "versions"
mesg = ""
url = "eedygreen/eedygreen.github.io"
branch = "new_update"

# Authenticate to Github
gh = Github(access_token)

# Access the repository contents
repo = gh.get_repo(url)

#logging.basicConfig(level="DEBUG") # for troubleshooting

def file_content(contents):
    return repo.get_contents(contents)

# status
def get_repo_status(contents):
    try:
        file_content(contents)
    except Exception: # the problem is in the except handlingß
        return sys.stdout.write(f"STATUS: {contents} Not Found!")

#  update
def update_repo(contents):
    new_file = f"{repo.name}/{file}"
    status   = file_content(contents)
    try:
        if not status:
            repo.create_file(new_file, "created!", mesg, branch="resume-update")
        else:
            content = file_content(contents)
            repo.update_file(content.path, f"{contents} updated!", mesg, content.sha, branch="resume-update" )
    except Exception:
        logging.raiseExceptions



# create pull_request
def create_pull_request(contents: str):
    repo.create_pull(title=contents, body=contents, head=branch, base="master")

def main():
    update_repo(file)
    create_pull_request("recent_update")

if __name__ == "__main__":
    main()