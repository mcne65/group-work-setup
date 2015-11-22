"""
Repo template: pyp-c1-a1 (Python Programming - Class 1 - Assignment 1)

python main.py create_repo_and_team --team-name random-123 --batch 004 --group-name g1 --users dave1 alanjohnson brandonjames
python main.py clone_repo_from_template --batch 004 --group-name g1 --class 1 --course pyp --assignment 1 --users dave1 alanjohnson brandonjames

pyp-c1-a1-004-g1

python main.py clone_group_repos_for_class group1_conf.json --course pyp --class 1 --batch 4 --group 1

"""
PASSWORD = ''

import click

from group_work_setup.models import Configuration
from group_work_setup.github import create_teams_and_repos_for_assignments


def report(teams_created):
    from clint.textui import puts, indent, colored

    puts(colored.green("\nSuccessfuly created repo and team!\n"))
    for team_created in teams_created:
        team = team_created['team']
        repos = team_created['repos']
        organization = team.to_json()['organization']
        team_url = "https://github.com/orgs/{org}/teams/{team_name}".format(
            org=organization['login'],
            team_name=team.name)
        puts("For team {team} ({url}): ".format(
            team=colored.yellow(team.name),
            url=colored.blue(team_url)))
        for repo in repos:
            with indent(4):
                puts("Repo {name} created: {url}".format(
                    name=colored.red(repo.name),
                    url=colored.blue(repo.html_url)))
        puts("")


@click.group()
def cli():
    pass


@cli.command()
@click.argument('team_configuration', type=click.File('r'),
                required=True)
@click.option('-u', '--user', help='Your Github user', required=True)
@click.option('-p', '--password', default=PASSWORD)
# @click.option('-p', '--password', prompt=True,
#               hide_input=True, help='Your Github password',
#               default=PASSWORD, required=True)
def clone_group_repos_for_class(team_configuration, user, password):
    """
    Creates repositories for teams based on a given set of assignments
    and classes.
    It's necessary to pass a team_configuration json file to describe
    the teams that compose a given class and the reposiories to create from.
    Check team_configuration_tpl.json for an example.

    """
    conf = Configuration.read_from_file(team_configuration)

    teams_created = create_teams_and_repos_for_assignments(
        user=user, password=password, configuration=conf)
    # import ipdb; ipdb.set_trace()
    report(teams_created)


@cli.command()
@click.option('-u', '--user', help='Your Github user', required=True)
@click.option('-p', '--password', default=PASSWORD)
def test_gh(user, password):
    from github3 import login
    from group_work_setup import github
    gh = login(user, password=password)
    user = gh.user()
    org = github.get_organization('rmotr', user)
    repo = github.create_repo_in_organization(org, 'test-repo')
    # import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    cli()
