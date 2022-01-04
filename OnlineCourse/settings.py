from pathlib import Path
import datetime
from datetime import timedelta
from django.conf import settings


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-tj!f_)=anceb3)34fv*oc$%15+y)m@!&467+if^h7koumqi1gn'
STRIP_KEY = 'sk_test_51KAqbJAz9OavjjPhXerGxPY7nDiRB9RQe3IVVGpbsCQqgbDTpfvjmzkrUSlSfoCk1HcrViPulSkOA0az0LPqp1Nv00Y7V0jyPQ'


#For production
# DEBUG = False
# ALLOWED_HOSTS = ['backend.techcyrus.com']

DEBUG = True
ALLOWED_HOSTS = ['*']




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'simple_history',
    'corsheaders',
    'rest_framework_swagger',
    'rest_framework_simplejwt.token_blacklist',
    'UserManagement.apps.UsermanagementConfig',
    'CourseManagement.apps.CoursemanagementConfig',
    'MembershipManagement.apps.MembershipmanagementConfig',
    'CommonApp.apps.CommonappConfig',
    'OrderManagement.apps.OrdermanagementConfig',
    'AdminDashBoard.apps.AdmindashboardConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OnlineCourse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            },
            
        },
        
    },
]

WSGI_APPLICATION = 'OnlineCourse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Rest API
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    
    'PAGE_SIZE': 10,
    
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
    
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '1/minute',
    #     'user': '20/minute',
    # },
}

#For Deployment:
# FONTEND_URL = "https://tech-cyrus.herokuapp.com/"

# CORS_ORIGIN_WHITELIST = (
#     'https://tech-cyrus.herokuapp.com/',
#     'https://tech-cyrus.herokuapp.com',
#     'tech-cyrus.herokuapp.com',
# )

# CORS_ALLOWED_ORIGINS = [
#     'https://tech-cyrus.herokuapp.com/',
#     'https://tech-cyrus.herokuapp.com',
#     'tech-cyrus.herokuapp.com',
# ]



#For local uses:
FONTEND_URL = "http://localhost:3000"

CORS_ALLOWED_ORIGINS = [
    'https://localhost:3000',
    'http://localhost:3000',
]

CORS_ORIGIN_WHITELIST = (
    'https://localhost:3000/',
    'http://localhost:3000/',
)

AUTH_USER_MODEL = "UserManagement.UserAccount"

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',"JWT"),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


STATIC_ROOT = BASE_DIR / 'staticfiles'  
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS =[
    BASE_DIR /'static'
]

MEDIA_ROOT = BASE_DIR / 'static/images'
