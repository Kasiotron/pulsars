from django.db import models


class Observation(models.Model):
    start_datetime = models.DateField(null=True, help_text="")
    frequency = models.FloatField(null=True, help_text="")
    length = models.FloatField(null=True, help_text="")
    pulses = models.IntegerField(null=True, help_text="")


class Pulsar(models.Model):
    def __str__(self):
        return "{}".format(self.NAME)
    NAME = models.CharField(max_length=200, help_text="Pulsar name.  The B name if exists, otherwise the J name.", null=True)
    P0 = models.DecimalField(max_digits=32, decimal_places=30, null=True, help_text="Barycentric period of the pulsar (s)")
    P1 = models.FloatField(null=True, help_text="Time derivative of barcycentric period (dimensionless)")
    F0 = models.DecimalField(max_digits=36, decimal_places=30, null=True, help_text="Barycentric rotation frequency (Hz)")
    F1 = models.FloatField(null=True, help_text="Time derivative of barycentric rotation frequency (s-2)")
    F2 = models.FloatField(null=True, help_text="Second time derivative of barycentric rotation frequency (s-3)")
    F3 = models.FloatField(null=True, help_text="Second time derivative of barycentric rotation frequency (s-4)")
    DM = models.FloatField(null=True, help_text="Dispersion measure (cm-3 pc)")
    DM1 = models.FloatField(null=True, help_text="First time derivative of dispersion measure (cm-3 pc yr-1)")
    RM = models.FloatField(null=True, help_text="Rotation measure (rad m-2)")
    W50 = models.FloatField(null=True, help_text="Width of pulse at 50% of peak (ms).")
    W10 = models.FloatField(null=True, help_text="Width of pulse at 10% (ms).")
    S400 = models.FloatField(null=True, help_text="Mean flux density at 400 MHz (mJy)")
    S1400 = models.FloatField(null=True, help_text="Mean flux density at 1400 MHz (mJy)")
    S2000 = models.FloatField(null=True, help_text="Mean flux density at 2000 MHz (mJy)")
    DIST = models.FloatField(null=True, help_text="Best estimate of the pulsar distance using the YMW16 DM-based distance as default (kpc)")
    AGE = models.FloatField(null=True, help_text="Spin down age (yr)")
    BSURF = models.FloatField(null=True, help_text="Surface magnetic flux density (Gauss)")
    EDOT = models.FloatField(null=True, help_text="Spin down energy loss rate (ergs/s)")
    P0_rr = models.FloatField(null=True, help_text="")
    P1_rr = models.FloatField(null=True, help_text="")
    F1_rr = models.FloatField(null=True, help_text="")
    F2_rr = models.FloatField(null=True, help_text="")
    F3_rr = models.FloatField(null=True, help_text="")
    DM_rr = models.FloatField(null=True, help_text="")
    DM1_rr = models.FloatField(null=True, help_text="")
    RM_rr = models.FloatField(null=True, help_text="")
    W50_rr = models.FloatField(null=True, help_text="")
    W10_rr = models.FloatField(null=True, help_text="")
    S400_rr = models.FloatField(null=True, help_text="")
    S1400_rr = models.FloatField(null=True, help_text="")
    S2000_rr = models.FloatField(null=True, help_text="")

    observations = models.ManyToManyField(Observation)
