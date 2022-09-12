# Generated by Django 4.1 on 2022-09-01 18:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
