from st2common.runners.base_action import Action
import six


class FilterAnsible(Action):

    def run(self, result, tasks):
        extracted = []

        for play in result['plays']:
            for task in play['tasks']:
                task_name = task['name']
                task_extract_details = next(t for t in tasks if t['name'] == task_name)
                if not task_extract_details:
                    continue

                task_extract = {}
                for host, vars_dict in six.iteritems(task['hosts']):
                    if task_extract_details['vars']:
                        task_extract[host] = {}
                        for var in task_extract_details['vars']:
                            task_extract[host][var] = vars_dict[var]
                    else:
                        task_extract[host] = vars_dict

                extracted.extend(task_extract)

        success = True if extracted else False
        return (success, extracted)
