# Generated by Django 3.1.5 on 2021-01-27 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Ort')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Ort',
                'verbose_name_plural': 'Ort',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Telefon nr:')),
                ('email', models.EmailField(max_length=254, verbose_name='E-post')),
                ('url', models.URLField(verbose_name='Url')),
                ('organization_number', models.CharField(max_length=50, verbose_name='Org.nr')),
                ('name', models.CharField(max_length=350, verbose_name='Nanm')),
                ('slug', models.CharField(max_length=350)),
                ('workplace', models.TextField(verbose_name='Adress')),
            ],
            options={
                'verbose_name': 'Employer',
                'verbose_name_plural': 'Employers',
            },
        ),
        migrations.CreateModel(
            name='JobTechTaxonomyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept_id', models.CharField(max_length=250, unique=True)),
                ('label', models.CharField(max_length=250)),
                ('legacy_ams_taxonomy_id', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branch',
            },
        ),
        migrations.CreateModel(
            name='JobAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250, unique=True, verbose_name='Title')),
                ('url', models.URLField(unique=True)),
                ('logo_url', models.URLField(unique=True)),
                ('description', models.TextField(verbose_name='Beskrivning')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('af_id', models.IntegerField(unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city', verbose_name='Ort')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.employer', verbose_name='Företag')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.jobtechtaxonomyitem', verbose_name='Branch')),
            ],
            options={
                'verbose_name': 'Tjänst',
                'verbose_name_plural': 'Tjänster',
            },
        ),
    ]
