# Generated by Django 3.2.4 on 2021-08-29 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serialsession',
            options={'ordering': ('-id',), 'verbose_name': 'serial session table', 'verbose_name_plural': 'serials session table'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_film', to='accounts.category', verbose_name='film category'),
            preserve_default=False,
        ),
    ]