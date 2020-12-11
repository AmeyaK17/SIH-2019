# Generated by Django 2.1.7 on 2019-02-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_id', models.CharField(max_length=100)),
                ('hos_id', models.CharField(max_length=30)),
                ('admin_email_id', models.CharField(max_length=50)),
                ('admin_mob_no', models.CharField(max_length=12)),
                ('admin_address', models.CharField(max_length=500)),
                ('admin_age', models.CharField(max_length=2)),
                ('admin_patient_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_id', models.CharField(max_length=50)),
                ('hos_id', models.CharField(max_length=30)),
                ('doc_mob_no', models.CharField(max_length=12)),
                ('doc_address', models.CharField(max_length=500)),
                ('doc_age', models.CharField(max_length=2)),
                ('doc_lic_no', models.CharField(max_length=100)),
                ('doc_admin_id', models.CharField(max_length=50)),
                ('doc_patient_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_name', models.CharField(max_length=100)),
                ('rec_id', models.CharField(max_length=100)),
                ('hos_id', models.CharField(max_length=30)),
                ('rec_email_id', models.CharField(max_length=50)),
                ('rec_mob_no', models.CharField(max_length=12)),
                ('rec_address', models.CharField(max_length=500)),
                ('rec_age', models.CharField(max_length=2)),
                ('rec_patient_id', models.CharField(max_length=100)),
            ],
        ),
    ]