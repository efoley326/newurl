from django.conf import settings
from random import choice
from string import ascii_letters, digits



AVAILABLE_CHARS = (ascii_letters + digits)

def create_random_url(chars=AVAILABLE_CHARS):
    return ("emily." + str("").join(
        [choice(chars) for _ in range(7)]
    )
)