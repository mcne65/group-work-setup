import unittest


TEST_DATA = {
    "113040": {
        "2002-2008": [
            ('"0"', ['"F"', '"69"-"0"']),
            ('"1"', ['"D"', '"76"-"70"']),
            ('"2"', ['"C"', '"84"-"77"']),
            ('"3"', ['"B"', '"92"-"85"']),
            ('"4"', ['"A"', '"100"-"93"'])
        ],
        "2009-2025": [
            ('"0"', ['"F"', '"69"-"0"']),
            ('"1"', ['"D"', '"73"-"70"']),
            ('"2"', ['"C"', '"79"-"74"']),
            ('"3"', ['"B"', '"89"-"80"']),
            ('"4"', ['"A"', '"110"-"90"'])
        ]
    }
}

EXPECTED_GRADES = {'A': {'2002-2008': '"100"-"93"', '2009-2025': '"110"-"90"'},
                   'B': {'2002-2008': '"92"-"85"', '2009-2025': '"89"-"80"'},
                   'C': {'2002-2008': '"84"-"77"', '2009-2025': '"79"-"74"'},
                   'D': {'2002-2008': '"76"-"70"', '2009-2025': '"73"-"70"'},
                   'F': {'2002-2008': '"69"-"0"', '2009-2025': '"69"-"0"'}}


def get_grades_for_key(grading_data):
    results = {}

    for year_range, grades in grading_data.items():
        for _id, grade_values in grades:
            grade_letter = grade_values[0].replace('"', '').replace("'", '')
            results.setdefault(grade_letter, {})
            results[grade_letter][year_range] = grade_values[1]
    return results


def get_grades(data):
    return {k: get_grades_for_key(v) for k, v in data.items()}


class GradingTestCase(unittest.TestCase):
    def test_get_grades_by_key(self):
        grades = get_grades_for_key(TEST_DATA["113040"])

        self.assertEqual(grades, EXPECTED_GRADES)

    def test_get_all_grades(self):
        grades = get_grades(TEST_DATA)
        expected = {
            "113040": EXPECTED_GRADES
        }

        self.assertEqual(grades, expected)
