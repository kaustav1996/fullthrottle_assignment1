from django.core.management.base import BaseCommand, CommandError
from userapi.models import User , ActivityPeriod
from datetime import datetime
import json

# Date format used in required JSON

DATE_FORMAT = '%b %d %Y %I:%M%p'

class Command(BaseCommand):

    help = '''
  Populates Dummy Data from JSON files [ Format : same as 'Test JSON.json']
    '''

    def add_arguments(self, parser):

        # Required Argument is JSON file 
        parser.add_argument('input_jsons', nargs='+', type=str)

    def handle(self, *args, **options):
            
            # Reading imput JSONs
            for input_json in options['input_jsons']:
                with open(input_json) as f:
                    data = json.load(f)
                    # For each member element :
                    for member in data['members']:
                        # Adding User
                        user=User(
                            id=member['id'] , 
                            real_name=member['real_name'] , 
                            tz = member['tz'])
                        user.save()
                        self.stdout.write(self.style.SUCCESS('Successfully added member : '+ member['id']))
                        # For each period under a member element : 
                        for activity_period in member['activity_periods']:
                            # Adding activity periods
                            activity_period=ActivityPeriod(
                                User=user,
                                start_time=datetime.strptime(activity_period['start_time'],DATE_FORMAT),
                                end_time=datetime.strptime(activity_period['end_time'],DATE_FORMAT)
                                )
                            activity_period.save()
                        self.stdout.write(self.style.SUCCESS('Successfully added activity periods for '+ member['id']))

            
