# Generated by Django 3.0.8 on 2020-07-03 07:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('address', models.CharField(max_length=100, verbose_name='住所')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^978-4-[0-9]{4}-[0-9]{4}-[0-9X]{1}$', message='ISBNコードは正しい形式で指定してください。')], verbose_name='ISBNコード')),
                ('title', models.CharField(max_length=100, verbose_name='書名')),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(17, message='価格は正の整数で指定してください。')], verbose_name='価格')),
                ('publisher', models.CharField(choices=[('翔泳社', '翔泳社'), ('技術評論社', '技術評論社'), ('秀和システム', '秀和システム'), ('SBクリエイティブ', 'SBクリエイティブ'), ('日経BP', '日経BP')], max_length=50, verbose_name='出版社')),
                ('published', models.DateField(verbose_name='刊行日')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=20, verbose_name='ユーザー名')),
                ('email', models.CharField(max_length=100, verbose_name='メールアドレス')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('body', models.TextField(max_length=255, verbose_name='本文')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Book')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='main.Book'),
        ),
    ]
