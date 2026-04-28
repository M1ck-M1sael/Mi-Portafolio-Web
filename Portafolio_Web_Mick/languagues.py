# languages.py

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
        # CONTENIDO DE LA SECCIÓN "SOBRE MÍ"
        "about_title": "Sobre mí",
        "about_name": "¡Hola! Soy Misael.",
        "description_1": "Soy estudiante de Ingeniería en Sistemas Computacionales en el Tecnológico Nacional de México, y actualmente trabajo como Systems Administrator, en donde gestiono infraestructura, soporte y operación de sistemas en entornos productivos.",
        "description_2": "También tengo mi propia Startup llamada StackTON, una empresa de soluciones IT. En ella soy CEO y Arquitecto Cloud con AWS.",
        "description_3": "Me caracterizo por el aprendizaje constante y la diciplina técnica. Actualmente me encuentro en proceso de obtener la certificación AWS Cloud Practitioner, fortaleciendo mis conocimientos en servicios cloud, buenas prácticas y arquitectura básica.",
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
        "project_2": "Futuro Proyecto",
        "project_2_description": "En proceso de desarrollo... ¡Pronto habrá novedades!",
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
        "contact_invitation_1": "Actualmente estoy abierto a nuevas oportunidades, colaboraciones en proyectos de infraestructura Cloud o consultorías técnicas a través de StackTON.",
        "contact_invitation_2": "Si buscas un perfil con disciplina técnica, amor por la automatización y que sepa trabajar bajo presión (y con mucho café), ¡hablemos!",
        "contact_cv_prompt": "¿Necesitas mi perfil detallado?",
        "contact_gmail": "mickmisa3l@gmail.com",
        "contact_linkedin": "Conectemos profesionalmente",
        "contact_github": "Revisa mi código y despliegues",
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

        # CONTENIDO DE LA SECCIÓN "SOBRE MÍ"
        "about_title": "About me",
        "about_name": "Hello there! I'm Misael.",
        "description_1": "I am a Computer Systems Engineering student at Tecnológico Nacional de México and currently work as a Systems Administrator, managing infrastructure, support, and system operations in production environments.",
        "description_2": "I also lead my own IT solutions startup, StackTON, where I serve as CEO and AWS Cloud Architect.",
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
        "project_2": "Future Project",
        "project_2_description": "In development... Stay tuned for updates!",
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
        "contact_invitation_1": "I am currently open to new opportunities, collaborations on cloud infrastructure projects, or technical consulting through StackTON.",
        "contact_invitation_2": "If you're looking for a profile with technical discipline, a love for automation, and the ability to work under pressure (and with lots of coffee), let's talk!",
        "contact_cv_prompt": "Do you need my detailed profile?",
        "contact_gmail": "mickmisa3l@gmail.com",
        "contact_linkedin": "Let's connect professionally",
        "contact_github": "Check out my code and deployments",
    }
}