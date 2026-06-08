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
        "description_2": "Actualmente estoy estudiando diferentes cursos para formarme como DevOps Engieneer.",
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
        "project_1": "StackTON",
        "project_1_description": "Startup de Arquitectura de Soluciones. Implementaciones de Infraestrucura en AWS y desarrollo web con Reflex y Stack convencional.",
        "project_2": "Python | Script de Métodos Numéricos",
        "project_2_description": "Resolver problemas matemáticos complejos mediante aproximaciones computacionales, iteraciones y optimización de recursos, minimizando el margen de error.",
        "project_3": "Futuro Proyecto",
        "project_3_description": "En proceso de desarrollo... ¡Pronto habrá novedades!",
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
        "project_1": "StackTON",
        "project_1_description": "Architecture of IT Solutions. Implementations of Infrastructure in AWS and web development with Reflex and conventional Stack.",
        "project_2": "Python | Numeric Methods Script",
        "project_2_description": "A Python script that implements various numerical methods for solving mathematical problems, such as root finding, numerical integration, and differential equations.",
        "project_3": "Future Project",
        "project_3_description": "In development... Stay tuned for updates!",
        "project_4": "Future Project",
        "project_4_description": "In development... Stay tuned for updates!",
        "project_5": "Future Project",
        "project_5_description": "In development... Stay tuned for updates!",
        "project_6": "Future Project",
        "project_6_description": "In development... Stay tuned for updates!",

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