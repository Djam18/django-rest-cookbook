from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            # Django 5.0: db_default sets the default at database level
            field=models.BooleanField(db_default=False),
        ),
    ]
