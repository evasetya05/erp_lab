# Generated by Django 5.2.3 on 2025-06-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_journalitem_credit_alter_journalitem_debit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='name',
            new_name='account_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='code',
        ),
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='balance_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='coa',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='coa_role_default',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
