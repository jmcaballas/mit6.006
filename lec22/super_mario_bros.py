def super_mario_bros(config):
    DP = {}

    for current_config in config:
        if on_flag(current_config):
            DP[current_config] = current_config["score"]
            continue

        if current_config["dead"] or current_config["time"] == 0:
            DP[current_config] = float("inf")
            continue

        max_score = float("-inf")
        for action in actions:
            new_config = apply_action(current_config, action)
            max_score = max(max_score, DP.get(new_config, 0))

        DP[current_config] = max_score

    return DP[config[0]]
