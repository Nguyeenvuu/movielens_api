# Generated by Django 3.1.7 on 2021-03-18 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedMovies',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='customer.customer')),
                ('recommendations', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'recommended_movies',
                'managed': False,
            },
        ),
    ]