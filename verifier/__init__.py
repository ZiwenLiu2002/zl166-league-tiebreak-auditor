from contract import Task, Tool

from .checks import expected, problem, result


def verify_input(tool, value):
    Tool(tool)
    issue = problem(value)
    return result(issue is None, issue or "input is valid")


def verify_output(tool, input_value, output_value, workspace):
    Tool(tool)
    valid = output_value.standings == expected(input_value)
    return result(valid, "standings are exact" if valid else "standings or tie-break order is incorrect")


def verify_task(task, arguments, output, reference, workspace):
    Task(task)
    return verify_output("compute_standings", arguments, output, workspace)
