# Generated by Django 4.1 on 2022-10-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('fashion', 'fashion'), ('electronics', 'electronics'), ('beauty', 'beauty'), ('home', 'home'), ('furniture', 'furniture'), ('grocery', 'grocery')], max_length=50),
        ),
    ]
