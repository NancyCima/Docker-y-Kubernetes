### **Infraestructura en Kubernetes para la Aplicación FastAPI**

#### **Introducción**
Para desplegar la aplicación que desarrollé con FastAPI en Kubernetes, propongo una infraestructura en Kubernetes para desplegar y escalar la aplicación FastAPI. El objetivo principal es garantizar que la aplicación sea fácil de mantener, escalar y desplegar de manera eficiente.

---

#### **Propuesta de Infraestructura**
1. **Pods:**  
   Cada instancia de la aplicación FastAPI correrá en un contenedor gestionado por un Pod. Los Pods son la unidad básica de Kubernetes y contendrán nuestra aplicación Dockerizada.  

2. **Deployments:**  
   Utilizar un Deployment nos permitirá manejar automáticamente la cantidad de Pods, actualizaciones y el escalamiento según sea necesario. Se configurará una estrategia de **RollingUpdate** para asegurar despliegues seguros.  

3. **Servicios (Services):**  
   Para exponer la aplicación FastAPI, se usará un `Service` de tipo `NodePort` en entornos locales (Docker Desktop) o `LoadBalancer` en GKE.  

4. **Persistencia (si aplica):**  
   Aunque FastAPI no requiere almacenamiento por defecto, configuraremos un volumen persistente para logs o archivos temporales.

---

### **Cambios en la Arquitectura**
Para adaptarnos mejor a Kubernetes:
- Implementaría escalamiento horizontal mediante el aumento de réplicas en el Deployment.
- Usaría un sistema de persistencia basado en **PersistentVolume** y **PersistentVolumeClaim** si la aplicación necesita almacenamiento local.
- Definiría límites de recursos para evitar el consumo excesivo de CPU y memoria.

---

### **Ejemplos de Configuración YAML**

A continuación, se presentan archivos de configuración YAML de ejemplo.

#### **Deployment (Cómputo)**  
Este Deployment asegura que siempre haya tres réplicas corriendo, con una estrategia de actualización incremental (RollingUpdate).

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-deployment
  labels:
    app: fastapi
spec:
  replicas: 3  # Número de Pods activos
  selector:
    matchLabels:
      app: fastapi
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  template:
    metadata:
      labels:
        app: fastapi
    spec:
      containers:
      - name: fastapi-container
        image: fastapi-server:latest  # Imagen creada previamente con Docker
        ports:
        - containerPort: 8080
        resources: # Límites de CPU y memoria para los Pods
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"
```
Este archivo crea tres réplicas de la aplicación, configuradas para trabajar en paralelo y manejar tráfico de manera equilibrada.

---

#### **Service (Red)**  
Para exponer la aplicación, configuré un `Service` que expone la aplicación a través de un puerto accesible externamente en entornos locales o en la nube.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  selector:
    app: fastapi
  ports:
    - protocol: TCP
      port: 80  # Puerto externo
      targetPort: 8080  # Puerto dentro del contenedor
  type: NodePort  # Cambiar a LoadBalancer para GKE
```

---

#### **Persistencia (Volumen)**  
Si la aplicación necesita guardar información, usaría un volumen persistente. Aquí está el YAML correspondiente:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: fastapi-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data" # Ruta local en el nodo (solo para entornos locales)
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: fastapi-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Este volumen se puede usar en los Pods mediante un `volumeMount` para guardar datos de forma persistente. Para esto se monta en el Pod configurándolo en el Deployment:

```yaml
      volumeMounts:
      - mountPath: "/app/data"
        name: storage
    volumes:
    - name: storage
      persistentVolumeClaim:
        claimName: fastapi-pvc
```

---


### **Pasos para Probar en Docker Desktop**
1. **Habilitar Kubernetes en Docker Desktop:**  
   Verifica que Kubernetes esté habilitado desde la configuración de Docker Desktop.  

2. **Aplicar los archivos YAML:**  
   Ejecuta los siguientes comandos para desplegar la infraestructura:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   kubectl apply -f persistent-volume.yaml
   ```

3. **Verificar el estado de los Pods:**  
   Asegúrate de que los Pods estén corriendo correctamente:
   ```bash
   kubectl get pods
   ```

4. **Acceder a la Aplicación:**  
   Encuentra el puerto asignado al `NodePort`:
   ```bash
   kubectl get service fastapi-service
   ```
   Luego accede a la aplicación desde el navegador o mediante herramientas como `curl`.

---

### **Conclusión**
Con esta infraestructura, la aplicación FastAPI puede desplegarse fácilmente en un clúster de Kubernetes, aprovechando sus capacidades de escalamiento y manejo de recursos. En GKE, solo sería necesario ajustar el tipo de `Service` a `LoadBalancer` y configurar un autoscaler para optimizar el rendimiento en entornos de alta carga.

Además, esta estructura es flexible y puede adaptarse fácilmente a nuevos requerimientos.