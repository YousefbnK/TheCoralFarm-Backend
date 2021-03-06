
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoralType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('image', models.ImageField(upload_to='')),
                ('light', models.CharField(max_length=120)),
                ('flow', models.CharField(max_length=120)),
                ('care', models.CharField(max_length=120)),
                ('coralType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CoralType')),
            ],
        ),
    ]
