from pathlib import Path
from datetime import datetime
from lib.misc import errors
from lib.gui import main

date = str(datetime.now().strftime("[%d.%m.%Y][%H.%M.%S]"))
path = str(Path(__file__).resolve().parent)

if __name__ == "__main__":
    main()

    if len(errors) > 0:
        Path(f"{path}/logs/").mkdir(parents=True, exist_ok=True)
        error_log = open(f"{path}/logs/log {date}.log", "w")

        error_log.write(f"log {date}.log\n[day.month.year][hours.minutes.seconds]\n")

        for error in errors:
            error_log.write(f"\n[{'='*30}]\n\n{str(error)}")
        error_log.close()
