<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Python Java" />

  &#xa0;

  <!-- <a href="https://pythonjava.netlify.app">Demo</a> -->
</div>

<h1 align="center">Python API requests</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/python-java?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/python-java?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/python-java?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/python-java?color=56BEB8">

</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Python API request 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/jfsmate" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Prueba técnica de creación de un script para acceder a una API y tratar sus datos.
## :sparkles: Features ##

:heavy_check_mark: Realizar un test en Python o Java que compruebe la respuesta del API siguiente (al menos de los 5 primeros elementos, recorrer los datos para ver si el texto coincide con lo esperado.): https://jsonplaceholder.typicode.com/albums.;\

:heavy_check_mark: Agregar a los tests el “flujo necesario” para los supuestos casos de que el API tuviese autenticación con:
- [Realizar esas llamadas incluyendo el grant_type client credentials de OAuth 2.0].
- [Realizar esas llamadas incluyendo el grant_type authorization code de OAuth 2.0].;\
;\

:heavy_check_mark: Agregar en el README “BDD given-when-then” para el ejercicio;\

## :rocket: Technologies ##

The following tools were used in this project:

- [Python3](https://www.python.org/)
- requests Python3 Library
- pytest
- pytest-html
- behave

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python3](https://www.python.org/downloads/), [Dockers](https://www.docker.com/) installed.

## :checkered_flag: Starting ##

## Project structure

- Dockerfile file, which helps us build our docker.
- requirements.text, helps us define the technologies and libraries we need.
- api/, API call module.
- config/, necessary configuration files.
- tests/, test execution script.

Example report:
- assets/ CSS para el reporte
- report.html

The system is dockerized.

## Step 1
We build our docker to build the image.

```bash
$ docker build --no-cache -t python-requests .

```

## Step 2
We run and raise our container within our private network.
```bash
docker run --rm python-requests
```

# Next steps
- Export the generated report to be able to view it locally in a browser.
- Include .gitignore file so we can upload unnecessary files to the repository
- Include docker compose execution.

# Ejemplo de Uso BDD (given-when-then)

## Escenario 1: Verificar Respuesta del API sin seguridad

**Given** que tengo acceso al API `https://jsonplaceholder.typicode.com/albums`  
**When** realizo una solicitud GET al API  
**Then** debería recibir una respuesta exitosa (código 200)  

## Escenario 2: Verificar Datos de los Primeros 5 Elementos

**Given** que he realizado una solicitud al API  
**When** examino los datos recibidos  
**Then** debería encontrar información sobre al menos 5 álbumes

## Escenario 3: Verificar Coincidencia con Texto Esperado

**Given** que tengo los datos de los primeros 5 álbumes  
**When** reviso los títulos de los álbumes  
**Then** cada título debería coincidir con el formato esperado

## Escenario 4: Obtener Token con Client Credentials

**Given** que tengo acceso al API `https://jsonplaceholder.typicode.com/albums`   
**When** realizo una solicitud para obtener un token de acceso usando el flujo de concesión de credenciales del cliente  
**Then** debería recibir un token de acceso válido

## Escenario 5: Obtener Token con Access Token

**Given** que tengo acceso al API `https://jsonplaceholder.typicode.com/albums`   
**When** realizo una solicitud de autorización y obtengo un código de autorización  
**Then** utilizo ese código para obtener un token de acceso usando el flujo de concesión de autorización  
**And** debería recibir un token de acceso válido

## Escenario 6: Hacer Llamada a la API Protegida con Access Token

**Given** que tengo un token de acceso válido  
**When** realizo una solicitud a la API protegida  
**Then** examino los datos recibidos
**And** debería recibir una respuesta exitosa con los datos esperados

> :warning: Se pueden realizar más escenario si se conocen los códigos de error o demás códigos de respuesta de la API.


## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/jfsmate" target="_blank">Juan Fernando Sánchez Maté</a>

&#xa0;

<a href="#top">Back to top</a>

