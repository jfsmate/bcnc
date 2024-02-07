<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Python Java" />

  &#xa0;

  <!-- <a href="https://pythonjava.netlify.app">Demo</a> -->
</div>

<h1 align="center">Prueba técnica de BCNC Consulting</h1>


<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Python Selenium 🚀 Under construction...  🚧
</h4> 

<hr> -->

<br>

## :dart: About ##

Prueba técnica de BCNC Consulting

# PLAN Y ESTRATEGIA DE TESTING
## ACTIVIDADES DE LA PRUEBA
### Planificación de la Prueba
Se definen los objetivos de la prueba. En nuestro caso tenemos el siguiente requerimiento por parte del cliente:

**Objetivo 1**
- Realizar con Python y Selenium unos tests que recorran las secciones del menú “HOME” y “WHO WE ARE”, para extraer el valor de los párrafos que estén dentro de los divs con la clase “text”.
- Esas secciones se encuentran en la web https://bcncgroup.com/
  
_Criterios de entrada:_
- Se necesita tener acceso a la web https://bcncgroup.com/.
- En el menú deben aparecer los items “HOME” y “WHO WE ARE”.

**Objetivo 2**
- Realizar un test en Python o Java que compruebe la respuesta del API siguiente (al menos de los 5 primeros elementos, recorrer los datos para ver si el texto coincide con lo esperado.): https://jsonplaceholder.typicode.com/albums.
- Agregar a los tests el “flujo necesario” para los supuestos casos de que el API tuviese autenticación con:
	- [Realizar esas llamadas incluyendo el grant_type client credentials de OAuth 2.0].
	- [Realizar esas llamadas incluyendo el grant_type authorization code de OAuth 2.0].

- Agregar en el README “BDD given-when-then” para el ejercicio

_Criterios de entrada:_
- Se necesita tener acceso a la API https://jsonplaceholder.typicode.com/albums.

**Objetivos comunes**
- Integrar alguna librería que reporte el informe de todos los tests.
- Dockerizarlo todo.
- Presentar en el readme un plan/estrategia de testing, explicando las metodologías.
- Realizar el código en varios archivos, aplicando el desacople entre los métodos y la ejecución de las pruebas en sí.


### Análisis de la Prueba
Identificamos el objeto de prueba y priorizamos las condiciones de prueba.

Objeto 1
- Accedemos a la web https://bcncgroup.com/
- Comprobamos que se muestra la página, pero tiene un loading previo que tarda en mostrar la HOME.
- Observamos que posee un menú lateral donde se encuentras "HOME" y "WHO WE ARE".
- Inpeccionamos el código y vemos los elementos con clase "text".

Objeto 2
- Comprobamos que tenemos acceso a la API requerida
- Observamos la respuesta y examinamos los datos.

### Diseño de la prueba
Hacemos un diseño de los casos de prueba y del entorno que necesitamos, junto con las herramientas necesarias.
Se establencen 2 script diferentes para cada ámbito de prueba.

En nuestro caso se ha desarrollado utilizando las siguientes herramientas:
- Windows 11
- WSL Ubuntu
- Visual Studio Code
- Docker
- Git
- Postman

Tecnologías:
- Python
- Selenium
- Pytest
- BDD

También definimos las historias de usuario, por ejemplo:
Objetivo 1
```bash
## Escenario 1: Extracción el contenido de los párrafos con la clase "text" de la sección "HOME"

Como el usuario acce a la página principal `https://bcncgroup.com/`  
Quiero que el usuario hace clic en el enlace del menú "HOME"  
Entonces se espera que se extraiga el contenido de los párrafos dentro de los divs con la clase "text" en la sección "HOME". 
```

Objetivo 2
```bash
## Escenario 1: Verificar Respuesta del API sin seguridad

Como el usuario tiene acceso al API `https://jsonplaceholder.typicode.com/albums`  
Quiero que el usuario realice una solicitud GET al API  
Entonces el usuario debería recibir una respuesta exitosa (código 200)  
```

### Implementación de la Prueba
Se construye el entorno de prueba, con todas las herramientas y tecnologías definidas.
  
### Ejecución de la Prueba
- Se ejecutan los script de prueba y se comprueba su funcionamiento.
- Se comprueban los reportes generados
- Se dockeriza cada script.
- Se identifican varias funcionalidades pendientes por desarrollar para conseguir un estádo óptimo de la prueba.
- Todo queda documentado en el archivo README.md de cada proyecto.

**Criterios de salida:**
Objetivo 1
- Verificación de todos los párrafos de los items de menú "HOME" y "WHO WE ARE".
- Reporte con la ejecución de los tests.

Objetivo 2
- Verificación de que al menos de los 5 primeros elementos,de la respuesta coincide con el texto.
- Reporte con la ejecución de los tests.

## TIPOS DE PRUEBA
**Pruebas Funcionales:**\
	Las pruebas funcionales se centran en validar que el software cumpla con los requisitos y expectativas del usuario.
	En un proyecto de Selenium con behave, las pruebas funcionales pueden estar basadas en escenarios BDD definidos en archivos de características (.feature).
	Utiliza behave para escribir y ejecutar pruebas funcionales que verifiquen que las funcionalidades clave del software funcionen como se espera.

**Pruebas de Regresión:**\
	Las pruebas de regresión se centran en asegurar que los cambios recientes en el código no hayan introducido regresiones o errores en el software existente.
	En un proyecto de Selenium con behave, puedes ejecutar tus pruebas de regresión regularmente para detectar cualquier regresión potencial después de cada cambio de código.
	Automatiza las pruebas de regresión utilizando pytest y asegúrate de incluir una amplia cobertura de casos de prueba para minimizar la posibilidad de regresiones.

**Pruebas de Integración:**\
	Las pruebas de integración se enfocan en probar la interacción entre diferentes componentes del software.
	En un proyecto de Selenium con behave, puedes utilizar pruebas de integración para verificar que las diferentes partes del sistema funcionen correctamente juntas.
	Utiliza behave para escribir escenarios que cubran casos de integración entre componentes de tu aplicación.

**Pruebas de Aceptación del Usuario (UAT):**\
	Las pruebas de aceptación del usuario son realizadas por los usuarios finales para validar que el software cumple con sus necesidades y expectativas.
	En un proyecto de Selenium con behave, puedes colaborar con los usuarios finales para escribir escenarios BDD que reflejen sus casos de uso y expectativas.
	Ejecuta estas pruebas de aceptación del usuario antes de cada lanzamiento para garantizar que el software cumpla con los criterios de aceptación del usuario.

**Pruebas Exploratorias:**\
	Las pruebas exploratorias se basan en la experiencia y conocimiento del tester para descubrir errores no documentados y áreas de mejora en el software.
	En un proyecto de Selenium con behave, los testers pueden realizar pruebas exploratorias durante el proceso de desarrollo y ejecución de pruebas para identificar posibles problemas y áreas de mejora.
	Complementa las pruebas automatizadas con pruebas exploratorias manuales para una cobertura más completa.

## ANÁLISIS DEL RIESGO
Debido al poco tiempo para realizar la prueba se han detectado riesgos de producto:
- Funcionalidad incorrecta
		En un primer momento se intentó crear un docker con toda la funcionalidad a través de la instalación de python, chrome y chromedriver.
		Se observó que las mayores versiónes que se podían instalar de ambos no eran compatibles.
- Asociados a la organización
		El probador ha tenido que invertir tiempo en actualizac conocimientos, debido a que se han utilizado tecnologías con las que no		
		ha trabajado con anterioridad.


