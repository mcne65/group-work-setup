import json


class Configuration(object):
    @classmethod
    def read_from_file(cls, conf_file):
        conf = json.load(conf_file)

        return cls(
            organization=conf['organization'],
            course=conf['course'],
            clazz=conf['class'],
            batch=conf['batch'],
            group=conf['group'],

            teams=conf['teams'],
            assignments=conf['assignments'],
            conf_json=conf)

    def __init__(self, organization, course, clazz,
                 batch, group, teams, assignments,
                 conf_json=None):

        self.organization = organization
        self.course = course
        self.clazz = clazz
        self.batch = batch
        self.group = group

        self._teams = teams
        self._assignments = assignments
        self._conf_json_raw = conf_json

        self.memoized_teams = []
        self.memoized_assignments = []

    @property
    def teams(self):
        if self.memoized_teams:
            return self.memoized_teams

        for team in self._teams:
            self.memoized_teams.append(Team(
                name=team['name'],
                participants_names=team['participants']))

        return self.memoized_teams

    @property
    def assignments(self):
        if self.memoized_assignments:
            return self.memoized_assignments

        for assignment in self._assignments:
            self.memoized_assignments.append(Assignment(
                name=assignment['name'],
                repo=assignment['repo'],
                organization=assignment['organization']))

        return self.memoized_assignments


class Team(object):
    def __init__(self, name, participants_names):
        self.name = name
        self.participants_names = participants_names


class Assignment(object):
    def __init__(self, name, repo, organization):
        self.name = name
        self.repo = repo
        self.organization = organization
