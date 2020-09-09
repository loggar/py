import asyncio
import time


def print_company_info(company):
    time.sleep(1)
    print(time.ctime(), company)


companies = ['ABT', 'ABBV', 'ABMD', 'ATVI', 'ADBE']
tasks = []

event_loop = asyncio.get_event_loop()

for company in companies:
    # Not calling the functions here, we are storing an awaitable functions in an array
    tasks.append((print_company_info(company)))

started = time.time()
event_loop.run_until_complete(asyncio.wait(tasks))
elapsed = time.time()
