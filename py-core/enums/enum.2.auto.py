from enum import Enum, auto


class TaskStatus(Enum):
    NOT_STARTED = auto()
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    CLOSED = auto()


print(TaskStatus.TODO)
print(TaskStatus.TODO.name)
print(TaskStatus.TODO.value)
print(isinstance(TaskStatus.TODO, Enum))
print(isinstance(TaskStatus.TODO, TaskStatus))

print(list(TaskStatus))

num_statuses = len(TaskStatus)
print("num_statuses:", num_statuses)

for status in TaskStatus:
    print(status.value, status.name)
