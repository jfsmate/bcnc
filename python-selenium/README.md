<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Python Java" />

  &#xa0;

  <!-- <a href="https://pythonjava.netlify.app">Demo</a> -->
</div>

<h1 align="center">Python Selenium</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jfsmate/python-selenium?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jfsmate/python-selenium?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jfsmate/python-selenium?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/jfsmate/python-selenium?color=56BEB8">

</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Python Selenium 🚀 Under construction...  🚧
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

Prueba técnica de creación de un script de automatización de pruebas para la web de BCNC GROUP.

## :sparkles: Features ##

:heavy_check_mark: Realizar con Python y Selenium unos tests que recorran las secciones del menú “HOME” y “WHO WE ARE”, para extraer el valor de los párrafos que estén dentro de los divs con la clase “text”.;\
:heavy_check_mark: Esas secciones se encuentran en la web https://bcncgroup.com/;\

## :rocket: Technologies ##

The following tools were used in this project:

- [Python3](https://www.python.org/)
- selenium
- pytest
- pytest-html
- behave

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python3](https://www.python.org/downloads/), [Dockers](https://www.docker.com/) installed.

## :checkered_flag: Starting ##

## Project structure

- Dockerfile file, which helps us build our docker.
- requirements.text, helps us define the technologies and libraries we need.
- pages/, contains the page files that structure the project.
- test/, contains the features and steps of the testing framework.
- conftest.py, module to connect with the selenium docker

The system is dockerized and uses 2 images to mount the test automation framework.

- selenium/standalone-chrome (image containing selenium, chromedriver and chrome)
- selenium_test (image with the automation framework)


## Step 1
Download de repository.
```bash
$ git clone https://github.com/jfsmate/bcnc.git

```
and access the python-selenium folder.

## Step 2
We download the image from selenium/standalon-chrome

```bash
$ docker pull selenium/standalone-chrome

```

## Step 3
We are launching the selenium service, but with a particular twist, within a private network where the two dockers can communicate.
```bash
$ docker run -d --network mi_network -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
```

## Step 4
We build our docker to build the image.
```bash
$ docker build --no-cache -t selenium_tests .
```

## Step 5
We run and raise our container within our private network.
```bash
docker run --rm --network mi_network selenium_tests
```


# Next steps
- Export the generated report to be able to view it locally in a browser.
- Include .gitignore file so we can upload unnecessary files to the repository
- Include docker compose execution.


# Ejemplo de Uso BDD (given-when-then)

## Escenario 1: Extracción el contenido de los párrafos con la clase "text" de la sección "HOME"

**Given** el usuario acce a la página principal `https://bcncgroup.com/`  
**When** el usuario hace clic en el enlace del menú "HOME"  
**Then** se espera que se extraiga el contenido de los párrafos dentro de los divs con la clase "text" en la sección "HOME". 

## Escenario 2: Extracción el contenido de los párrafos con la clase "text" de la sección "WHO WE ARE"

**Given** el usuario acce a la página principal `https://bcncgroup.com/who-we-are`  
**When** el usuario hace clic en el enlace del menú "HOME"  
**Then** se espera que se extraiga el contenido de los párrafos dentro de los divs con la clase "text" en la sección "WHO WE ARE".

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/jfsmate" target="_blank">Juan Fernando Sánchez Maté</a>

&#xa0;

<a href="#top">Back to top</a>

