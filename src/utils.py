import re
import ast

def parse_json(response):
    matches = re.findall(r'```json(.*?)```', response, re.DOTALL)

    if len(matches) > 0:
        return ast.literal_eval(matches[0].strip())
    else:
        return None