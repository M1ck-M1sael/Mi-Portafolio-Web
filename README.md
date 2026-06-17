# 🚀 mickmisael.com - Cloud-Native Personal Portfolio

## 📖 Descripción General
Este repositorio contiene el código fuente y la configuración de infraestructura de mi portafolio web personal. Desarrollado íntegramente en **Python** utilizando el framework **Reflex**, este proyecto no solo funciona como una vitrina de mi experiencia, sino como una demostración práctica y funcional de mis habilidades en arquitectura Cloud, despliegue automatizado y prácticas DevOps.

## 🏗️ Arquitectura del Sistema
A continuación, se detalla la infraestructura implementada en AWS y el flujo de integración/despliegue continuo (CI/CD):

![Arquitectura AWS y CI/CD](/projects/portafolio_web/Flujo_Infraestructura_Portafolio.webp)

## 🛠️ Stack Tecnológico
* **Frontend & Backend:** Python, Reflex.
* **Infraestructura Cloud (AWS):** Amazon S3, Amazon CloudFront, Route 53, AWS Certificate Manager (ACM), IAM.
* **CI/CD:** GitHub Actions.
* **Control de Versiones:** Git / GitHub.

## 🔄 Proceso de Despliegue (CI/CD)
El proyecto cuenta con un pipeline automatizado mediante **GitHub Actions**. El flujo elimina los despliegues manuales y funciona de la siguiente manera:
1. **Trigger:** Un `git push` a la rama `main` activa el workflow.
2. **Build:** El entorno virtual instala dependencias y compila los archivos estáticos a través de Reflex.
3. **Deploy:** Utilizando credenciales seguras de un usuario **AWS IAM** con privilegios mínimos, el pipeline sincroniza los archivos generados con un bucket de **Amazon S3** (`aws s3 sync`).
4. **Invalidación:** Se ejecuta una invalidación de caché en **Amazon CloudFront** para garantizar que los cambios se reflejen de forma inmediata a nivel global.

## ⚡ Retos y Optimizaciones: Migración a Serverless
Para garantizar principios de eficiencia operativa y reducción de costos, la arquitectura de este proyecto fue refactorizada:
* **Estado inicial:** Despliegue basado en contenedores utilizando **Amazon ECS**, lo que generaba costos constantes por mantener recursos de cómputo encendidos.
* **Solución y Resultado:** Migración total de la infraestructura hacia un modelo de alojamiento estático serverless. Al exportar el proyecto a un bucket S3 y distribuirlo mediante CloudFront, se logró reducir drásticamente el gasto operativo mensual de AWS, se eliminó la carga de parcheo de servidores y se optimizó la latencia para el usuario final.

## ⚠️ Limitaciones Conocidas
Al migrar de una arquitectura basada en contenedores a un modelo 100% estático, se eliminó el servidor backend en Python. Esto cortó la conexión de WebSockets que el framework Reflex requiere para manejar el estado interactivo de la aplicación. 
Como resultado de esta decisión de diseño, funciones dinámicas como el **botón de cambio de idioma** se encuentran actualmente deshabilitadas. El ahorro radical de costos operativos y la mejora en seguridad justificaron la pérdida temporal de esta funcionalidad, documentándose como deuda técnica para una futura refactorización mediante enrutamiento estático (SSG).

## 💻 Ejecución Local
Si deseas clonar y correr este proyecto en tu entorno local:

1. Clona el repositorio:
```
   git clone [https://github.com/M1ck-M1sael/Mi-Portafolio-Web](https://github.com/M1ck-M1sael/Mi-Portafolio-Web)
```
2. Instala las dependencias y Reflex:
```
  python -m venv venv
  source venv/bin/activate  # En Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```
3. Inicial la aplicación en modo desarrollo:
```
  reflex run
```