import sh
from sh import git, ls, pwd, cd, ErrorReturnCode

BATCH = "b4"
GROUP = "g2"
# TEAMS = ["t2", "t3"]
TEAMS = ["t3"]
REPOS = ["pyp-c3-a1"]

for team in TEAMS:
    for repo in REPOS:
        team_repo_name = "{repo}-{batch}-{group}-{team}".format(
            repo=repo, batch=BATCH, group=GROUP, team=team)
        team_repo_git_url = "git@github.com:rmotr/{}.git".format(
            team_repo_name)

        with sh.pushd(repo):
            git.remote.add(team_repo_name, team_repo_git_url)
            try:
                out = git.push(team_repo_name, 'master')
                print(out.stdout or out.stderr)
            except ErrorReturnCode as e:
                pass
            finally:
                git.remote.remove(team_repo_name)
