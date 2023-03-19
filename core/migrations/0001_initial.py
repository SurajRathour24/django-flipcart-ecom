# Generated by Django 4.1.1 on 2022-10-02 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Amaravati', 'Amaravati'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Itanagar', 'Itanagar'), ('Assam', 'Assam'), ('Dispur', 'Dispur'), ('Bihar', 'Bihar'), ('Patna', 'Patna'), ('Chhattisgarh', 'Chhattisgarh'), ('Raipur', 'Raipur'), ('Goa', 'Goa'), ('Panaji', 'Panaji'), ('Gujarat', 'Gujarat'), ('Gandhinagar', 'Gandhinagar'), ('Haryana', 'Haryana'), ('Chandigarh', 'Chandigarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Shimla', 'Shimla'), ('Jharkhand', 'Jharkhand'), ('Ranchi', 'Ranchi'), ('Karnataka', 'Karnataka'), ('Bangalore', 'Bangalore'), ('Kerala', 'Kerala'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Bhopal', 'Bhopal'), ('Maharashtra', 'Maharashtra'), ('Mumbai', 'Mumbai'), ('Manipur', 'Manipur'), ('Imphal', 'Imphal'), ('Meghalaya', 'Meghalaya'), ('Shillong', 'Shillong'), ('Mizoram', 'Mizoram'), ('Aizawl', 'Aizawl'), ('Nagaland', 'Nagaland'), ('Kohima', 'Kohima'), ('Odisha', 'Odisha'), ('Bhubaneshwar', 'Bhubaneshwar'), ('Punjab', 'Punjab'), ('Chandigarh', 'Chandigarh'), ('Rajasthan', 'Rajasthan'), ('Jaipur', 'Jaipur'), ('Sikkim', 'Sikkim'), ('Gangtok', 'Gangtok'), ('Tamil Nadu', 'Tamil Nadu'), ('Chennai', 'Chennai'), ('Telangana', 'Telangana'), ('Hyderabad', 'Hyderabad'), ('Tripura', 'Tripura'), ('Agartala', 'Agartala'), ('Uttarakhand', 'Uttarakhand'), ('Dehradun', 'Dehradun'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Lucknow', 'Lucknow'), ('West Bengal', 'West Bengal'), ('Kolkata', 'Kolkata')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=50)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('fashion', 'fashion'), ('elctronics', 'electronics'), ('beauty', 'beauty'), ('home', 'home'), ('furniture', 'furniture'), ('grocery', 'grocery')], max_length=50)),
                ('product_image', models.ImageField(upload_to='productimage')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('odered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Amaravati', 'Amaravati'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Itanagar', 'Itanagar'), ('Assam', 'Assam'), ('Dispur', 'Dispur'), ('Bihar', 'Bihar'), ('Patna', 'Patna'), ('Chhattisgarh', 'Chhattisgarh'), ('Raipur', 'Raipur'), ('Goa', 'Goa'), ('Panaji', 'Panaji'), ('Gujarat', 'Gujarat'), ('Gandhinagar', 'Gandhinagar'), ('Haryana', 'Haryana'), ('Chandigarh', 'Chandigarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Shimla', 'Shimla'), ('Jharkhand', 'Jharkhand'), ('Ranchi', 'Ranchi'), ('Karnataka', 'Karnataka'), ('Bangalore', 'Bangalore'), ('Kerala', 'Kerala'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Bhopal', 'Bhopal'), ('Maharashtra', 'Maharashtra'), ('Mumbai', 'Mumbai'), ('Manipur', 'Manipur'), ('Imphal', 'Imphal'), ('Meghalaya', 'Meghalaya'), ('Shillong', 'Shillong'), ('Mizoram', 'Mizoram'), ('Aizawl', 'Aizawl'), ('Nagaland', 'Nagaland'), ('Kohima', 'Kohima'), ('Odisha', 'Odisha'), ('Bhubaneshwar', 'Bhubaneshwar'), ('Punjab', 'Punjab'), ('Chandigarh', 'Chandigarh'), ('Rajasthan', 'Rajasthan'), ('Jaipur', 'Jaipur'), ('Sikkim', 'Sikkim'), ('Gangtok', 'Gangtok'), ('Tamil Nadu', 'Tamil Nadu'), ('Chennai', 'Chennai'), ('Telangana', 'Telangana'), ('Hyderabad', 'Hyderabad'), ('Tripura', 'Tripura'), ('Agartala', 'Agartala'), ('Uttarakhand', 'Uttarakhand'), ('Dehradun', 'Dehradun'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Lucknow', 'Lucknow'), ('West Bengal', 'West Bengal'), ('Kolkata', 'Kolkata')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
