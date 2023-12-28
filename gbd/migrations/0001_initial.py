# Generated by Django 3.2.16 on 2023-12-28 01:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ctype', models.CharField(blank=True, choices=[('NDA', 'NDA'), ('Evaluation/Material Transfer Agreement', 'Evaluation/Material Transfer Agreement'), ('Distribution Agreement', 'Distribution Agreement'), ('Licensing Agreement', 'Licensing Agreement'), ('etc', 'etc')], max_length=50)),
                ('date1', models.DateField(blank=True, default=0)),
                ('date2', models.DateField(blank=True, default=0)),
                ('upload', models.FileField(upload_to='file/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='RHDT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIME', models.CharField(choices=[('期初目標設定', '期初目標設定'), ('期中レビュー', '期中レビュー'), ('期末レビュー', '期末レビュー')], default='期初目標設定', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GOAL22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GOAL22A1', models.TextField(blank=True)),
                ('GOAL22B1', models.TextField(blank=True)),
                ('GOAL22C1', models.TextField(blank=True)),
                ('GOAL22D1', models.TextField(blank=True)),
                ('GOAL22E1', models.TextField(blank=True)),
                ('GOAL22F1', models.TextField(blank=True)),
                ('GOAL22G1', models.TextField(blank=True)),
                ('GOAL22AP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22BP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22CP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22DP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22EP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22FP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22GP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22A2', models.TextField(blank=True)),
                ('GOAL22B2', models.TextField(blank=True)),
                ('GOAL22C2', models.TextField(blank=True)),
                ('GOAL22D2', models.TextField(blank=True)),
                ('GOAL22E2', models.TextField(blank=True)),
                ('GOAL22F2', models.TextField(blank=True)),
                ('GOAL22G2', models.TextField(blank=True)),
                ('GOAL22A3', models.TextField(blank=True)),
                ('GOAL22B3', models.TextField(blank=True)),
                ('GOAL22C3', models.TextField(blank=True)),
                ('GOAL22D3', models.TextField(blank=True)),
                ('GOAL22E3', models.TextField(blank=True)),
                ('GOAL22F3', models.TextField(blank=True)),
                ('GOAL22G3', models.TextField(blank=True)),
                ('GOAL22AR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22BR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22CR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22DR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22ER', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22FR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22GR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL22AJ', models.TextField(blank=True)),
                ('GOAL22BJ', models.TextField(blank=True)),
                ('GOAL22CJ', models.TextField(blank=True)),
                ('GOAL22DJ', models.TextField(blank=True)),
                ('GOAL22EJ', models.TextField(blank=True)),
                ('GOAL22FJ', models.TextField(blank=True)),
                ('GOAL22GJ', models.TextField(blank=True)),
                ('GOAL22Q1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL22Q2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL22Q3', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL22Q1A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL22Q2A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL22Q3A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL22Q1Y', models.IntegerField(default=0)),
                ('GOAL22Q2Y', models.IntegerField(default=0)),
                ('GOAL22Q3Y', models.IntegerField(default=0)),
                ('GOAL22Q1M', models.IntegerField(default=0)),
                ('GOAL22Q2M', models.IntegerField(default=0)),
                ('GOAL22Q3M', models.IntegerField(default=0)),
                ('GOAL22Q1D', models.IntegerField(default=0)),
                ('GOAL22Q2D', models.IntegerField(default=0)),
                ('GOAL22Q3D', models.IntegerField(default=0)),
                ('GOAL23A1', models.TextField(blank=True)),
                ('GOAL23B1', models.TextField(blank=True)),
                ('GOAL23C1', models.TextField(blank=True)),
                ('GOAL23D1', models.TextField(blank=True)),
                ('GOAL23E1', models.TextField(blank=True)),
                ('GOAL23F1', models.TextField(blank=True)),
                ('GOAL23G1', models.TextField(blank=True)),
                ('GOAL23AP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23BP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23CP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23DP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23EP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23FP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23GP', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23A2', models.TextField(blank=True)),
                ('GOAL23B2', models.TextField(blank=True)),
                ('GOAL23C2', models.TextField(blank=True)),
                ('GOAL23D2', models.TextField(blank=True)),
                ('GOAL23E2', models.TextField(blank=True)),
                ('GOAL23F2', models.TextField(blank=True)),
                ('GOAL23G2', models.TextField(blank=True)),
                ('GOAL23A3', models.TextField(blank=True)),
                ('GOAL23B3', models.TextField(blank=True)),
                ('GOAL23C3', models.TextField(blank=True)),
                ('GOAL23D3', models.TextField(blank=True)),
                ('GOAL23E3', models.TextField(blank=True)),
                ('GOAL23F3', models.TextField(blank=True)),
                ('GOAL23G3', models.TextField(blank=True)),
                ('GOAL23AR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23BR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23CR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23DR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23ER', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23FR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23GR', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('GOAL23AJ', models.TextField(blank=True)),
                ('GOAL23BJ', models.TextField(blank=True)),
                ('GOAL23CJ', models.TextField(blank=True)),
                ('GOAL23DJ', models.TextField(blank=True)),
                ('GOAL23EJ', models.TextField(blank=True)),
                ('GOAL23FJ', models.TextField(blank=True)),
                ('GOAL23GJ', models.TextField(blank=True)),
                ('GOAL23Q1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL23Q2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL23Q3', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL23Q1A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL23Q2A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL23Q3A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('GOAL23Q1Y', models.IntegerField(default=0)),
                ('GOAL23Q2Y', models.IntegerField(default=0)),
                ('GOAL23Q3Y', models.IntegerField(default=0)),
                ('GOAL23Q1M', models.IntegerField(default=0)),
                ('GOAL23Q2M', models.IntegerField(default=0)),
                ('GOAL23Q3M', models.IntegerField(default=0)),
                ('GOAL23Q1D', models.IntegerField(default=0)),
                ('GOAL23Q2D', models.IntegerField(default=0)),
                ('GOAL23Q3D', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CPA22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPA22A1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22A2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22A3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22B1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22B2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22B3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22C1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22C2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22C3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22D1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22D2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22D3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22E1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22E2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22E3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22A1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22A2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22A3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22B1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22B2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22B3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22C1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22C2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22C3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22D1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22D2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22D3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22E1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22E2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22E3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA22A1K', models.TextField(blank=True)),
                ('CPA22A2K', models.TextField(blank=True)),
                ('CPA22A3K', models.TextField(blank=True)),
                ('CPA22B1K', models.TextField(blank=True)),
                ('CPA22B2K', models.TextField(blank=True)),
                ('CPA22B3K', models.TextField(blank=True)),
                ('CPA22C1K', models.TextField(blank=True)),
                ('CPA22C2K', models.TextField(blank=True)),
                ('CPA22C3K', models.TextField(blank=True)),
                ('CPA22D1K', models.TextField(blank=True)),
                ('CPA22D2K', models.TextField(blank=True)),
                ('CPA22D3K', models.TextField(blank=True)),
                ('CPA22E1K', models.TextField(blank=True)),
                ('CPA22E2K', models.TextField(blank=True)),
                ('CPA22E3K', models.TextField(blank=True)),
                ('CPA22A1P', models.TextField(blank=True)),
                ('CPA22A2P', models.TextField(blank=True)),
                ('CPA22A3P', models.TextField(blank=True)),
                ('CPA22B1P', models.TextField(blank=True)),
                ('CPA22B2P', models.TextField(blank=True)),
                ('CPA22B3P', models.TextField(blank=True)),
                ('CPA22C1P', models.TextField(blank=True)),
                ('CPA22C2P', models.TextField(blank=True)),
                ('CPA22C3P', models.TextField(blank=True)),
                ('CPA22D1P', models.TextField(blank=True)),
                ('CPA22D2P', models.TextField(blank=True)),
                ('CPA22D3P', models.TextField(blank=True)),
                ('CPA22E1P', models.TextField(blank=True)),
                ('CPA22E2P', models.TextField(blank=True)),
                ('CPA22E3P', models.TextField(blank=True)),
                ('CPA22C', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('CPA22A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('CPA22Y', models.IntegerField(default=0)),
                ('CPA22M', models.IntegerField(default=0)),
                ('CPA22D', models.IntegerField(default=0)),
                ('CPA23A1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23A2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23A3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23B1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23B2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23B3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23C1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23C2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23C3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23D1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23D2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23D3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23E1C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23E2C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23E3C', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23A1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23A2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23A3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23B1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23B2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23B3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23C1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23C2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23C3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23D1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23D2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23D3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23E1A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23E2A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23E3A', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1)),
                ('CPA23A1K', models.TextField(blank=True)),
                ('CPA23A2K', models.TextField(blank=True)),
                ('CPA23A3K', models.TextField(blank=True)),
                ('CPA23B1K', models.TextField(blank=True)),
                ('CPA23B2K', models.TextField(blank=True)),
                ('CPA23B3K', models.TextField(blank=True)),
                ('CPA23C1K', models.TextField(blank=True)),
                ('CPA23C2K', models.TextField(blank=True)),
                ('CPA23C3K', models.TextField(blank=True)),
                ('CPA23D1K', models.TextField(blank=True)),
                ('CPA23D2K', models.TextField(blank=True)),
                ('CPA23D3K', models.TextField(blank=True)),
                ('CPA23E1K', models.TextField(blank=True)),
                ('CPA23E2K', models.TextField(blank=True)),
                ('CPA23E3K', models.TextField(blank=True)),
                ('CPA23A1P', models.TextField(blank=True)),
                ('CPA23A2P', models.TextField(blank=True)),
                ('CPA23A3P', models.TextField(blank=True)),
                ('CPA23B1P', models.TextField(blank=True)),
                ('CPA23B2P', models.TextField(blank=True)),
                ('CPA23B3P', models.TextField(blank=True)),
                ('CPA23C1P', models.TextField(blank=True)),
                ('CPA23C2P', models.TextField(blank=True)),
                ('CPA23C3P', models.TextField(blank=True)),
                ('CPA23D1P', models.TextField(blank=True)),
                ('CPA23D2P', models.TextField(blank=True)),
                ('CPA23D3P', models.TextField(blank=True)),
                ('CPA23E1P', models.TextField(blank=True)),
                ('CPA23E2P', models.TextField(blank=True)),
                ('CPA23E3P', models.TextField(blank=True)),
                ('CPA23C', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('CPA23A', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('CPA23Y', models.IntegerField(default=0)),
                ('CPA23M', models.IntegerField(default=0)),
                ('CPA23D', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
