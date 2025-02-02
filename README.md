# 🚀 Desarrollo de un LLM Personalizado para la Resolución de Dudas Técnicas en la Instalación de un Sistema SONAR

## 📌 Introducción al Problema
En nuestra empresa, la instalación y configuración de sistemas **SONAR** es un proceso técnico que requiere conocimientos específicos. Para mejorar la eficiencia y reducir la dependencia de documentación extensa, buscamos desarrollar un **modelo de lenguaje (LLM) personalizado** que pueda responder preguntas técnicas de manera precisa y rápida.  

El objetivo principal es que los técnicos y usuarios puedan resolver sus dudas sin necesidad de revisar manualmente múltiples documentos.

---

## 🛠️ Metodología y Enfoque

### 📖 1. Estructuración de la información  
✅ **Extracción de datos**:  
- Se analizaron **tres documentos PDF** con información técnica sobre el sistema **SONAR**.  
- Utilizamos **LangChain** para segmentar la información por encabezados, permitiendo una organización clara y estructurada.  
- Generamos un **JSON con preguntas y respuestas (QA)** basado en los documentos, asegurando ejemplos específicos y relevantes.  

### 🤖 2. Evaluación de Modelos  
✅ **Modelos evaluados**:  
- **google-t5/t5-base** → **Entrenado completamente, sin cuantificación**.  
- **BSC-LT/salamandra-2b-instruct** → **Cuantificado a 4 bits y ajustado con LoRA**.  

📊 **Resultados**:  
El modelo **google-t5/t5-base**, entrenado sin cuantificación, ofreció **mejores respuestas** en términos de precisión y coherencia que **BSC-LT/salamandra-2b-instruct**, que estaba cuantificado a 4 bits.

### 💻 3. Implementación de la Interfaz  
✅ **Desarrollo con Streamlit**  
- Se creó una **interfaz de usuario en Streamlit** para permitir la interacción con el LLM de manera sencilla y eficiente.  
- Esto permite que los técnicos accedan rápidamente a respuestas sin necesidad de consultar manualmente los documentos.

---

## 📊 Conclusiones y Resultados  

🔹 **LangChain** ayudó a estructurar los datos eficientemente, mejorando la calidad del entrenamiento.  
🔹 **El modelo google-t5/t5-base sin cuantificación superó al BSC-LT/salamandra-2b-instruct cuantificado**, mostrando que la capacidad de procesamiento es clave en modelos generativos.  
🔹 **La integración con Streamlit** permitió crear una interfaz accesible, reduciendo la carga de soporte técnico.  
🔹 Este **LLM personalizado mejora la productividad** y optimiza la resolución de dudas técnicas.  

✅ **Conclusión:** Hemos demostrado que la personalización de modelos LLM con datos específicos de la empresa puede ser una solución eficiente para el soporte técnico y la automatización del conocimiento técnico.  

🚀 ¡Este proyecto marca un gran avance en la optimización del acceso a información técnica en nuestra empresa!  

---
