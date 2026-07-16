"""Lightweight scheduler: runs periodic jobs (currently: Telegram review reminders).

Runs every REMINDER_TICK_SECONDS; send_due_reminders is idempotent per user/day
(guarded by last_reminded_date and the user's local reminder hour).
"""
import time

from app.db.session import SessionLocal
from app.services.motivation_service import send_due_reminders

REMINDER_TICK_SECONDS = 300


def tick() -> None:
    db = SessionLocal()
    try:
        sent = send_due_reminders(db)
        if sent:
            print(f'[scheduler] sent {sent} reminder(s)')
    except Exception as exc:  # keep the loop alive
        print(f'[scheduler] error: {exc}')
    finally:
        db.close()


def main() -> None:
    print('Scheduler started: review reminders every', REMINDER_TICK_SECONDS, 's')
    while True:
        tick()
        time.sleep(REMINDER_TICK_SECONDS)


if __name__ == '__main__':
    main()
