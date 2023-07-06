from django.core.exceptions import ImproperlyConfigured
import json

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" %secret_name
        raise ImproperlyConfigured(msg)

SECRET_KEY = get_secret('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    
    'captcha',
    'material' ,
    'material.admin' ,
    'simple_history',
    'import_export',
    # 'grappelli',
    'rest_framework.authtoken',
    'dj_rest_auth',
    # 'related_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'preventconcurrentlogins',
    
    
    #apps
    'applications.argumento',
    'applications.base_cliente',
    'applications.cliente',
    'applications.datos_g',
    'applications.guia',
    'applications.fisico',   
    'applications.courrier', 
    'applications.users',
    'applications.home',
    'applications.call',
    'applications.ruta',
    'applications.pqr',
    'applications.tracking',
    'applications.daviplata',
    'rest_framework',
    #'applications.zona',

]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication' 
    ],
}
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

MATERIAL_ADMIN_SITE  = {
    'HEADER' :   ( 'Bienvenido a Dio' ),   # Encabezado del sitio de administración 
    'TITLE' :    ( 'Bienvenido a Dio' ),   # Título del sitio de administración 
    'FAVICON' :   'img/Logo.jpg' ,   # Favicon del sitio de administración (se debe especificar la ruta a la estática) 
    'MAIN_BG_COLOR' :   'black ' ,   # Color principal del sitio de administración, se debe especificar el color css 
    'MAIN_HOVER_COLOR' :   '#115559' ,   # 
    # Color de desplazamiento principal del sitio de administración,El color css debe especificarse 'PROFILE_PICTURE' :  'ruta / a / imagen' ,   # Imagen de perfil del sitio de administración (se debe especificar la ruta a la estática) 
    'PROFILE_BG' :   'img/7q.gif' ,   # Fondo del perfil del sitio de administración (se debe especificar la ruta a la estática) 
    # 'LOGIN_LOGO' :   'img/Logo.jpg'  ,  # Logotipo del sitio de administración en la página de inicio de sesión (se debe especificar la ruta a la estática) 
    'LOGOUT_BG' :   'img/2q.gif'  ,   # Fondo del sitio de administración en las páginas de inicio / cierre de sesión (la ruta a la estática debe ser especificado) 
    'SHOW_THEMES' :   True ,   # Mostrar el botón de temas de administrador predeterminado 
    # 'TRAY_REVERSE' : Verdadero ,  # Ocultar las herramientas de objeto y la línea de envío adicional de forma predeterminada 
    # 'NAVBAR_REVERSE' : Verdadero ,   # Ocultar la barra de navegación lateral de forma predeterminada 
    # 'SHOW_COUNTS' : Verdadero , # Mostrar recuentos de instancias para cada modelo 
    # 'APP_ICONS' : {   # Establecer iconos para aplicaciones (minúsculas ), incluidas las aplicaciones de terceros, {'application_name': 'material_icon_name', ...} 
    #     'sites' : 'send' ,
    # },
    # 'MODEL_ICONS' : {   # Establecer iconos para modelos (minúsculas), incluidos modelos de terceros, {'model_name': 'material_icon_name', ...} 
    #     'site' : 'contact_mail' ,
    # }
}

GRAPPELLI_ADMIN_TITLE = 'Firstsource'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
    
   
]
#SESSION_COOKIE_AGE = 5 # 600 segundos = 10 minutos
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True 

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
#SESSION_COOKIE_AGE = 300 # = 5 minutos
SESSION_SAVE_EVERY_REQUEST = True

ROOT_URLCONF = 'Dio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
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

WSGI_APPLICATION = 'Dio.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Historial

SIMPLE_HISTORY_REVERT_DISABLED=True

MULTI_CAPTCHA_ADMIN  = {
     'motor' : 'recaptcha2' , 
}

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 
RECAPTCHA_PUBLIC_KEY = '6LehY7EjAAAAAPcDEXz3dTltdh6RjvTVGtpCmlKs'
RECAPTCHA_PRIVATE_KEY = '6LehY7EjAAAAABMbl_CnXdgQp9IK4oMWJj8lyKrD'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# SESSIO_ENGINE = "django.contrib.sessions.backends.cache"

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
#         "LOCATION": "127.0.0.1:11211",
#     }
# }