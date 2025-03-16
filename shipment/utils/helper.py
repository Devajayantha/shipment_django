import random
import string

def generate_tracking_number():
    return 'SM' .join(random.choices(string.ascii_uppercase + string.digits, k=10))