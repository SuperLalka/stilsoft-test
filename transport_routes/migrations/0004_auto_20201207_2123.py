# Generated by Django 3.1.4 on 2020-12-07 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport_routes', '0003_auto_20201207_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassengersReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], help_text='Select user group', max_length=10, null=True)),
                ('review_text', models.CharField(blank=True, help_text='Enter your review text', max_length=100, null=True)),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_routes.transport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'transport_routes_passengers_reviews',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='reviews',
            field=models.ManyToManyField(through='transport_routes.PassengersReviews', to='transport_routes.Transport'),
        ),
    ]
