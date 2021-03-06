# Generated by Django 2.0.5 on 2018-05-07 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
        ('app', '0010_auto_20180507_2318'),
        ('connector', '0003_auto_20180502_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectorStep',
            fields=[
                ('campaignstepfield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='messenger.CampaignStepField')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('messenger.campaignstepfield', models.Model),
        ),
        migrations.RemoveField(
            model_name='connectorcampaign',
            name='copy_connector_id',
        ),
        migrations.RemoveField(
            model_name='connectorcampaign',
            name='created_by_id',
        ),
        migrations.RemoveField(
            model_name='searchresult',
            name='searchid',
        ),
        migrations.AddField(
            model_name='connectorcampaign',
            name='connectors',
            field=models.ManyToManyField(to='connector.SearchResult'),
        ),
        migrations.AddField(
            model_name='connectorcampaign',
            name='copy_connector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='connector.ConnectorCampaign'),
        ),
        migrations.AddField(
            model_name='connectorcampaign',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='connectorcampaigns', to='app.LinkedInUser'),
        ),
        migrations.AddField(
            model_name='search',
            name='company',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='industry',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='location',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='searches', to='app.LinkedInUser'),
        ),
        migrations.AddField(
            model_name='search',
            name='sales_search',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='url_search',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='searchresult',
            name='industry',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='searchresult',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='searchresults', to='app.LinkedInUser'),
        ),
        migrations.AddField(
            model_name='searchresult',
            name='search',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='connector.Search'),
        ),
        migrations.AlterField(
            model_name='search',
            name='keyword',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='company',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='location',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='connectorstep',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaignsteps', to='connector.ConnectorCampaign'),
        ),
    ]
