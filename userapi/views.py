from django.http import JsonResponse
from datetime import datetime

# Importing Models.

from .models import User , ActivityPeriod

#Date format according to requirement 

DATE_FORMAT = '%b %d %Y %I:%M%p'


def GetMembers(request):
    response_dict=dict()

    Members = User.objects.all()

    # Checking if any member is there , if not return with 'ok' as false

    if(Members):

        # Set 'ok' as true
        response_dict['ok']='true'

        for user in Members:

            # Declare members as list before first entry

            if('members' not in response_dict):
                response_dict['members']=list()

            # Append user info and activity periods in required JSON format
            response_dict['members'].append({ 
                'id':user.id ,
                'real_name':user.real_name ,
                'tz':str(user.tz),
                'activity_periods':[
                    { 
                    'start_time': datetime.strftime(period.start_time ,DATE_FORMAT),
                    'end_time' : datetime.strftime(period.end_time,DATE_FORMAT) 
                    } for period in ActivityPeriod.objects.filter(User=user).order_by('start_time') ]
                    })
    else:
        # Set 'ok' as false when no members are present
        response_dict['ok']='false'


    return JsonResponse(response_dict,safe=False)