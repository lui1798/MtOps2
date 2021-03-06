#-*- coding:utf8 -*-
"""
Django settings for MtOps2 project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_6ysfedhknh=8rfrc#ar$60vah%^x0wxq65-ruadm1j+y^7gaa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'grappelli', # 第三方应用，用于美化 admin，提升可用性（在'django.contrib.admin'之前引用）
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guardian', # 第三方应用，扩展 Django 内置权限系统，增加 object 级权限
    'djauth_ext', # 自定义 django 内置认证授权应用
    'asset', # 资产应用
    'code_update', # 代码上线应用
    'dbop', # 数据库运维应用
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'MtOps2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MtOps2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mtops2',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans' # Django 国际化相关设置

TIME_ZONE = 'Asia/Shanghai' # 设置 Django 时区，注意此设置只在模版系统渲染数据时生效，Django 内部存储等以 UTC 时间为准

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static/') # 用于 python manage.py collectstatic 命令收集项目静态文件
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/auth/user/info-detail/' # Django 认证系统认证成功后跳转页面 URL，登录页表单中隐藏字段值
LOGIN_URL = '/auth/user/login/' # 设置 Django 认证系统 login() 方法 URl
LOGOUT_URL = '/auth/user/logout/' # 设置 Django 认证系统 logout() 方法 URL


GRAPPELLI_ADMIN_HEADLINE = 'MtOps' # GRAPPELLI 自定义 admin HEADLINE
GRAPPELLI_ADMIN_TITLE = 'MtOps' # GRAPPELLI 自定义 admin TITLE

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend', # 设置 django-guardian 权限后端
)
ANONYMOUS_USER_ID = -1 # django-guardian 支持匿名用户 object 授权
GUARDIAN_TEMPLATE_403 = True # 权限验证失败返回 403.html

# Celery 设置
BROKER_URL = 'redis://127.0.0.1:6380' # 设置 Celery 使用 redis 作为消息中间人（broker）
CELERY_ACCEPT_CONTENT=['json', 'pickle'] # CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml'] # 此设置在 Celery 3.2.x 中必须使用的，明确指出允许使用的序列化格式
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE # 使用和Django 同样的时区
