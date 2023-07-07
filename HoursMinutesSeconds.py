hms = []


def gethms(seconds):
    hrs = seconds // 3600
    secs = ((seconds / 3600) - hrs) * 3600
    mins = secs // 60
    secs = ((secs / 60) - mins) * 60
    hr = int(hrs)
    minu = int(mins)
    sec = int(secs)
    print(f"{hr}h {minu}m {sec}s")
