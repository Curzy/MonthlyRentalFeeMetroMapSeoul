from django.db import models


class Line(models.Model):
    lines = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.lines


class Station(models.Model):
    dabang_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30, unique=True)
    line = models.ManyToManyField(Line)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        info = str(self.dabang_id) + ' ' + str(self.name) + ' ' + str(self.line.all())
        return info


class Price(models.Model):

    class Meta:
        get_latest_by = 'created_at'

    station = models.ForeignKey(Station, related_name='price_history')
    deposit = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        info = str(self.station.dabang_id) + ' ' + str(self.station.name) + ' ' + str(self.deposit) + '/' + str(self.price) + ' ' + str(self.created_at)
        return info
