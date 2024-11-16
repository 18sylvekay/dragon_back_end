import datetime

import pytz

from project.dragons.models import Dragon


def calculate_level(obj: Dragon):
    current_date = datetime.datetime.now(pytz.UTC)
    delta = current_date - obj.date_created

    print('date created', obj.date_created)

    # Calculate full weeks since date created
    return delta.days // 7
