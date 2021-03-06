from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNumber', models.CharField(max_length=20)),
                ('CaseName', models.CharField(max_length=20)),
                ('CaseInfo', models.CharField(max_length=250)),
                ('Medicines', models.CharField(max_length=100)),
                ('DocUploads', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecepID', models.CharField(max_length=20)),
                ('DocsID', models.CharField(max_length=20)),
                ('HospitalID', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='Docs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Docs'),
        ),
    ]
