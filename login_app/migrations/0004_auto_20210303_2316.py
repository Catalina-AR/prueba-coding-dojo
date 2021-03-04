# Generated by Django 2.2.4 on 2021-03-04 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_amigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.CharField(max_length=20)),
                ('added', models.ManyToManyField(related_name='agregados', to='login_app.User')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador', to='login_app.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Amigo',
        ),
    ]