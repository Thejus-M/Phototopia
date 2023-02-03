from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
  """Model definition for Pictures."""

  # TODO: Define fields here
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  picture_id = models.AutoField(primary_key=True)
  picture_like = models.IntegerField()
  picture_random_code = models.BigIntegerField()
  pic = models.ImageField(upload_to='photos')
  class Meta:
    """Meta definition for Pictures."""

    verbose_name = 'Picture'
    verbose_name_plural = 'Pictures'

  def __str__(self):
    """Unicode representation of Pictures."""
    return f" {self.user} id-{self.picture_like} "


class UserInfo(models.Model):
  """Model definition for UserInfo."""

  # TODO: Define fields here
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  user_info_id = models.AutoField(primary_key=True)
  user_pic = models.ManyToManyField(Picture)
  profile_picture = models.ImageField(upload_to='user_images')

  class Meta:
    """Meta definition for UserInfo."""

    verbose_name = 'UserInfo'
    verbose_name_plural = 'UserInfos'

  def __str__(self):
    return f"{self.user} id-{self.user_info_id}"
