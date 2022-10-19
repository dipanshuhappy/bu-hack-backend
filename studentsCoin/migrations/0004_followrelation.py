# Generated by Django 4.0.6 on 2022-10-17 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentsCoin', '0003_studentcoindetail_student_professional_detail_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='studentsCoin.studentcoindetail')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='studentsCoin.studentcoindetail')),
            ],
        ),
    ]
