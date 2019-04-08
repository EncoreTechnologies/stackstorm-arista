from st2common.runners.base_action import Action
import json


class FilterCli(Action):

    def run(self, cli_result, command):
        results = []
        for r in cli_result:
            if command in r:
                parsed = json.loads(r[command])
                results.append(parsed)
        return results
