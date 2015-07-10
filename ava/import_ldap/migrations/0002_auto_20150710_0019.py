# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_ldap', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activedirectorygroup',
            options={'ordering': ['cn', 'distinguished_name']},
        ),
        migrations.AlterModelOptions(
            name='activedirectoryuser',
            options={'ordering': ['cn', 'distinguished_name']},
        ),
        migrations.RenameField(
            model_name='activedirectorygroup',
            old_name='distinguishedName',
            new_name='distinguished_name',
        ),
        migrations.RenameField(
            model_name='activedirectorygroup',
            old_name='objectCategory',
            new_name='object_category',
        ),
        migrations.RenameField(
            model_name='activedirectorygroup',
            old_name='objectGUID',
            new_name='object_guid',
        ),
        migrations.RenameField(
            model_name='activedirectorygroup',
            old_name='objectSid',
            new_name='object_sid',
        ),
        migrations.RenameField(
            model_name='activedirectorygroup',
            old_name='sAMAccountName',
            new_name='sam_account_name',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='accountExpires',
            new_name='account_expires',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='adminCount',
            new_name='admin_count',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='badPasswordTime',
            new_name='bad_password_time',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='badPwdCount',
            new_name='bad_pwd_count',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='displayName',
            new_name='display_name',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='distinguishedName',
            new_name='distinguished_name',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='isCriticalSystemObject',
            new_name='is_critical_system_object',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='lastLogoff',
            new_name='last_logoff',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='lastLogon',
            new_name='last_logon',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='lastLogonTimestamp',
            new_name='last_logon_timestamp',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='logonCount',
            new_name='logon_count',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='logonHours',
            new_name='logon_hours',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='objectGUID',
            new_name='object_guid',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='objectSid',
            new_name='object_sid',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='primaryGroupID',
            new_name='primary_group_id',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='pwdLastSet',
            new_name='pwd_last_set',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='sAMAccountName',
            new_name='sam_account_name',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='sAMAccountType',
            new_name='sam_account_type',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='uSNChanged',
            new_name='user_account_control',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='uSNCreated',
            new_name='usn_changed',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='userAccountControl',
            new_name='usn_created',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='whenChanged',
            new_name='when_changed',
        ),
        migrations.RenameField(
            model_name='activedirectoryuser',
            old_name='whenCreated',
            new_name='when_created',
        ),
        migrations.AlterUniqueTogether(
            name='activedirectorygroup',
            unique_together=set([('object_guid', 'object_sid')]),
        ),
        migrations.AlterUniqueTogether(
            name='activedirectoryuser',
            unique_together=set([('object_guid', 'object_sid')]),
        ),
    ]
