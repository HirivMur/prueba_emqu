# PruebaEMQU - Backend

## Clonar el repositorio:


```
$ git clone https://github.com/HirivMur/prueba_emqu.git

```
## Requerimientos
- python3
- pip
## Ambiente
Crea un virtualenv para installar las dependencias:
```

$ python3 -m virtualenv env

```
Activa el ambiente 
```
MacOs
$ source env/bin/activate
Windows
$ env\Scripts\activate
```
 `(env)` indica que la sesión en terminal operra en un entorno virtual creado por `virtualenv`.

Instalación de dependencias:
```
(env)$ pip install -r requirements.txt
```

## Configuraciones

- Ahora, necesitamos crear un archivo `.env` .
Usa el archivo de ejemplo: `.env_example`

- Crea una nueva base de datos mysql llamada `db_emqu` y agrega su configuración al archivo `.env`. 
Carga a `db_emqu` el backup `backup_db_emqu`

Migración de los modelos:
```
(env)$ python manage.py migrate
```


## Correr el sistema 

````
(env)$ python manage.py runserver
````

## API Documentación

Con interfaz gráfica:
````
Crear una nueva encuesta `http://127.0.0.1:8000/api/encuestas/create/`
Consultar las estadísticas `http://127.0.0.1:8000/api/encuestas/estadisticas/list/`
````
Sin interfaz gráfica: Catálogo de redes sociales.

token: 8af7b636b8d7af3196857fb4e90f2d4cdbbfaa57
````
`http://127.0.0.1:8000/api/encuestas/redsocial/list/`
`http://127.0.0.1:8000/api/encuestas/redsocial/create/`
{
    "descripcion":"Facebook"
}

`http://127.0.0.1:8000/api/encuestas/redsocial/<pk>/update/`

{
    "descripcion":"Facebook"
}
