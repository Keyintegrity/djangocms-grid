from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('inner', models.BooleanField(default=True, help_text='Defines whether the plugin is already inside a grid container or another Multi-column plugin.', verbose_name='inner')),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridColumn',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('size', models.CharField(default='1', max_length=50, verbose_name='size', choices=[('1', 'grid-1'), ('2', 'grid-2'), ('3', 'grid-3'), ('4', 'grid-4'), ('5', 'grid-5'), ('6', 'grid-6'), ('7', 'grid-7'), ('8', 'grid-8'), ('9', 'grid-9'), ('10', 'grid-10'), ('11', 'grid-11'), ('12', 'grid-12'), ('13', 'grid-13'), ('14', 'grid-14'), ('15', 'grid-15'), ('16', 'grid-16'), ('17', 'grid-17'), ('18', 'grid-18'), ('19', 'grid-19'), ('20', 'grid-20'), ('21', 'grid-21'), ('22', 'grid-22'), ('23', 'grid-23'), ('24', 'grid-24')])),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
