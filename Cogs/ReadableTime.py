def getReadableTimeBetween(first, last):
    # A helper function to make a readable string between two times
    timeBetween = int(last-first)
    days    = int(timeBetween/86400)
    hours   = int((timeBetween-(days*86400))/3600)
    minutes = int((timeBetween-(hours*3600 + days*86400))/60)
    seconds = int(timeBetween-(minutes*60 + hours*3600 + days*86400))
    msg = ""
    if days > 0:
        if days == 1:
            msg = '{}{} day, '.format(msg, str(days))
        else:
            msg = '{}{} days, '.format(msg, str(days))
    if hours > 0:
        if hours == 1:
            msg = '{}{} hour, '.format(msg, str(hours))
        else:
            msg = '{}{} hours, '.format(msg, str(hours))
    if minutes > 0:
        if minutes == 1:
            msg = '{}{} minute, '.format(msg, str(minutes))
        else:
            msg = '{}{} minutes, '.format(msg, str(minutes))
    if seconds == 1:
        msg = '{}{} second, '.format(msg, str(seconds))
    else:
        msg = '{}{} seconds, '.format(msg, str(seconds))

    return msg[:-2]	