
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(max_length=12)),
                ('instrument_type', models.CharField(choices=[('Guitar', 'Guitar'), ('Violin', 'Violin'), ('Piano', 'Piano')], max_length=20)),
            ],
        ),
    ]
