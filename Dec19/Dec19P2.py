# Brayden Jonsson, 2023
import helper
from collections import deque


file = open("sample_text.txt", "r")


# Format of workflows:
# {
#   workflow_title: [
#       [rule, target],
#       [rule, target],
#       ...,
#       default_target
#   ],
#   ...
# }

workflows = {}

for line in file:
    if line.strip() == "":
        break

    workflow_name, rules = line.strip().split("{")
    rule_list = rules[:-1].split(",")
    split_rule_list = [rule.split(":") if rule.find(":") > 0 else rule for rule in rule_list]

    workflows[workflow_name] = split_rule_list

# Now that the workflows are constructed, we can parse the parts


file.close()
