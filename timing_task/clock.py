from datetime import date, datetime

import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print("tick ! the time is : %s" % datetime.now())
    os.system("python3 ..\\create_file.py")


if __name__ == "__main__":
    scheduler = BackgroundScheduler(timezone='Asia/Shanghai')

    # scheduler.add_job(tick, 'interval', days=1, start_date="2021-2-19 5:00:00")
    scheduler.add_job(tick, 'interval', seconds=15, start_date=datetime.today())

    scheduler.start()

    print("Press Ctrl + {0} to exit".format('Break' if os.name == 'nt' else 'C'))
    try:
        while True:
            time.sleep(60)
            print(f"sleep! - {datetime.now()}")
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Exit The Job !")
