import sh
from sh import git, ErrorReturnCode, rm

BATCH = "b4"
GROUP = "g3"
TEAMS = ["t1", "t2", "t3", "t4"]
ASSIGNMENTS_ORGANIZATION = 'rmotr'
TEAM_ORGANIZATION = 'rmotr-group-assignments'
REPOS = ["pyp-c1-a1", "pyp-c1-a2", "pyp-c1-a3"]


def push_for_teams(teams, repo):
    for team in teams:
        print("\t Pushing changes for team {}".format(team))
        team_repo_name = "{repo}-{batch}-{group}-{team}".format(
            repo=repo, batch=BATCH, group=GROUP, team=team)
        team_repo_git_url = "git@github.com:{org}/{repo}.git".format(
            org=TEAM_ORGANIZATION, repo=team_repo_name)

        with sh.pushd(repo):
            git.remote.add(team_repo_name, team_repo_git_url)
            try:
                out = git.push(team_repo_name, 'master')
                print(out.stdout or out.stderr)
            except ErrorReturnCode as e:
                pass
            finally:
                git.remote.remove(team_repo_name)


for repo in REPOS:
    repo_git_url = "git@github.com:{org}/{repo}.git".format(
        org=ASSIGNMENTS_ORGANIZATION, repo=repo)
    print("Cloning repo {}".format(repo))
    git.clone(repo_git_url)

    print("Repo cloned. Pushing to teams")
    push_for_teams(TEAMS, repo)
    print("All pushed. deleting repo")

    # delete repo
    rm("-Rf", repo)
    print("{} done!".format(repo))
