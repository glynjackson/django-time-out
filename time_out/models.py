from django.db import models


class MaintenanceSchedule(models.Model):
    """
     Maintenance Schedule Of All Tasks.
    """
    description = models.TextField(max_length=60,
                                   help_text='Short description of the maintenance work to be carried out.')
    start_time = models.DateTimeField(help_text='Date and time of planned work.')
    end_time = models.DateTimeField(help_text='Completion date and time of planned work.')
    active = models.BooleanField(default=False, help_text='Is task active, should it run?')

    def __unicode__(self):
        return self.start_time.isoformat()

