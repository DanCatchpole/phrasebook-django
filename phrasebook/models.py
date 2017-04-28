from django.db import models
from django.contrib.auth import models as auth_modules
from django.utils.timezone import now


class Language(models.Model):
    name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    flag_name = models.CharField(max_length=3)
    color = models.CharField(max_length=7)
    hello = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " (" + self.english_name + ")"


class Category(models.Model):
    name = models.CharField(max_length=200)
    shortened = models.CharField(max_length=3)
    description = models.TextField(default="")
    created_on = models.DateTimeField('date created', default=now)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(auth_modules.User, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + self.language.flag_name + ")"


class Word(models.Model):
    foreign = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField('date created', default=now)
    starred = models.BooleanField(default=False)

    def __str__(self):
        return self.foreign + " = " + self.english


class UserLanguage(models.Model):
    user = models.ForeignKey(auth_modules.User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " - " + self.language.flag_name


class UserProgress(models.Model):
    user = models.ForeignKey(auth_modules.User, on_delete=models.CASCADE)
    level = models.IntegerField()
    xp = models.BigIntegerField()

    def __str__(self):
        return self.user.username + " - level " + str(self.level) + ", Total XP: " + str(self.xp)


class UserIcon(models.Model):
    user = models.ForeignKey(auth_modules.User, on_delete=models.CASCADE)
    icon = models.URLField()
