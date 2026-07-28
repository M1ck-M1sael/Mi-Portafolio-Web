import datetime

TEXTOS = {

    # CONTENIDO EN ESPAÑOL
    "es": {
        "btn_idioma": "EN",
        "btn_cv": "Descargar CV",
        "nombre_nav": "Mick Misael",
        "nav_items": {
            "sobre_mi": "Sobre mí",
            "proyectos": "Proyectos",
            "contacto": "Contacto",
        },
        # CONTENIDO DE LA SECCIÓN "FOOTER"
        "footer_copyright": f"© {datetime.datetime.now().year} Mick Misael. Todos los derechos reservados.",

        # CONTENIDO DE LA SECCIÓN "SOBRE MÍ"
        "about_title": "Sobre mí",
        "about_name": "¡Hola! Soy Misael.",
        "description_1": "Soy estudiante de Ingeniería en Sistemas Computacionales en el Tecnológico Nacional de México, y actualmente trabajo como Systems Administrator, en donde gestiono infraestructura, soporte y operación de sistemas en entornos productivos.",
        "description_2": "Actualmente estoy estudiando diferentes cursos para formarme como DevOps Engineer.",
        "description_3": "Me caracterizo por el aprendizaje constante y la disciplina técnica. Actualmente me encuentro en proceso de obtener la certificación AWS Cloud Practitioner, fortaleciendo mis conocimientos en servicios cloud, buenas prácticas y arquitectura básica.",
        "funfact": "Amante de los gatos, arañas y el exceso de café... soy el estereotipo de mi carrera, ¿verdad? ¡Caray!",
        "skills_title": "Habilidades",
        "label_hard": "Habilidades Duras",
        "label_soft": "Habilidades Blandas",
        "label_useless": "Habilidades Inútiles",

        # CONTENIDO DE LA SECCIÓN "HABILIDADES"
        "habilidades_duras": [
            {"name": "AWS Cloud", "color": "orange"},
            {"name": "SysAdmin (Windows & Linux)", "color": "gray"},
            {"name": "Python & Reflex", "color": "blue"},
            {"name": "Cultura DevOps", "color": "purple"},
        ],
        "habilidades_blandas": [
            {"name": "Comunicación Asertiva", "color": "teal"},
            {"name": "Liderazgo", "color": "indigo"},
            {"name": "Trabajo en Equipo", "color": "cyan"},
            {"name": "Resolución de Problemas", "color": "crimson"},
        ],
        "habilidades_inutiles": [
            {"name": "Hablar como Gollum", "color": "grass"},
            {"name": "Silbar (Infravalorado)", "color": "yellow"},
            {"name": "Hacer Guturales", "color": "tomato"},
            {"name": "Conocer todo el lore del W2M Crew", "color": "pink"},
            {"name": "Redundar", "color": "amber"},
            {"name": "Hablar como Gollum", "color": "grass"},
        ],

        # CONTENIDO DE LA SECCIÓN "PROYECTOS"
        "projects_title": "Proyectos",
        "project_1": "Portafolio Web Personal",
        "project_1_description": "Desarrollo Full-Stack e implementación en AWS con el uso de la cultura DevOps.",
        "project_2": "Python | Script de Métodos Numéricos",
        "project_2_description": "Resolver problemas matemáticos complejos mediante aproximaciones computacionales, iteraciones y optimización de recursos, minimizando el margen de error.",
        "project_3": "StackTON",
        "project_3_description": "Startup de Arquitectura de Soluciones. Implementaciones de Infraestrucura en AWS y desarrollo web con Reflex y Stack convencional.",
        "project_4": "Futuro Proyecto",
        "project_4_description": "En proceso de desarrollo... ¡Pronto habrá novedades!",
        "project_5": "Futuro Proyecto",
        "project_5_description": "En proceso de desarrollo... ¡Pronto habrá novedades!",
        "project_6": "Futuro Proyecto",
        "project_6_description": "En proceso de desarrollo... ¡Pronto habrá novedades!",

        # CONTENIDO DE LA SECCIÓN "CONTACTO"
        "contact_title": "Contacto",
        "contact_header": "¿Tienes un proyecto en mente?",
        "contact_invitation_1": "Actualmente estoy abierto a nuevas oportunidades, colaboraciones en proyectos de infraestructura Cloud o consultorías técnicas.",
        "contact_invitation_2": "Si buscas un perfil con disciplina técnica, amor por la automatización y que sepa trabajar bajo presión (y con mucho café), ¡hablemos!",
        "contact_cv_prompt": "¿Necesitas mi perfil detallado?",
        "contact_gmail": "mickmisa3l@gmail.com",
        "contact_linkedin": "Conectemos profesionalmente",
        "contact_github": "Revisa mi código y despliegues",

#CONTENIDO DE LA SECCIÓN "DOCUMENTACIÓN"

        "doc_markdown": """
# 🚀 Documentación de Arquitectura y CI/CD

El portafolio web (mickmisael.com) no es únicamente una galería de proyectos y experiencia, sino una demostración práctica y funcional de mis conocimientos y habilidades en arquitectura Cloud y despliegue automatizado

Desarrollado íntegramente en Python utilizando el framework Reflex, el objetivo principal de este proyecto es evidenciar la capacidad de construir, desplegar y mantener infraestructura en la nube de nivel producción. La elección de Reflex permitió unificar el desarrollo Full-Stack bajo un mismo lenguaje, mientras que la infraestructura subyacente fue diseñada con un enfoque total en la cultura DevOps: priorizar la escalabilidad, seguridad, automatización continua y optimización de recursos.

## 🏗️ Diagrama de Infraestructura
![Arquitectura AWS y CI/CD](/projects/portafolio_web/Flujo_Infraestructura_Portafolio.webp)

**El flujo de trabajo automatizado sigue los siguientes pasos:**
1. **Desencadenador (Trigger):** El pipeline se activa automáticamente cada vez que realizo un git push a la rama principal de mi repositorio en GitHub.
2. **Entorno de Compilación (Build):** GitHub Actions levanta un entorno virtual (Runner), donde instala las dependencias de Python y el framework Reflex.
3. **Generación de Estáticos:** Se ejecuta el comando de Reflex para exportar la aplicación. Esto compila el Frontend (HTML, CSS, JavaScript) y genera los archivos estáticos finales.
4. **Autenticación Segura en AWS:** Utilizando **AWS IAM**, configuré un usuario dedicado exclusivamente para GitHub Actions. Las credenciales de este usuario (Access Keys) están almacenadas de forma segura en los **Secrets** del repositorio de GitHub. Esto cumple con el principio de menor privilegio, otorgando permisos solo para interactuar con el bucket S3 específico.
5. **Despliegue a S3:** El pipeline utiliza la AWS CLI para sincronizar (aws s3 sync) los archivos estáticos generados directamente en el bucket de Amazon S3, configurado para el hosting de sitios estáticos.
6. **Invalidación de Caché:** Como paso final, el pipeline ejecuta una invalidación de caché en AWS CloudFront. Esto fuerza a la CDN a buscar las versiones más recientes de los archivos en S3, asegurando que los usuarios visualicen los cambios de inmediato sin tener que esperar a que expire el TTL de la caché.

**Beneficios técnicos:** Esta automatización garantiza que el proceso de despliegue sea repetible, reduce el riesgo de error humano y minimiza el tiempo entre escritura del código y su disponibilidad en producción.

## ⚡ Retos y Optimizaciones:
El desarrollo de esta infraestructura no fue estático; evolucionó para resolver problemas reales de operación. El reto técnico más significativo durante el ciclo de vida de este proyecto fue la optimización radical de los costos de infraestructura en AWS sin sacrificar el rendimiento ni la disponibilidad global.

* **El Problema:** En su versión inicial, el backend y el frontend de la aplicación estaban alojados y ejecutándose mediante contenedores de **AWS ECS** (Elastic Container Service). Aunque esta arquitectura era robusta, mantenía recursos de cómputo encendidos de forma continua, lo que generaba un gasto operativo mensual completamente innecesario para el tráfico y la naturaleza de un portafolio personal.
* **La Solución:** Para aplicar principios reales de eficiencia y arquitectura de Cloud, tomé la decisión de desmantelar la infraestructura basada en contenedores y migrar a un entorno simple, económico y acorde a un portafolio web usando solamente **AWS S3** y **AWS CloudFront**.

    * Se dieron de baja todas las tareas y clústeres de **AWS ECS**.
    * Se refactorizó la exportación del proyecto en Reflex para generar una build 100% estática.
    * Se reconfiguraron los orígenes de la CDN en CloudFront para apuntar exclusivamente a un bucket de **AWS S3**.

## ⚠️ Limitaciones Conocidas:
Al migrar de una arquitectura basada en contenedores (ECS) a un modelo 100% estático serverless (S3), se eliminó el servidor backend. Esto cortó la conexión de WebSockets que el framework Reflex requiere para manejar estado interactivo de la aplicacion en tiempor real.

Como resultado de esta decisión consciente de diseño, fuciones dinámicas como el **botón de cambio de idioma** se encuentran actualmente deshabilidatas. El ahorro radical de gastos operativos y la mejora en seguridad justificaron la pérdida temporal de esta funcionalidad, la  cual queda como deuda técnica para una futura refactorización mediante enrutamiento estático.

## ✅​ El resultado:
Esta migración transformó el proyecto de un modelo de cómputo continuo a un modelo de alojamiento estático **serverless**. Esto no solo redujo drásticamente la factura mensual de AWS a **una fracción de su costo original**, sino que también disminuyó la superficie de ataque, eliminó la necesidad de parchear servidores y delegó toda la carga de distribución global y seguridad a AWS CloudFront, mejorando el **tiempo de respuesta** para el usuario final.
""", 

        # CONTENIDO DE LA SECCIÓN "CERTIFICACIONES"

        "cert_title": "Certificaciones",
        "cert_description": "Validación oficial y conocimientos respaldados por la industria.",
        "cert_list": [
            {
                "title": "AWS Certified Cloud Practitioner",
                "issuer": "Udemy",
                "date": "Diciembre 2025",
                "badge_url": "/certs/AWS_CP_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-278702d3-b0cd-49d9-a689-c4456046b9c6/",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "Docker Traning Course",
                "issuer": "KodeKloud",
                "date": "Julio 2025",
                "badge_url": "/certs/DOCK_TRN_COURSE_KODEKLOUD.webp",
                "verify_url": "https://lnkd.in/p/g-fxegwU",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "Terrafomr: De principiante a Certificado 2026",
                "issuer": "Udemy",
                "date": "Junio 2026",
                "badge_url": "/certs/TERRAFORM.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-8318999e-03c1-46a1-bd3c-64faa607e63b/",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "Administración de Active Directory con Windows PowerShell",
                "issuer": "Udemy",
                "date": "Junio 2024",
                "badge_url": "/certs/ADM_AD_DMS_W_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-7ed2e0cd-3029-4973-a2af-367d7de59ca1/",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "PowerShell Básico para Principiantes",
                "issuer": "Udemy",
                "date": "Mayo 2024",
                "badge_url": "/certs/POW_B_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-ec262e83-b38b-43b0-b411-e44dadaa7768/",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "Curso de Auditores Internos de Sistema de Gestion (ISO 19011:2018 e ISO 27001:2022)",
                "issuer": "Aktiva",
                "date": "Julio 2023",
                "badge_url": "/certs/ISO_27001.webp",
                "verify_url": "https://www.linkedin.com/in/misael-lópez-franco-409566209/overlay/Certifications/1871249793/treasury?profileId=ACoAADTxHMkBvlU0vVhyg9M8VbXIEd5TT9D6aj4",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "AD DS, DNS y DHCP en Windows Server",
                "issuer": "Udemy",
                "date": "Agosto 2023",
                "badge_url": "/certs/AD_DNS_DHCP_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-0883095e-1b97-4b91-9040-bd23260b50de/",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "Administración de Windows desde la Consola",
                "issuer": "Udemy",
                "date": "Febrero 2023",
                "badge_url": "/certs/ADM_WIN_CLI_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-9ad30dee-258a-4ea5-9667-b7ff443405ba/",
                "btn_verify": "Verificar Credencial",
            },
        ],

    },

    # CONTENIDO EN INGLÉS (TRADUCCIÓN)
    "en": {
        "btn_idioma": "ES",
        "btn_cv": "Download CV",
        "nombre_nav": "Mick Misael",
        "nav_items": {
            "sobre_mi": "About me",
            "proyectos": "Projects",
            "contacto": "Contact",
        },
        # CONTENIDO DE LA SECCIÓN "FOOTER"
        "footer_copyright": f"© {datetime.datetime.now().year} Mick Misael. All rights reserved.",

        # CONTENIDO DE LA SECCIÓN "SOBRE MÍ"
        "about_title": "About me",
        "about_name": "Hello there! I'm Misael.",
        "description_1": "I am a Computer Systems Engineering student at Tecnológico Nacional de México and currently work as a Systems Administrator, managing infrastructure, support, and system operations in production environments.",
        "description_2": "I am currently studying various courses to train as a DevOps Engineer.",
        "description_3": "I am driven by continuous learning and technical discipline. Currently, I am working toward my AWS Cloud Practitioner certification, deepening my expertise in cloud services, best practices, and foundational architecture.",
        "funfact": "Cat lover, spider enthusiast, and fueled by a concerning amount of coffee... I’m basically the walking stereotype of my major, aren't I? Geez!",
        "skills_title": "Skills",
        "label_hard": "Hard Skills",
        "label_soft": "Soft Skills",
        "label_useless": "Useless Skills",

        # CONTENIDO DE LA SECCIÓN "HABILIDADES"
        "habilidades_duras": [
            {"name": "AWS Cloud", "color": "orange"},
            {"name": "SysAdmin (Windows & Linux)", "color": "gray"},
            {"name": "Python & Reflex", "color": "blue"},
            {"name": "DevOps Culture", "color": "purple"},
        ],
        "habilidades_blandas": [
            {"name": "Assertive Communication", "color": "teal"},
            {"name": "Leadership", "color": "indigo"},
            {"name": "Teamwork", "color": "cyan"},
            {"name": "Problem Solving", "color": "crimson"},
        ],
        "habilidades_inutiles": [
            {"name": "Gollum Impression", "color": "grass"},
            {"name": "Whistling (Underrated)", "color": "yellow"},
            {"name": "Death Growls", "color": "tomato"},
            {"name": "W2M Crew Lore Expert", "color": "pink"},
            {"name": "Redundancy", "color": "amber"},
            {"name": "Gollum Impression", "color": "grass"},
        ],
        
        # CONTENIDO DE LA SECCIÓN "PROYECTOS"
        "projects_title": "Projects",
        "project_1": "Personal Web Portfolio",
        "project_1_description": "Full-Stack development and AWS deployment with the use of DevOps culture.",
        "project_2": "Python | Numeric Methods Script",
        "project_2_description": "A Python script that implements various numerical methods for solving mathematical problems, such as root finding, numerical integration, and differential equations.",
        "project_3": "StackTON",
        "project_3_description": "Architecture of IT Solutions. Implementations of Infrastructure in AWS and web development with Reflex and conventional Stack.",
        "project_4": "Future Project",
        "project_4_description": "In development... Stay tuned for updates!",
        "project_5": "Future Project",
        "project_5_description": "In development... Stay tuned for updates!",
        "project_6": "Future Project",
        "project_6_description": "In development... Stay tuned for updates!",

        # CONTENIDO DE LA SECCIÓN "DOCUMENTACIÓN"
"doc_markdown": """
# 🚀 Architecture and CI/CD Documentation

The web portfolio (mickmisael.com) is not just a project and experience gallery, but a practical and functional demonstration of my knowledge and skills in Cloud architecture and automated deployment.

Developed entirely in Python using the Reflex framework, the main goal of this project is to showcase the ability to build, deploy, and maintain production-grade cloud infrastructure. Choosing Reflex allowed me to unify Full-Stack development under a single language, while the underlying infrastructure was designed with a total focus on DevOps culture: prioritizing scalability, security, continuous automation, and resource optimization.

## 🏗️ Infrastructure Diagram
![AWS Architecture and CI/CD](/projects/portafolio_web/Flujo_Infraestructura_Portafolio.webp)

**The automated workflow follows these steps:**
1. **Trigger:** The pipeline is automatically triggered every time I perform a git push to the main branch of my GitHub repository.
2. **Build Environment:** GitHub Actions spins up a virtual environment (Runner), where it installs the Python dependencies and the Reflex framework.
3. **Static Generation:** The Reflex command is executed to export the application. This compiles the Frontend (HTML, CSS, JavaScript) and generates the final static files.
4. **Secure AWS Authentication:** Using **AWS IAM**, I configured a dedicated user exclusively for GitHub Actions. The credentials for this user (Access Keys) are securely stored in the **Secrets** of the GitHub repository. This complies with the principle of least privilege, granting permissions to interact only with the specific S3 bucket.
5. **Deployment to S3:** The pipeline uses the AWS CLI to sync (`aws s3 sync`) the generated static files directly into the Amazon S3 bucket, configured for static website hosting.
6. **Cache Invalidation:** As a final step, the pipeline executes a cache invalidation in AWS CloudFront. This forces the CDN to fetch the latest versions of the files from S3, ensuring users see the changes immediately without having to wait for the cache TTL to expire.

**Technical benefits:** This automation guarantees a repeatable deployment process, reduces the risk of human error, and minimizes the time between writing code and its availability in production.

## ⚡ Challenges and Optimizations:
The development of this infrastructure was not static; it evolved to solve real operational problems. The most significant technical challenge during the lifecycle of this project was the radical optimization of AWS infrastructure costs without sacrificing performance or global availability.

* **The Problem:** In its initial version, the application's backend and frontend were hosted and running using **AWS ECS** (Elastic Container Service) containers. Although this architecture was robust, it kept compute resources running continuously, generating a monthly operational expense that was completely unnecessary for the traffic and nature of a personal portfolio.
* **The Solution:** To apply real principles of efficiency and Cloud architecture, I made the decision to dismantle the container-based infrastructure and migrate to a simple, cost-effective environment suitable for a web portfolio using only **AWS S3** and **AWS CloudFront**.

    * All **AWS ECS** tasks and clusters were decommissioned.
    * The project export in Reflex was refactored to generate a 100% static build.
    * The CDN origins in CloudFront were reconfigured to point exclusively to an **AWS S3** bucket.

## ⚠️ Known Limitations:
By migrating from a container-based architecture (ECS) to a 100% static serverless model (S3), the backend server was eliminated. This severed the WebSockets connection that the Reflex framework requires to manage interactive application state in real-time.

As a result of this conscious design decision, dynamic features such as the **language toggle button** are currently disabled. The radical savings in operational costs and the improvement in security justified the temporary loss of this functionality, which remains as technical debt for future refactoring via static routing.

## ✅ The Result:
This migration transformed the project from a continuous compute model to a **serverless** static hosting model. This not only drastically reduced the monthly AWS bill to **a fraction of its original cost**, but also decreased the attack surface, eliminated the need to patch servers, and offloaded all global distribution and security workloads to AWS CloudFront, improving the **response time** for the end user.
""",

        # CONTENIDO DE LA SECCIÓN "CONTACTO"
        "contact_title": "Contact",
        "contact_header": "Got a project in mind?",
        "contact_invitation_1": "I am currently open to new opportunities, collaborations on cloud infrastructure projects, or technical consulting.",
        "contact_invitation_2": "If you're looking for a profile with technical discipline, a love for automation, and the ability to work under pressure (and with lots of coffee), let's talk!",
        "contact_cv_prompt": "Do you need my detailed profile?",
        "contact_gmail": "mickmisa3l@gmail.com",
        "contact_linkedin": "Let's connect professionally",
        "contact_github": "Check out my code and deployments",

        # CONTENIDO DE LA SECCIÓN "CERTIFICACIONES"
        "cert_title": "Certifications",
        "cert_description": "Official validation and knowledge supported by the industry.",
        "cert_list": [
            {
                "title": "AWS Certified Cloud Practitioner",
                "issuer": "Udemy",
                "date": "March 2026",
                "badge_url": "/certs/AWS_CP_Cert.webp",
                "verify_url": "https://udemy-certificate.s3.amazonaws.com/pdf/UC-278702d3-b0cd-49d9-a689-c4456046b9c6.pdf",
                "btn_verify": "Verify Credential",
            },

            {
                "title": "Docker Traning Course",
                "issuer": "KodeKloud",
                "date": "July 2025",
                "badge_url": "/certs/DOCK_TRN_COURSE_KODEKLOUD.webp",
                "verify_url": "https://lnkd.in/p/g-fxegwU",
                "btn_verify": "Verificar Credencial",
            },

            {
                "title": "Terraform: From Beginner to Certificate 2026",
                "issuer": "Udemy",
                "date": "June 2026",
                "badge_url": "/certs/TERRAFORM.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-8318999e-03c1-46a1-bd3c-64faa607e63b/",
                "btn_verify": "Verify Credential",
            },

            {
                "title": "Administration of Active Directory with Windows PowerShell",
                "issuer": "Udemy",
                "date": "June 2024",
                "badge_url": "/certs/ADM_AD_DMS_W_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-7ed2e0cd-3029-4973-a2af-367d7de59ca1/",
                "btn_verify": "Verify Credential",
            },

            {
                "title": "PowerShell Basics for Beginners",
                "issuer": "Udemy",
                "date": "May 2024",
                "badge_url": "/certs/POW_B_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-ec262e83-b38b-43b0-b411-e44dadaa7768/",
                "btn_verify": "Verify Credential",
            },

            {
                "title": "Internal Auditor for Management Systems (ISO 19011:2018 e ISO 27001:2022)",
                "issuer": "Aktiva",
                "date": "July 2023",
                "badge_url": "/certs/ISO_27001.webp",
                "verify_url": "https://www.linkedin.com/in/misael-lópez-franco-409566209/overlay/Certifications/1871249793/treasury?profileId=ACoAADTxHMkBvlU0vVhyg9M8VbXIEd5TT9D6aj4",
                "btn_verify": "Verify Credential",
            },

            {
                "title": "AD DS, DNS y DHCP on Windows Server",
                "issuer": "Udemy",
                "date": "August 2023",
                "badge_url": "/certs/AD_DNS_DHCP_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-0883095e-1b97-4b91-9040-bd23260b50de/",
                "btn_verify": "Verify Credential",
            },

            {
                "title": "Administration of Windows from the Console",
                "issuer": "Udemy",
                "date": "February 2023",
                "badge_url": "/certs/ADM_WIN_CLI_Cert.webp",
                "verify_url": "https://www.udemy.com/certificate/UC-9ad30dee-258a-4ea5-9667-b7ff443405ba/",
                "btn_verify": "Verify Credential",
            },
        ],
    }
}