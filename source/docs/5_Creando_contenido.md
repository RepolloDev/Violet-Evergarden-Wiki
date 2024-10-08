<h1 align='center'>✍️ Creando contenido</h1>

Dado que la página web es una Wiki, el contenido es
lo más importante. El proyecto se trata de hacer una
página profesional hablando de diseño web, pero
se quedaría corto si solo muestro algunos parrafos
de texto para de manera genérica.

La información que se estudia y publica está
dividida en diferentes categorías:

- Personajes
- Capítulos
- Espaciales
- Historias

Cosa que se ve reflejada en la estructura del proyecto
en la carpeta `/pages/`, en el mismo se encuentras
estos directorios con las páginas HTML correspondientes.

## 🗞️ Información

Dado que de momento no se tiene un diseño claro de
la página web porque es necesario saber como es el
contenido que se va a mostrar (en información), entonces
se ha decidido **crear un primero los datos**.

```bash
# Estructura de páginas
.
└── 📁 pages
    ├── 🗃️ chapters
    |   ├── 🔶 index.html
    |   └── 📄 README.md
    ├── 🗃️ characters
    |   ├── 🔶 index.html
    |   └── 📄 README.md
    ├── 🗃️ specials
    |   ├── 🔶 index.html
    |   └── 📄 README.md
    ├── 🗃️ stories
    |   ├── 🔶 index.html
    |   └── 📄 README.md
    └── 🔶 index.html
```

Dado que no quiero separar el contenido del
resultado final, decidí que los datos se
almacenarán junto con el código fuente.

### 💊 Encapsulamiento

Desde cada categoría y sus subdirectorios se
manejará las páginas de la siguiente manera:

```bash
# Una página cualquiera
└── 🗃️ Personajes
    ├── 📦 assets
    ├── 🔶 index.html
    ├── 📄 README.md
    ├── ...subdirectorios
    └── 🗃️ Violet-Evergarden
```

El funcionamiento es bastante simple y funciona de manera
_recursiva_ para cada página, es decir, que cada página
tiene la misma estructura.

- `assets`: Carpeta que contiene los recursos de la página,
  como imagenes, videos, etc.
- `index.html`: Página principal, es la entrada que muestra
  la información haciendo uso de los datos y recursos.
- `README.md`: Archivo que contiene la información de la
  página, es el contenido que se mostrará en la página principal.
- `...subdirectorios`: Directorios que contienen más páginas,
  es decir, un proceso recursivo.

Entonces, si quiero ver únicamente texto plano acerca de un
personaje, por ejemplo, Violet Evergarden, puedo hacerlo
accediendo al directorio `/pages/characters/Violet-Evergarden/README.md`.

> Este método hace que cada página sea independiente de
> su contexto, es decir, que se puede mover a cualquier
> lugar sin que afecte su funcionamiento.
