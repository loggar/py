from enum import Enum


class TaskStatus(Enum):
    NOT_STARTED = 0
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3
    CLOSED = 4


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
