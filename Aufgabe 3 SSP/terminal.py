class TColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Log:
    def w(msg):
        print(f"{TColors.WARNING}{msg}{TColors.ENDC}")

    def e(msg):
        print(f"{TColors.FAIL}{msg}{TColors.ENDC}")
    
    def s(msg):
        print(f"{TColors.OKGREEN}{msg}{TColors.ENDC}")
