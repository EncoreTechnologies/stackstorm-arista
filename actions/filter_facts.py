from st2common.runners.base_action import Action


class FilterFacts(Action):

    def run(self, facts, keys):
        results = []
        for f in facts:
            filtered = {}
            for k in keys:
                filtered[k] = f[k]
            results.append(filtered)
        return results
