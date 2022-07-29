from django.db import models

# Create your models here.


class Member(models.Model):
    mb_id = models.CharField(max_length=30, unique=True)
    # pwd = models.
    mb_nm = models.CharField(max_legth=50)
    phone = models.IntegerField()
    mb_type = models.CharField(max_length=2)
    total_point = models.IntegerField()


class Guide(models.Model):
    mb_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    guide_profile = models.ImageField()
    star_rate = models.IntegerField()
    review_count = models.PositiveIntegerField()
    tour_sta_time = models.TimeField()
    tour_end_time = models.TimeField()
    car_tour_yn = models.CharField(max_length=1)
    camp_tour_yn = models.CharField(max_length=1)
    etc = models.TextField()


class Guide_Lang(models.Model):
    guide_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    # lang_cd =


class GuideMatching(models.Model):
    user_mb_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    guide_mb_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    tour_type = models.CharField()  # choices
    tour_sta_time = models.TimeField()
    tour_end_time = models.TimeField()
    tour_day = models.DateField()
