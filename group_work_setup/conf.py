PASSWORD = ''
ORGANIZATION_NAME = 'rmotr'
COURSES_OPTIONS = ['pyp']

TEAM_NAME_TEMPLATE = "b{batch}-{course}-g{group}-{team_name}"
MAIN_REPO_NAME_TEMPLATE = '{course}-c{_class}-a{assignment}'
TEAM_REPO_NAME_TEMPLATE = (
    MAIN_REPO_NAME_TEMPLATE + '-'
    'b{batch}-g{group}-{team_name}')
