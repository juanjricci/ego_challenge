# Desafío Backend EGO
## Pasos para levantar el proyecto localmente

## 1. Preparar el entorno
1. En el directorio deseado clonar el repositorio con el comando 
```
git clone https://github.com/juanjricci/ego_challenge.git
```
2. Crear un entorno virtual python con 
```
python3 -m venv <nombre_del_venv>
```
Generalmente, como nombre del entorno virtual se utiliza `venv` pero puede elegirse el que se desea.

3. Activar el entorno virtual con el comando 
```
source <nombre_del_venv>/bin/activate
```
Esto nos mostrará el nombre del entorno virtual encerrado en paréntesis precediendo al prompt.

4. Entrar en el directorio creado: `cd ego_challenge`. 

5. Instalar los requerimientos para el entorno virtual:
```
pip install -r requirements.txt
```
Puede mostrarse un error con un paquete llamado `bdist_wheel`. En ese caso podemos ignorar el error.

## 2. Levantar el proyecto localmente
1. Ubicarse en el directorio test_dev con el comando `cd test_dev`. 
2. Aplicar las migraciones de la base de datos:
```
python3 manage.py migrate
```
3. Levantar el proyecto localmente:
```
python3 manage.py runserver
```
Esto va a levantar el proyecto en `http://127.0.0.1:8000/`.

## 3. Probar las APIs a través de los endpoints
> En este instructivo lo haremos desde un navegador, pero puede hacerse desde algún software como Postman.
### Endpoint para administrar los modelos
1. Abrir un navegador e ir a `http://127.0.0.1:8000/ego/api/modelos`. Nos mostrará una lista vacía y, debajo, un formulario. Para crear un modelo podemos completar el formulario o seleccionar la ventana `Raw data` (recomendado) y completar el código `json` con alguno de los ejemplos provistos en el directorio `ego_challenge/test_dev/ego/json_utiles/post_modelo.json` (asegurarse que el campo `Media type` sea `application/json`).

2. Presionar el botón `POST`. Esto creará el nuevo modelo y lo mostrará en la lista de arriba.

3. Agregar algunos más de los modelos del archivo `post_modelo.json`.

4. Probar hacer una PUT o PATCH request de algún modelo. Por ejemplo: 
    - Ir a `http://127.0.0.1:8000/ego/api/modelos/1/`. Esto mostrará los datos del modelo con `id=1`. 
    - En el formulario de abajo, seleccionar la ventana `Raw data` y podemos cambiar alguno de los valores de los atributos y presionar el botón `PUT` o podemos utilizar el método `PATCH` ingresando en el json solamente el atributo que se desee actualizar, como en este ejemplo:
    ```
    {
        "anio": 2021,
    }
    ```
5. Probar eliminar alguno de los modelos. Por ejemplo:
    - Ir a `http://127.0.0.1:8000/ego/api/modelos/2/`.
    - Clickear el botón rojo `DELETE`.
    - Ir a `http://127.0.0.1:8000/ego/api/modelos/` y comprobar que modelo con `id=2` no se encuentra más en la lista.

### Endpoints para filtrar y ordenar los modelos
 - Podemos filtrar los modelos con los siguientes endpoints:
```
Filtra todos los modelos:
> http://127.0.0.1:8000/ego/api/modelos/
Filtra los modelos de tipo AUTO:
> http://127.0.0.1:8000/ego/api/modelos/?tipo=AUTO
Filtra los modelos de tipo SUV o CROSSOVER:
> http://127.0.0.1:8000/ego/api/modelos/?tipo__in=SUV,CROSSOVER
Filtra los modelos de tipo PICKUP o COMERCIAL:
> http://127.0.0.1:8000/ego/api/modelos/?tipo__in=PICKUP,COMERCIAL
```
 - Podemos ordenar los modelos con los siguientes endpoints:
```
Ordena por precio (ascendente):
> http://127.0.0.1:8000/ego/api/modelos/?ordering=precio
Ordena por precio (descendiente):
> http://127.0.0.1:8000/ego/api/modelos/?ordering=-precio
Ordena por año (ascendente):
> http://127.0.0.1:8000/ego/api/modelos/?ordering=anio
Ordena por año (descendiente):
> http://127.0.0.1:8000/ego/api/modelos/?ordering=-anio
```
 - Podemos filtrar y ordenar al mismo tiempo. Por ejemplo:
```
Filtra los modelos de tipo AUTO y los ordena por precio (ascendente):
> http://127.0.0.1:8000/ego/api/modelos/?tipo=AUTO&ordering=precio
```

### Endpoint para administrar componentes
1. Ir a `http://127.0.0.1:8000/ego/api/componentes`.

2. Hacer POST requests con los elementos del archivo `componentes.json`. 
> Pueden ser actualizados o eliminados de la misma forma que los modelos.

### Endpoint para administrar componentes
1. Ir a `http://127.0.0.1:8000/ego/api/fichas`.

2. Hacer POST requests con los elementos del archivo `post_ficha.json`. (Utilizar la ventana `Raw data` para ingresar el json del archivo.)
> Pueden ser actualizados o eliminados de la misma forma que los modelos. Tiene una relación uno a uno con los modelos, por lo que si eliminamos un modelo se eliminará su ficha correspondiente. 