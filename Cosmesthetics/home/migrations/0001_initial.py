# Generated by Django 3.2.12 on 2022-07-21 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('small_title', models.CharField(max_length=200)),
                ('main_title', models.CharField(max_length=80)),
                ('third_title', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=25)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(default='', upload_to='banners/')),
                ('link_to', models.URLField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('preference', models.CharField(default='Phone', max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromoCodeDiscount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discount_price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SlideContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('small_title', models.CharField(max_length=200)),
                ('main_title', models.CharField(max_length=80)),
                ('third_title', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=25)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(default='', upload_to='slides/')),
                ('link_to', models.URLField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('promo_code_text', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('promo_code_discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.promocodediscount')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('featured', models.CharField(choices=[('Featured', 'Featured'), ('Non-featured', 'Non-featured')], default='Non-featured', max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('marked_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('available_quantity', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(default='', upload_to='cosmeproducts/')),
                ('return_policy', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('tags', models.CharField(max_length=300)),
                ('meta_keywords', models.CharField(max_length=255)),
                ('meta_description', models.TextField()),
                ('modified_date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
                ('users_wishlist', models.ManyToManyField(blank=True, related_name='user_wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.PositiveBigIntegerField(default=0)),
                ('unique_order_id', models.CharField(default='', max_length=300)),
                ('delivery_charge', models.PositiveIntegerField(default=100)),
                ('promo_discount', models.PositiveIntegerField(default=0)),
                ('total_cost', models.PositiveBigIntegerField(default=0)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(choices=[('pending', 'pending'), ('received', 'received'), ('packed', 'packed'), ('on_the_way', 'on_the_way'), ('delivered', 'delivered'), ('cancel', 'cancel')], default='pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
