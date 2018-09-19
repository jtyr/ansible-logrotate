def logrotate_add_postfix(data):
    for i, v in enumerate(data):
        if isinstance(v, dict):
            logrotate_add_postfix(list(v.values())[0])
        else:
            data[i] += "!;"

    return data


class FilterModule(object):
    def filters(self):
        return {
            'logrotate_add_postfix': logrotate_add_postfix,
        }
