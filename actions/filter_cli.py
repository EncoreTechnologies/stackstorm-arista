from st2common.runners.base_action import Action
import json


class FilterCli(Action):

    def run(self, cli_result, command, hosts, raw):
        results = []
        for idx, r in enumerate(cli_result):
            if command in r:
                output = r[command].replace('\\n', '\n')
                if not raw:
                    output = json.loads(output)
                results.append({'host': hosts[idx],
                                'command': command,
                                'result': output})
        return results
