import os
import random
from .models import pokeneas


def get_random_pokenea():
    return random.choice(pokeneas)


def get_container_id():
    return os.uname()[1]
