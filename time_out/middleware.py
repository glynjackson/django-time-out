# Django/Python imports
from datetime import datetime
from django.shortcuts import render_to_response

# App imports
from .models import MaintenanceSchedule


def get_current_time():
    """
    Determine what the current time.
    :return: Time data object.
    """
    return datetime.now()


class DownTimeMiddleware(object):


    def process_request(self, request):
        """
        Hook: process_request()
        Called on each request, before Django decides which view to execute.
        :param request:
        :return:
        """
        # If the admin then don't show maintenance page.
        if request.path.startswith("/admin"):
            return None

        # Filter all objects
        now = get_current_time()
        objects = MaintenanceSchedule.objects.filter(start_time__lt=now, end_time__gt=now, active=True)

        if objects.count() > 0:
            # If we have more than one.
            maintenance = objects[0]

            abort_request = True

            if abort_request:
                context = {'maintenance': maintenance}
                return render_to_response('down_time/down_time.html', context)

        return None




























