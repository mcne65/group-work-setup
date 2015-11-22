import itertools
from github3 import login

from . import utils


def get_organization(org_login, user):
    iter = itertools.dropwhile(
        lambda org: org.login != org_login, user.iter_orgs())
    for org in iter:
        return org


def create_repo_in_organization(organization, name, description=None,
                                homepage='', private=False, has_issues=True,
                                has_wiki=True, has_downloads=True,
                                auto_init=False, gitignore_template=''):
    return organization.create_repo(
        name, description=description, homepage=homepage,
        private=private, has_issues=has_issues,
        has_wiki=has_wiki, has_downloads=has_downloads,
        auto_init=auto_init, gitignore_template=gitignore_template)


def create_repos_for_team_name(organization, configuration, team_name):
    repos = []
    for assignment in configuration.assignments:
        repo_name = utils.generate_repo_name_for_team(
            batch=configuration.batch, course=configuration.course,
            group=configuration.group, _class=configuration.clazz,
            assignment=assignment.name, team_name=team_name)

        repo = create_repo_in_organization(organization, repo_name)
        repos.append(repo)

    return repos


def create_team_for_repos(organization, configuration, team_name,
                          repo_names, permission='push'):
    team_name = utils.generate_team_name(
        batch=configuration.batch, course=configuration.course,
        group=configuration.group, team_name=team_name)
    team = organization.create_team(
        team_name, repo_names=repo_names, permission=permission)

    return team


def get_repo_names_from_repos(repos):
    return ['{}/{}'.format(repo.owner.login, repo.name) for repo in repos]


def create_team_and_repos(organization, configuration, team):
    repos = create_repos_for_team_name(organization, configuration, team.name)
    repo_names = get_repo_names_from_repos(repos)
    github_team = create_team_for_repos(
        organization, configuration, team.name, repo_names)
    [github_team.invite(p) for p in team.participants_names]

    return github_team, repos


def create_teams_and_repos_for_assignments(user, password, configuration):
    gh = login(user, password=password)
    user = gh.user()
    org = get_organization(configuration.organization, user)

    teams = []
    for _team in configuration.teams:
        team, repos = create_team_and_repos(
            org, configuration, _team)
        teams.append({
            'team': team,
            'repos': repos
        })

    return teams
