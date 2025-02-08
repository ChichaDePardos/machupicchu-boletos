# 🎟️ Adquiere tu Boleto - Machu Picchu

Aplicación GUI para consultar disponibilidad de boletos, circuitos, rutas y horarios en Machu Picchu. Desarrollada con Python y Tkinter, integrada con la API oficial del Ministerio de Cultura de Perú.

![image](https://github.com/user-attachments/assets/724484de-c553-47fb-b65d-6c9688e552c3)


## 🚀 Características principales
- **Selección interactiva**:  
  ✔️ Circuitos oficiales de Machu Picchu  
  ✔️ Rutas disponibles por circuito (actualizadas en tiempo real)  
- **Calendario visual**:  
  📅 Fechas disponibles resaltadas en verde  
  ⚠️ Temporada alta/baja indicada en las rutas  
- **Horarios en tiempo real**:  
  🕒 Intervalos de ingreso con cupos disponibles  
  🔄 Actualización automática al seleccionar fecha  
- **Diseño intuitivo**:  
  🖥️ Interfaz responsive y fácil de navegar  
  📱 Compatible con múltiples resoluciones  

## 📋 Requisitos previos
- **Python 3.8 o superior**  
  [Descargar Python](https://www.python.org/downloads/)
- **Dependencias** (instalación automática en el siguiente paso):
  ```bash
  requests      # Para solicitudes HTTP
  tkinter       # Interfaz gráfica (generalmente incluido con Python)
  tkcalendar    # Widget de calendario interactivo
  ```

## ⚙️ Instalación paso a paso
1. Clona el repositorio:
   ```bash
   git clone https://github.com/ChichaDePardos/machupicchu-boletos.git
   cd machupicchu-boletos
   ```
2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   *(Crea un archivo `requirements.txt` con este contenido:*
   ```
   requests==2.31.0
   tkcalendar==1.6.1
   *No incluir tkinter - viene con Python*)

## 🖥️ Cómo usar la aplicación
1. **Iniciar**:
   ```bash
   python app.py
   ```
2. **Flujo de uso**:
   1. Selecciona un circuito → Las rutas disponibles aparecerán automáticamente
   2. Elige una ruta → El calendario mostrará fechas disponibles en verde
   3. Haz clic en una fecha → Los horarios con cupos aparecerán en la lista inferior
   4. Doble clic en un horario → (Implementar lógica de reserva según tus necesidades)

## 🚨 Notas importantes
- **Conexión a Internet**: Requerida para consultar la API oficial
- **Certificados SSL**: Las verificaciones están deshabilitadas (seguir [estas instrucciones](https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification) para producción)
- **Temporadas**: Algunas rutas solo están disponibles en temporada alta (noviembre-abril)

## 🤝 Contribuciones
¡Tus aportes son bienvenidos! Sigue estos pasos:
1. Reporta errores o sugerencias en [Issues](https://github.com/tu-usuario/machupicchu-boletos/issues)
2. Para cambios de código:
   ```bash
   fork → feature branch → pruebas → pull request
   ```
3. **Guía de estilo**:
   - PEP8 para código Python
   - Comentarios en español/inglés
   - Tests para nuevas funcionalidades

## 📄 Licencia
MIT License - Ver [LICENSE](LICENSE) para detalles completos.

---

**⚠️ Disclaimer**: Proyecto no oficial con fines educativos.  
Los datos provienen de la API pública del [Ministerio de Cultura del Perú](https://www.cultura.gob.pe/).  
No garantiza la disponibilidad real de boletos - consultar siempre fuentes oficiales.
