import os
import re
from github import Github, GithubException

def update_star_count(readme_contents, repo_info):
    pattern = fr'\(⭐\s*\d+\)\s*\[{repo_info.name}\]'
    new_readme_line = f'(⭐ {repo_info.stargazers_count}) [{repo_info.name}]'
    return re.sub(pattern, new_readme_line, readme_contents)

def main():
    token = os.environ["GITHUB_TOKEN"]
    gh = Github(token)
    repo = gh.get_repo(os.environ["GITHUB_REPOSITORY"])

    readme = repo.get_contents("README.md")
    readme_contents = readme.decoded_content.decode("utf-8")

    repo_urls = re.findall(r'\(https://github.com/([\w-]+/[\w-]+)\)', readme_contents)

    for repo_path in repo_urls:
        try:
            repo_info = gh.get_repo(repo_path)
            readme_contents = update_star_count(readme_contents, repo_info)
        except GithubException as e:
            print(f"Error while fetching {repo_path}: {e}")
            continue

    if readme_contents != readme.decoded_content.decode("utf-8"):
        repo.update_file(
            path=readme.path,
            message="Updated star counts",
            content=readme_contents,
            sha=readme.sha,
            branch="main",
        )

if __name__ == "__main__":
    main()
