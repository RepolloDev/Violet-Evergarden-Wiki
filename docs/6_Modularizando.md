<h1 align='center'>🧩 Modularizando</h1>

Uno de los conceptos más importantes en programación es la
modularización, este es un _paradigma_ (forma de programar)
que consiste en dividir un programa en partes más pequeñas,
de forma que cada parte tenga una responsabilidad específica.

En la programación web, es mucho más importante modularizar
las cosas porque en una simple página web pueden existir
varios elementos complejos y repetitivos.

## 😩 Vanilla no sabe muy bien

Utilizar las tecnolgías básicas de la web (HTML, CSS y JS)
nos limita mucho a la hora de modularizar, ya que no hay
una forma nativa de hacerlo.

En una página HTML, si queremos repetir un elemento, debemos
copiar y pegar el código, lo que hace que el código sea
repetitivo y difícil de mantener.

En todo esto hay que agregar el funcionamiento de CSS y JS,
que para ciertos elementos es difícil de mantener.

> [!NOTE]
> Usar el enfoque de todo en uno, es decir, toda la pagina
> esta compuesta fuertemente, es algo muy dificil de mantener
> y mucho peor desarrollar.

## 🤔 ¿Cómo modularizar?

Para poder utilizar la técnica de la modularización en
nuestros proyectos, tenemos varias opciones:

- **JavaScript**: Crear una funcionalidad para remplazar
  elementos HTML por otros, de forma dinámica.
- **Librerías**: Utilizar librerías para utilizar
  componentes ya hechos o crear los nuestros.
- **Sin nada**: Utilizar HTML, CSS y JS puro, pero
  de una forma más organizada.

La última opción parece complicada, pero dado que para
este proyecto no utilizaremos librerias que no sean
más que para diseño, nos enfocaremos en esta.

## 📦 Estructura de carpetas

En el proyecto se creará una carpeta llamada `components`,
la cual contendrá varios directorios, cada uno con un
componente.

```
.
├── 🧩 components
│   ├── 🖼️ image
│   │   ├── index.html
│   │   ├── index.css
│   │   └── index.js (opcional)
...
```

En cada carpeta de componente, se creará un archivo HTML,
CSS y JS (opcional) que contendrá el código del componente.
De esta manera **nos enfocamos en desarrollar parte por parte**
la estructura de la página.

## 🫠 Usando módulos

Dado que nuestro enfoque es utilizar los módulos de HTML,
CSS y JavaScript en una página web, seguiremos la siguiente
estructura:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="es">
  <head>
    ...
    <title>Titulo de la página</title>
    ...
    <!-- Libraries -->
    <link rel="stylesheet" href="/lib/bootstrap/index.css" />
    <script src="/lib/bootstrap/index.js"></script>
    ...
    <!-- Global -->
    <link rel="stylesheet" href="/styles/global.css" />
    <script src="/scripts/global.js"></script>
    ...
    <!-- Components Styles -->
    <link rel="stylesheet" href="/components/image/index.css" />
    ...
    <!-- Local Styles -->
    <link rel="stylesheet" href="./assets/index.css" />
  </head>
  <body>
    ...
  </body>
  <!-- Components Scripts -->
  <script src="/components/image/index.js"></script>
  ...
  <!-- Local Scripts -->
  <script src="./assets/index.js"></script>
</html>
```

De esta forma agrupamos los estilos y scripts de los diferentes
componentes y recursos externos en la página, de forma que
podamos mantener el código de una forma más organizada.

Este tiene un gran problema que el uso de los componentes de HTML,
dado que no existe una forma de importar un archivo HTML en otro,
por lo que debemos copiar y pegar el código de cada componente
en la página principal.

> [!NOTE]
> Respecto a la forma en la que se organizan las páginas, esto
> se desarrollo en [5. Creando contenido](./5_Creando_contenido.md)
> donde se explica como se estructura una página web.