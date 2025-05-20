from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0001_squashed_0004_auto_20160611_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='db',
            field=models.CharField(
                max_length=191,
                default='',
                help_text='The database the model under version control is stored in.',
            ),
            preserve_default=False,
        ),
    ]