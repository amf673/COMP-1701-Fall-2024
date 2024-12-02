# 
# An example of nested for loops. 
# Print all the times in a day, to the second
# 
def main()->None:
    """ Print out the times of the day in HH:MM:SS"""
    for h in range(24):
        for m in range(60):
            for s in range(60):
                print( f"{h:02}:{m:02}:{s:02}")

main()
