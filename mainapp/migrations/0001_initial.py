# Generated by Django 3.1.2 on 2020-10-20 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_type', models.BooleanField()),
                ('code', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('sender', models.CharField(max_length=30)),
                ('sender_phone', models.CharField(max_length=30)),
                ('sender_address', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=30)),
                ('receiver_phone', models.CharField(max_length=30)),
                ('receiver_address', models.CharField(max_length=100)),
                ('box_detail', models.CharField(max_length=30)),
                ('worker', models.CharField(default='미정', max_length=30)),
                ('worker_phone', models.CharField(default=' ', max_length=30)),
                ('visit_date', models.DateTimeField(null=True)),
                ('box_step', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=50)),
                ('box_date', models.DateTimeField()),
                ('box_now', models.CharField(max_length=50)),
                ('box_state', models.CharField(max_length=30)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.box')),
            ],
        ),
    ]
