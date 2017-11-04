from django.db import models
from django.core.urlresolvers import reverse


class UserList(models.Model):
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    area = models.CharField(max_length=25)
    zip = models.IntegerField()
    bal = models.IntegerField()
    password = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first + ' ' + self.last


class Bsnl(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class Electricity(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class Water(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class Gas(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class Cable(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class Paper(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class Telecom1(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class Telecom2(models.Model):
    aadhar = models.ForeignKey(UserList, on_delete=models.CASCADE)
    bill_date = models.DateField()
    due_date = models.DateField()
    bill = models.IntegerField()
    consumption = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return str(self.aadhar) + ' - ' + str(self.status)


class UserStack(models.Model):
    col1 = models.CharField(max_length=50)
    col2 = models.CharField(max_length=50)

    def __str__(self):
        return str(self.col1)


class Company(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class CompanyStack(models.Model):
    col1 = models.CharField(max_length=50)
    col2 = models.CharField(max_length=50)

    def __str__(self):
        return str(self.col1)

