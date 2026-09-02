import json
import unittest
import time
import os

class JSONTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.results = {
            'passed': [],
            'failed': []
        }

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results['passed'].append(
            {
                'status': 'success',
                'test_scenario_name': test._testMethodName
            }
        )

    def addError(self, test, err):
        super().addError(test, err)
        failed_output = self._exc_info_to_string(err, test).split('\n')[-2]
        self.results['failed'].append(
            {
                'status': 'error',
                'test_scenario_name': test._testMethodName,
                'message': failed_output
            }
        )

    def addFailure(self, test, err):
        super().addFailure(test, err)
        failed_output = self._exc_info_to_string(err, test).split('\n')[-2]
        self.results['failed'].append(
            {
                'status': 'failure',
                'test_scenario_name': test._testMethodName,
                'message': failed_output
            }
        )

    def addSkip(self, test, err):
        super().addSkip(test, err)
        failed_output = self._exc_info_to_string(err, test).split('\n')[-2]
        self.results['failed'].append(
            {
                'status': 'skip',
                'test_scenario_name': test._testMethodName,
                'message': failed_output
            }
        )


class JSONTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def run_tests():
    ARTIFACTS_PATH = "./common"

    test_dir = 'tests'
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()
    suite.addTests(loader.discover(test_dir))


    runner = JSONTestRunner(verbosity = 2, resultclass=JSONTestResult)
    start_time = time.time()
    result = runner.run(suite)
    end_time = time.time()

    structure_data = {
        'results': result.results,
        'time_taken': round(end_time - start_time, 3),
    }

    file_path = os.path.join(ARTIFACTS_PATH,'python-test-json-test-runner.json')
    with open(file_path, 'w') as structure_json_output_file:
        json.dump(structure_data,structure_json_output_file,indent=2)


if __name__ == '__main__':
    run_tests()