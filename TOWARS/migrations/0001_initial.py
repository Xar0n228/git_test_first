# Generated by Django 2.1.7 on 2019-03-26 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_key', models.CharField(blank=True, choices=[('pizza', 'Пицца'), ('sushi', 'Суши'), ('burger', 'Бургер'), ('drink', 'Напиток'), ('alcohol', 'Алкоголь')], default='pizza', max_length=30, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория товара:',
                'verbose_name_plural': 'Категория товаров:',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mStatus', models.CharField(blank=True, choices=[('ready', 'доступен'), ('not_ready', 'недоступен'), ('allready', 'В разработке')], default='ready', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Towar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='_', max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('zena', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ves', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default=None, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, help_text='150x150px', upload_to='media_true/%Y/%m/%d', verbose_name='Ссылка картинки')),
                ('category_new', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back_to_towar', to='TOWARS.Category_new')),
                ('status', models.ForeignKey(blank=True, default='ready', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back_to_towar', to='TOWARS.Status')),
            ],
            options={
                'verbose_name': 'Товар:',
                'verbose_name_plural': 'Товары:',
                'default_related_name': 'back_to_towar',
            },
        ),
    ]