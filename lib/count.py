def count(start, stop):
    toreturn = ""
    if start < stop:
        while start < stop:
            toreturn += str(start) + ","
            start += 1
        toreturn += str(stop)
    else:
        while start > stop:
            toreturn += str(start) + ","
            start -= 1
        toreturn += str(stop)
    return toreturn

print count(4,13)