# 
# Al Fedoruk
# COMP 1701 

def sendSOS()-> None:
    """ Send an SOS """
    send_S()
    send_O()
    send_O()

def send_S() -> None:
    print( " ... ")

def send_O()-> None:
    """ Send a Morse code O"""
    print( " --- ")


def main() -> None:
    sendSOS()

main()
