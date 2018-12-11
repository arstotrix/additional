def getstats():
    a = 5
    b = 10
    return a, b

def playgame(a, b):
    a = a * 2
    b = b * 2
    return a, b

def main():
    playgame(getstats())
    
    
