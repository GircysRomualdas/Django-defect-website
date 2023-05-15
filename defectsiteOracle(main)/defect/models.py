from django.db import models

class Location(models.Model):
    nID = models.AutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    sDescription = models.TextField(max_length=254)
    nParentID = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return   self.sName


class Type(models.Model):
    nID = models.AutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    sDescription = models.TextField(max_length=254)
    nParentID = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return   self.sName

class Position(models.Model):
    nID = models.AutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    sDescription = models.TextField(max_length=254)
    nParentID = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return   self.sName

class LocationType(models.Model):
    nLocationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    nTypeID = models.ForeignKey(Type, on_delete=models.CASCADE)
    nHidden = models.IntegerField(null=True, blank=True)
    dtCreated_at = models.DateTimeField(auto_now_add=True, verbose_name="date creted")
    dtUpdatedAt = models.DateTimeField(auto_now=True, verbose_name="date updated")

    def __str__(self):
        return  str(self.nLocationID) + ' ' + str(self.nTypeID)
    
    class Meta:
        unique_together = (('nLocationID','nTypeID'),)

class TypePosition(models.Model):
    nTypeID = models.ForeignKey(Type, on_delete=models.CASCADE)
    nPositionID = models.ForeignKey(Position, on_delete=models.CASCADE)
    nHidden = models.IntegerField(null=True, blank=True)
    dtCreated_at = models.DateTimeField(auto_now_add=True, verbose_name="date creted")
    dtUpdatedAt = models.DateTimeField(auto_now=True, verbose_name="date updated")

    def __str__(self):
        return  str(self.nTypeID) + ' ' + str(self.nPositionID)
    
    class Meta:
        unique_together = (('nTypeID','nPositionID'),)

