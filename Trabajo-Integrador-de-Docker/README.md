# **FastAPI Docker Server - Text Analyzer**  

Este proyecto implementa un servidor HTTP utilizando **FastAPI** que ofrece un servicio de análisis de texto. Este servidor está diseñado para ejecutarse dentro de un contenedor Docker, asegurando portabilidad y facilidad de despliegue.  

## **Características**  
El servidor proporciona un endpoint `/analyze_text` que:  
- Calcula la longitud del texto enviado.  
- Cuenta el número de palabras.  
- Convierte el texto a mayúsculas.  
- Invierte el texto.  

Incluye validación de entrada y genera documentación interactiva automáticamente.  

---

## **Estructura del proyecto**  
```
Trabajo-Integrador-de-Docker/
│
├── app/
│   ├── main.py              # Código principal del servidor FastAPI
│   ├── requirements.txt     # Dependencias del proyecto
│
├── Dockerfile               # Instrucciones para construir la imagen Docker
├── README.md                # Instrucciones y descripción del proyecto
└── inputs_outputs.txt       # Ejemplos de pruebas con inputs y outputs esperados
```

---

## **Requisitos previos**  
Asegúrate de tener instalado:  
- [Docker](https://www.docker.com/)  
- [Git](https://git-scm.com/)  

---

## **Cómo usar este proyecto**  

### 1. Clonar el repositorio  
```bash
git clone https://github.com/NancyCima/Docker-y-Kubernetes.git
cd Trabajo-Integrador-de-Docker
```

### 2. Construir la imagen Docker  
```bash
docker build -t fastapi-server .
```

### 3. Ejecutar el contenedor  
```bash
docker run -d -p 8080:8080 fastapi-server
```

### 4. Acceder al servidor  
El servidor estará disponible en [http://localhost:8080](http://localhost:8080).  

### 5. Probar el endpoint  
Envía solicitudes HTTP al endpoint `/analyze_text` con el parámetro `text`. Por ejemplo:  
```bash
curl "http://localhost:8080/analyze_text?text=Hola%20mundo"
```

### 6. Explorar la documentación interactiva  
FastAPI genera documentación automáticamente:  
- **Swagger UI**: [http://localhost:8080/docs](http://localhost:8080/docs)  
- **Redoc**: [http://localhost:8080/redoc](http://localhost:8080/redoc)  

---

## **Ejemplo de entrada y salida**  

### **Solicitud**  
```bash
GET http://localhost:8080/analyze_text?text=Hola%20mundo
```  

### **Respuesta (JSON)**  
```json
{
  "original_text": "Hola mundo",
  "length": 10,
  "word_count": 2,
  "uppercase": "HOLA MUNDO",
  "reversed": "odnum aloH"
}
```

---

## **Customización**  
Si deseas cambiar la lógica del análisis, edita el archivo `app/main.py` y personaliza la función `analyze_text`.  

---

## **Notas técnicas**  
### **Dependencias**  
Las dependencias del proyecto están definidas en el archivo `requirements.txt` y se instalan automáticamente durante el proceso de construcción del Dockerfile:  
- `fastapi`: Framework web rápido y moderno para construir APIs.  
- `uvicorn`: Servidor ASGI para ejecutar aplicaciones FastAPI.  

### **Dockerfile**  
El Dockerfile define un entorno ligero basado en Python 3.10 slim. Expone el puerto `8080` y utiliza **Uvicorn** como servidor de producción.  

### **Comandos útiles**  
#### Detener el contenedor:  
```bash
docker ps        # Obtén el ID del contenedor en ejecución
docker stop <CONTAINER_ID>
```  

#### Listar imágenes Docker:  
```bash
docker images
```  

#### Eliminar una imagen Docker:  
```bash
docker rmi fastapi-server
```  
---

### **Fundamentación de las tecnologías elegidas**

Elegí **Python** como lenguaje para este proyecto porque es con el que me siento más cómoda, ya que es el lenguaje que uso en mi día a día, tanto en la universidad como en el trabajo, por lo que tengo mucha experiencia con él.

Por otro lado, seleccioné **FastAPI** porque ya lo he utilizado en proyectos académicos y laborales. Es un framework que me resulta práctico por lo rápido que se puede implementar una API funcional y bien documentada.

En resumen, opté por estas tecnologías porque son las que mejor manejo y las que considero más adecuadas para este tipo de proyectos.

---

## **To-Do**  
1. Agregar más funcionalidades al análisis de texto (por ejemplo, detectar lenguaje o frecuencia de palabras).  
2. Implementar pruebas automatizadas con `pytest`.  
3. Crear un pipeline CI/CD para despliegue automático.  

---

## **Licencia**  
Este proyecto es de código abierto bajo la licencia MIT. Siéntete libre de modificarlo y adaptarlo a tus necesidades.  

**¡Gracias por probar este servidor!** 🚀  
