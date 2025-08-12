def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    def beat(move):
        return {'R': 'P', 'P': 'S', 'S': 'R'}[move]

    if not opponent_history:
        player.prev_move = 'R'
        return 'R'

    counts = {'R': 0, 'P': 0, 'S': 0}
    for m in opponent_history:
        counts[m] += 1

    most_freq_move = max(counts, key=counts.get)
    strategy1 = beat(most_freq_move)

    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2]:
        strategy2 = beat(opponent_history[-1])
    else:
        strategy2 = strategy1

    def detect_cycle(history):
        n = len(history)
        for cycle_len in [2, 3]:
            if n >= cycle_len * 2:
                cycle = history[-cycle_len:]
                if history[-2*cycle_len:-cycle_len] == cycle:
                    return cycle[0]  # predict cycle start
        return None

    cycle_pred = detect_cycle(opponent_history)
    if cycle_pred:
        strategy3 = beat(cycle_pred)
    else:
        strategy3 = strategy2

    if player.prev_move and opponent_history[-1] == beat(player.prev_move):
        strategy4 = beat(opponent_history[-1])
    else:
        strategy4 = strategy3

    player.prev_move = strategy4
    return strategy4

player.prev_move = None
