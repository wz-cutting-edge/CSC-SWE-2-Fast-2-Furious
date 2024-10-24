# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

#library archive tables from project database
class Users(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, username) found, that is not supported. The first column is selected.
    username = models.CharField(max_length=255)
    acctype = models.CharField(db_column='accType', max_length=5)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('userid', 'username'),)

class Library(models.Model):
    mediaid = models.AutoField(db_column='mediaID', primary_key=True)  # Field name made lowercase.
    title = models.TextField()
    author = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=11)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library'

class CurrentRentals(models.Model):
    media = models.ForeignKey('Library', models.DO_NOTHING, db_column='media_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    borrowerid = models.ForeignKey('Users', models.DO_NOTHING, db_column='borrowerID', blank=True, null=True)  # Field name made lowercase.
    borrowername = models.ForeignKey('Users', models.DO_NOTHING, db_column='borrowerName', to_field='username', related_name='currentrentals_borrowername_set', blank=True, null=True)  # Field name made lowercase.
    rental_start = models.DateTimeField(db_column='rental_Start', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'current_rentals'

class TagToMedia(models.Model):
    mediaid = models.ForeignKey(Library, models.DO_NOTHING, db_column='mediaID')  # Field name made lowercase.
    tagid = models.ForeignKey('Tags', models.DO_NOTHING, db_column='tagID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tag_to_media'


class Tags(models.Model):
    tagid = models.AutoField(db_column='tagID', primary_key=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='tagName', max_length=255)  # Field name made lowercase.
    genre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


