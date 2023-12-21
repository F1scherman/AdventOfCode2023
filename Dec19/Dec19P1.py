# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")


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
accepted_parts_sum = 0

for line in file:
    parameters = line.strip()[1:-1].split(",")

    x, m, a, s = 0, 0, 0, 0

    for parameter in parameters:
        exec(parameter)

    current_workflow = "in"
    while True:
        workflow = workflows[current_workflow]
        target = workflow[-1]
        for rule in workflow[:-1]:
            if eval(rule[0]):
                target = rule[1]
                break
        if target == "A":
            accepted_parts_sum += x + m + a + s
            break
        elif target == "R":
            break
        else:
            current_workflow = target

print(accepted_parts_sum)


file.close()
