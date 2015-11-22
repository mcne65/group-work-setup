import json
import unittest
try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO
from main import Configuration, Team, Assignment


SAMPLE_TEAM_CONFIGURATION = {
    "organization": "rmotr",
    "course": "pyp",
    "class": 1,
    "batch": 4,
    "group": 1,

    "assignments": [
        {"organization": "rmotr", "name": "pyp-c1-a1"},
        {"organization": "rmotr", "name": "pyp-c1-a2"},
        {"organization": "rmotr", "name": "pyp-c1-a3"}
    ],
    "teams": [
        {
            "name": "t1",
            "participants": [
                "calvin1", "robert1", "david2"
            ]
        },
        {
            "name": "t1",
            "participants": [
                "brandon1", "michelle1"
            ]
        }
    ]
}


class ConfigurationReadTestCase(unittest.TestCase):
    def test_configuration_read_from_io_is_not_none(self):
        conf = Configuration.read_from_file(
            StringIO(json.dumps(SAMPLE_TEAM_CONFIGURATION)))
        self.assertIsNotNone(conf)

    def test_configuration_read_from_io_creates_attrs(self):
        conf = Configuration.read_from_file(
            StringIO(json.dumps(SAMPLE_TEAM_CONFIGURATION)))
        self.assertEqual(conf.organization, 'rmotr')
        self.assertEqual(conf.course, 'pyp')
        self.assertEqual(conf.clazz, 1)
        self.assertEqual(conf.batch, 4)
        self.assertEqual(conf.group, 1)

        self.assertEqual(
            conf._teams, SAMPLE_TEAM_CONFIGURATION['teams'])
        self.assertEqual(
            conf._assignments, SAMPLE_TEAM_CONFIGURATION['assignments'])

    def test_conf_teams(self):
        conf = Configuration.read_from_file(
            StringIO(json.dumps(SAMPLE_TEAM_CONFIGURATION)))
        self.assertEqual(len(conf.teams), 2)
        self.assertIsInstance(conf.teams[0], Team)

        self.assertEqual(conf.teams[0].name, 't1')
        self.assertEqual(
            conf.teams[0].participants_names,
            ["calvin1", "robert1", "david2"])

        self.assertEqual(conf.teams[1].name, 't1')
        self.assertEqual(
            conf.teams[1].participants_names,
            ["brandon1", "michelle1"])

    def test_conf_assignments(self):
        conf = Configuration.read_from_file(
            StringIO(json.dumps(SAMPLE_TEAM_CONFIGURATION)))
        self.assertEqual(len(conf.assignments), 3)
        self.assertIsInstance(conf.assignments[0], Assignment)

        self.assertEqual(conf.assignments[0].name, "pyp-c1-a1")
        self.assertEqual(conf.assignments[0].organization, "rmotr")

        self.assertEqual(conf.assignments[1].name, "pyp-c1-a2")
        self.assertEqual(conf.assignments[1].organization, "rmotr")

        self.assertEqual(conf.assignments[2].name, "pyp-c1-a3")
        self.assertEqual(conf.assignments[2].organization, "rmotr")
