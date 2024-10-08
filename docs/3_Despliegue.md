<h1 align='center'>🚀 Despliegue</h1>

Prácticamente un proyecto web debe ser desplegado
para que sea accesbile a los usuarios, de lo contrario
**que sentido tiene mostrar un proyecto web**.

El despliegue de un proyecto completamente _vanilla_
es muy simple, existen varios servicios que permiten
hacerlo de manera gratuita.

## 🎈 GitHub Pages

GitHub Pages es un servicio de GitHub que permite
desplegar proyectos estáticos de manera gratuita.
Este proceso es bastante sencillo y se lo puede
hacer con algunos clicks. Pero, para este caso
se utilizan los _Github Actions_, que son _scripts_
que se ejecutan en GitHub.

La pregunta es, ¿por qué usar _Github Actions_? Pues, por
simple comodidad, ya que **el proyecto puede ser complejo**
durante el desarrollo y puede que necesitemos hacer
ciertas cosas para realizar el despliegue. Entonces, con
_Github Actions_ podemos adelantarnos a esos problemas.

### 📦 Configuración

En el apartado de _Actions_ en el repositorio se puede
crear una action o utilizar una _workflow_ ya existente.
Para este caso, se utiliza el _Static HTML_.

<p align='center'>
    <img width='400' src='../source/assets/photos/3.1_despliegue.png'/>
</p>

De esta manera, ya se tiene una forma de desplegar el
proyecto de manera automática. Cada vez que se haga un
_push_ a la rama _main_, se ejecutará la _workflow_ y
se desplegará el proyecto.

## 🤔 ¿Por qué ahora?

La razón de hacer el despliegue ahora es porque es una de las cosas más simples e importantes que se tiene para este tipo de proyecto.

> [!TIP]
> Como el proyecto es completamente estático , no se necesita de un servidor para desplegarlo, por lo que se puede hacer de manera gratuita.
