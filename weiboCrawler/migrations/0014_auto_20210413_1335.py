# Generated by Django 2.2.19 on 2021-04-13 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weiboCrawler', '0013_remove_weibotext_retweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weibotext',
            name='weibo_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weibo_text_user', to='weiboCrawler.WeiboUser', to_field='weibo_user_id'),
        ),
    ]