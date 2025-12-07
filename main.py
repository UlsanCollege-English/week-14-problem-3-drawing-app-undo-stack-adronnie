def simulate_history(actions):
    stack = []  # this will store the active actions

    for action in actions:
        if action == "UNDO":
            if stack:
                stack.pop()   # undo last action
        else:
            stack.append(action)  # normal action

    return stack  # final remaining actions
