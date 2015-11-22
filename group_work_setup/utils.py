from .conf import TEAM_NAME_TEMPLATE, TEAM_REPO_NAME_TEMPLATE


def generate_team_name(batch, course, group, team_name):
    return TEAM_NAME_TEMPLATE.format(
        batch=batch, course=course,
        group=group, team_name=team_name)


def generate_repo_name_for_team(batch, course, group, _class,
                                assignment, team_name):
    return TEAM_REPO_NAME_TEMPLATE.format(
        batch=batch, course=course,
        group=group, _class=_class,
        assignment=assignment, team_name=team_name)
