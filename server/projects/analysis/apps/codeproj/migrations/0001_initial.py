# -*- coding: utf-8 -*-
# Generated by Django 3.1.12 on 2021-11-29 11:34
"""
codeproj数据迁移脚本
0001_initial
"""
import django.db.models.manager
from django.db import migrations, models

import apps.base.basemodel


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            # codeproj_project
            name='Project',
            fields=[
                ('created_time',
                 models.DateTimeField(db_index=True, default=apps.base.basemodel.utcnow, verbose_name='创建时间')),
                ('creator', models.CharField(blank=True, max_length=128, null=True, verbose_name='创建人')),
                ('modified_time',
                 models.DateTimeField(db_index=True, default=apps.base.basemodel.utcnow, verbose_name='最近修改时间')),
                ('modifier', models.CharField(blank=True, max_length=128, null=True, verbose_name='最近修改人')),
                ('deleted_time', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='删除时间')),
                ('deleter', models.CharField(blank=True, max_length=128, null=True, verbose_name='删除人')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='项目全局id')),
                ('repo_id', models.BigIntegerField(db_index=True, verbose_name='代码库全局id')),
                ('scan_scheme_id', models.BigIntegerField(blank=True, null=True, verbose_name='扫描方案全局id')),
                ('scm_type',
                 models.CharField(choices=[('git', 'Git'), ('svn', 'SVN')], max_length=8, verbose_name='代码库类型')),
                ('scm_url', models.CharField(max_length=512, verbose_name='代码库地址')),
                ('org_sid', models.CharField(blank=True, max_length=64, null=True, verbose_name='团队编号')),
                ('team_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='项目组名称')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            # codeproj_scan
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.BigIntegerField(verbose_name='代码库全局id')),
                ('state',
                 models.IntegerField(choices=[(0, 'Waiting'), (1, 'Running'), (2, 'Closed'), (3, 'Closing')], default=1,
                                     verbose_name='状态')),
                ('create_time', models.DateTimeField(blank=True, null=True, verbose_name='扫描创建时间')),
                ('scan_time', models.DateTimeField(auto_now_add=True, verbose_name='扫描起始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='扫描结束时间')),
                ('current_revision', models.CharField(blank=True, max_length=512, null=True, verbose_name='扫描版本号')),
                ('scm_time', models.DateTimeField(blank=True, null=True, verbose_name='扫描版本时间')),
                ('result_code', models.IntegerField(blank=True, null=True, verbose_name='结果状态码')),
                ('result_msg', models.TextField(blank=True, null=True, verbose_name='结果详细信息')),
                ('job_gid', models.IntegerField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True, verbose_name='扫描类型')),
                ('creator', models.CharField(blank=True, max_length=128, null=True, verbose_name='启动人')),
                ('daily_save', models.BooleanField(default=False, verbose_name='扫描结果数据保存开关，默认为False')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeproj.project',
                                              verbose_name='产品名称')),
            ],
        ),
    ]