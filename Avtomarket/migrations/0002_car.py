
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avtomarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('ot_kuchi', models.IntegerField()),
                ('narxi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('yili', models.IntegerField()),
                ('avtosalon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='Avtomarket.avtosalon')),
            ],
        ),
    ]
