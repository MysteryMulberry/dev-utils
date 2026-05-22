import sys, time
from datetime import datetime, timezone

def convert(val):
    try:
        ts = float(val)
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        print(f'Unix: {ts} -> UTC: {dt.isoformat()} -> Local: {datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")}')
    except ValueError:
        dt = datetime.fromisoformat(val)
        ts = dt.timestamp()
        print(f'ISO: {val} -> Unix: {int(ts)}')

if __name__=='__main__':
    val = sys.argv[1] if len(sys.argv)>1 else str(int(time.time()))
    convert(val)
