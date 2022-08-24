from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters'
        if len(form['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 3 characters'
        if not EMAIL_REGEX.match(form['email_address']):
            errors['email_address'] = 'Invalid Email Address'
        email_check = self.filter(email_address=form['email_address'])
        if email_check:
            errors['email_address'] = "Email already in use"
        if len(form['password']) < 8:
            errors['password'] = 'Password must be atleast 8 characters'
        if form['password'] != form['confirm']:
            errors['password']= 'Passwords do not match'
        return errors

    def authenticate(self, email_address, password):
        users = self.filter(email_address=email_address)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email_address = form['email_address'],
            password = pw,
        )

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Note(models.Model):
    note = models.TextField()
    user= models.ForeignKey(User, related_name="note", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)