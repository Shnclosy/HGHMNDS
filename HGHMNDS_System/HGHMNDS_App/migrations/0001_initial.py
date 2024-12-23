# Generated by Django 5.1.3 on 2024-12-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=255, null=True)),
                ('Item_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('color', models.CharField(choices=[('red', 'Red'), ('yellow', 'Yellow'), ('blue', 'Blue'), ('black', 'Black'), ('white', 'White')], max_length=10)),
                ('size', models.CharField(choices=[('XSmall', 'X-Small'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('XLarge', 'X-Large')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('user', 'User'), ('seller', 'Seller'), ('admin', 'Admin')], default='user', max_length=10)),
            ],
        ),
    ]
