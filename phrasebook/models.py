from django.db import models
from django.contrib.auth import models as auth_modules


class Language(models.Model):
    name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    flag_name = models.CharField(max_length=3)

    @property
    def __str__(self):
        return self.name + " (" + self.english_name + ")"


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField('date created')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(auth_modules.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.language.flag_name + ")"


class Word(models.Model):
    foreign = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField('date created')

    def __str__(self):
        return self.foreign + " = " + self.english


class UserLanguage(models.Model):
    user = models.ForeignKey(auth_modules.User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " - " + self.language.flag_name


class UserIcon(models.Model):
    user = models.ForeignKey(auth_modules.User, on_delete=models.CASCADE)
    icon = models.URLField()
