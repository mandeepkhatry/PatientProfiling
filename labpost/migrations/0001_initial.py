# Generated by Django 2.0.6 on 2018-08-03 07:21

from django.db import migrations, models
import django.db.models.deletion
import labpost.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('initializer', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[('Xray', 'X-Ray'), ('VXray', 'Video X-Ray'), ('Endoscopy', 'Endoscopy'), ('MRI', 'MRI')], max_length=20)),
                ('image', models.ImageField(upload_to=labpost.models.user_dir_path)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.LabAccount')),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='initializer.visit')),
            ],
        ),
        migrations.CreateModel(
            name='TestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField(default=0)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.LabAccount')),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testName', models.CharField(max_length=30, unique=True)),
                ('unit', models.CharField(max_length=10)),
                ('minVal', models.FloatField(null=True)),
                ('maxVal', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['testName'],
            },
        ),
        migrations.AddField(
            model_name='testitem',
            name='testName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labpost.TestModel'),
        ),
        migrations.AddField(
            model_name='testitem',
            name='visit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='initializer.visit'),
        ),
    ]
