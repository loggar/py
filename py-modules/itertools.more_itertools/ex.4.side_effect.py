import more_itertools

num_events = 0


def _increment_num_events(_):
    nonlocal num_events
    num_events += 1


# Iterator that will be consumed
event_iterator = more_itertools.side_effect(_increment_num_events, events)

more_itertools.consume(event_iterator)

print(num_events)
