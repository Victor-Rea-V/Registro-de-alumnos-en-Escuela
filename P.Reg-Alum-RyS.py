from datetime import datetime
import json
import os

ARCHIVO_DATOS = "academia_ritmo_sabor.json"

class AcademiaBaile:
    def __init__(self):
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(ARCHIVO_DATOS):
            try:
                with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
                    contenido = json.load(f)
                    if isinstance(contenido, dict) and "alumnos" in contenido:
                        return contenido
            except json.JSONDecodeError:
                pass
        return {"alumnos": [], "asistencias": []}

    def guardar_datos(self):
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)

    def registrar_alumno(self):
        while True:
            print("\n==================================================")
            print("          REGISTRO DE NUEVO ALUMNO                ")
            print("==================================================")
            print("💡 Escribe 'salir' en cualquier campo si deseas cancelar el registro.")

            # 1. Validar Cédula
            while True:
                cedula = input("Ingrese la Cédula / ID (solo números, mín. 7 dígitos): ").strip()
                if cedula.lower() == 'salir':
                    print("⚠️ Registro cancelado.")
                    return
                if cedula.isdigit() and len(cedula) >= 7:
                    if any(a["cedula"] == cedula for a in self.datos["alumnos"]):
                        print("❌ Error: Ya existe un alumno registrado con esa cédula. Vuelva a intentarlo.")
                        continue
                    break
                print("❌ Error: La cédula debe contener únicamente números y tener una longitud válida.")

            # 2. Validar Nombre
            while True:
                nombre = input("Nombre completo: ").strip()
                if nombre.lower() == 'salir':
                    print("⚠️ Registro cancelado.")
                    return
                if nombre and all(c.isalpha() or c.isspace() for c in nombre):
                    break
                print("❌ Error: El nombre solo debe contener letras y espacios.")

            # 3. Validar Fecha de Nacimiento
            while True:
                fecha_nac = input("Fecha de nacimiento [Formato: YYYY-MM-DD]: ").strip()
                if fecha_nac.lower() == 'salir':
                    print("⚠️ Registro cancelado.")
                    return
                try:
                    datetime.strptime(fecha_nac, "%Y-%m-%d")
                    break
                except ValueError:
                    print("❌ Error: Formato incorrecto. Use YYYY-MM-DD (Ej: 2000-05-12).")

            # 4. Validar Teléfono
            while True:
                telefono = input("Teléfono principal (solo números, mín. 7 dígitos): ").strip()
                if telefono.lower() == 'salir':
                    print("⚠️ Registro cancelado.")
                    return
                if telefono.isdigit() and len(telefono) >= 7:
                    break
                print("❌ Error: El teléfono debe contener solo números válidos.")

            # 5. Validar Correo
            while True:
                correo = input("Correo electrónico: ").strip()
                if correo.lower() == 'salir':
                    print("⚠️ Registro cancelado.")
                    return
                if "@" in correo and "." in correo and len(correo) > 5:
                    break
                print("❌ Error: Correo inválido. Asegúrese de incluir '@' y un punto.")
            
            print("\n--- FICHA MÉDICA Y EMERGENCIA ---")
            
            # 6. Teléfono de Emergencia
            while True:
                tel_emergencia = input("Teléfono de contacto de emergencia (solo números): ").strip()
                if tel_emergencia.lower() == 'salir':
                    print("⚠️ Registro cancelado.")
                    return
                if tel_emergencia.isdigit() and len(tel_emergencia) >= 7:
                    break
                print("❌ Error: El teléfono de emergencia debe contener solo números.")

            # 7. Ficha Médica
            while True:
                ficha_medica = input("Alergias o condiciones físicas (Si no tiene, escriba 'Ninguna'): ").strip()
                if ficha_medica.lower() == 'salir':
                    print("⚠️ Registro cancelado.")
                    return
                if ficha_medica:
                    break
                print("❌ Error: Este campo no puede estar vacío.")
            
            print("\n--- SELECCIÓN ACADÉMICA ---")
            
            # 8. Estilo
            estilos_dict = {
                "1": "Salsa On1", "2": "Salsa On2", "3": "Salsa Caleña",
                "4": "Bachata Sensual", "5": "Bachata Tradicional", "6": "Merengue", "7": "Urbano"
            }
            while True:
                print("\nEstilos disponibles:")
                for k, v in estilos_dict.items():
                    print(f"[{k}] {v}")
                op_estilo = input("Seleccione el número del estilo de baile: ").strip()
                if op_estilo in estilos_dict:
                    estilo = estilos_dict[op_estilo]
                    break
                print("❌ Error: Opción inválida. Elija un número del 1 al 7.")

            # 9. Nivel
            niveles_dict = {"1": "Principiante", "2": "Intermedio", "3": "Avanzado"}
            while True:
                print("\nNiveles disponibles:")
                for k, v in niveles_dict.items():
                    print(f"[{k}] {v}")
                op_nivel = input("Seleccione el número del nivel: ").strip()
                if op_nivel in niveles_dict:
                    nivel = niveles_dict[op_nivel]
                    break
                print("❌ Error: Opción inválida. Elija un número del 1 al 3.")

            # 10. Horario
            horarios_dict = {
                "1": "Mañanas (10:00 AM - 12:00 PM)", "2": "Tardes (04:00 PM - 05:00 PM)",
                "3": "Tardes (06:00 PM - 07:00 PM)", "4": "Noches (08:00 PM - 09:00 PM)"
            }
            while True:
                print("\nHorarios disponibles:")
                for k, v in horarios_dict.items():
                    print(f"[{k}] {v}")
                op_horario = input("Seleccione el número del horario: ").strip()
                if op_horario in horarios_dict:
                    horario = horarios_dict[op_horario]
                    break
                print("❌ Error: Opción inválida. Elija un número del 1 al 4.")

            # 11. Días
            dias_dict = {"1": "Lunes y Miércoles", "2": "Martes y Jueves", "3": "Viernes"}
            while True:
                print("\nDías disponibles:")
                for k, v in dias_dict.items():
                    print(f"[{k}] {v}")
                op_dias = input("Seleccione el número de los días de clase: ").strip()
                if op_dias in dias_dict:
                    dias = dias_dict[op_dias]
                    break
                print("❌ Error: Opción inválida. Elija un número del 1 al 3.")

            # Guardar alumno
            nuevo_alumno = {
                "cedula": cedula, "nombre": nombre, "fecha_nacimiento": fecha_nac,
                "telefono": telefono, "correo": correo, "emergencia": tel_emergencia,
                "ficha_medica": ficha_medica, "estilo": estilo, "nivel": nivel,
                "horario": horario, "dias": dias,
                "fecha_ingreso": datetime.now().strftime("%Y-%m-%d"),
                "estado": "Activo"
            }

            self.datos["alumnos"].append(nuevo_alumno)
            self.guardar_datos()

            # Resumen
            print("\n" + "="*50)
            print(" 🎉 ¡REGISTRO EXITOSO EN RITMO Y SABOR ECUADOR! 🎉")
            print("="*50)
            print(f"📌 Cédula / ID:          {nuevo_alumno['cedula']}")
            print(f"👤 Nombre Completo:     {nuevo_alumno['nombre']}")
            print(f"🎂 Fecha de Nacimiento: {nuevo_alumno['fecha_nacimiento']}")
            print(f"📞 Teléfono Principal:  {nuevo_alumno['telefono']}")
            print(f"📧 Correo Electrónico:  {nuevo_alumno['correo']}")
            print(f"🚨 Contacto Emergencia: {nuevo_alumno['emergencia']}")
            print(f"🏥 Ficha Médica:        {nuevo_alumno['ficha_medica']}")
            print(f"💃 Estilo de Baile:     {nuevo_alumno['estilo']}")
            print(f"📈 Nivel:               {nuevo_alumno['nivel']}")
            print(f"⏰ Horario:             {nuevo_alumno['horario']}")
            print(f"📅 Días:                {nuevo_alumno['dias']}")
            print(f"📅 Fecha de Ingreso:    {nuevo_alumno['fecha_ingreso']}")
            print(f"🟢 Estado del Alumno:   {nuevo_alumno['estado']}")
            print("="*50)

            # Opción para finalizar o continuar ingresando alumnos
            continuar = input("\n¿Desea registrar otro alumno? (s/n): ").strip().lower()
            if continuar != 's':
                print("🏁 Saliendo al menú principal...")
                break

    def listar_alumnos(self):
        alumnos = self.datos.get("alumnos", [])
        if not alumnos:
            print("\n📂 No hay alumnos registrados todavía.")
            return

        print("\n--- LISTA DE ALUMNOS INSCRITOS ---")
        for i, a in enumerate(alumnos, 1):
            print(f"{i}. [{a.get('estado', 'Activo')}] Cédula: {a.get('cedula')} | Nombre: {a.get('nombre')} | Estilo: {a.get('estilo')} ({a.get('nivel')}) | Ingreso: {a.get('fecha_ingreso')}")

    def registrar_asistencia(self):
        alumnos = [a for a in self.datos.get("alumnos", []) if a.get("estado") == "Activo"]
        if not alumnos:
            print("\n❌ No hay alumnos activos para registrar asistencia.")
            return

        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        print(f"\n--- REGISTRO DE ASISTENCIA DIARIA ({fecha_hoy}) ---")
        
        for a in alumnos:
            while True:
                asistio = input(f"¿Asistió {a.get('nombre')} ({a.get('estilo')})? (s/n): ").strip().lower()
                if asistio in ['s', 'n']:
                    break
                print("❌ Error: Digite 's' para Sí o 'n' para No.")
                
            estado_asistencia = "Presente" if asistio == 's' else "Ausente"
            
            registro = {
                "cedula": a.get("cedula"),
                "nombre": a.get("nombre"),
                "fecha": fecha_hoy,
                "estado": estado_asistencia
            }
            self.datos["asistencias"].append(registro)
        
        self.guardar_datos()
        print("✅ Asistencia registrada y guardada correctamente.")

    def calcular_mensualidad(self):
        print("\n--- CÁLCULO DE COSTOS / MENSUALIDADES ---")
        while True:
            try:
                num_personas = int(input("Ingrese el número de personas a inscribir juntas (1, 2 o 3): "))
                if num_personas == 1:
                    total = 45
                    break
                elif num_personas == 2:
                    total = 80
                    break
                elif num_personas >= 3:
                    total = 100
                    break
                else:
                    print("❌ Cantidad no válida. Debe ser mayor o igual a 1.")
            except ValueError:
                print("❌ Error: Debe ingresar un número entero válido.")
        print(f"💰 El valor total a pagar por {num_personas} persona(s) es: ${total} USD.")

    def reporte_inscripciones_por_mes(self):
        alumnos = self.datos.get("alumnos", [])
        if not alumnos:
            print("\n📂 No hay alumnos registrados para generar el reporte.")
            return

        conteo_meses = {}
        for a in alumnos:
            fecha_ingreso = a.get("fecha_ingreso", "")
            if len(fecha_ingreso) >= 7:
                mes_anio = fecha_ingreso[:7]
                conteo_meses[mes_anio] = conteo_meses.get(mes_anio, 0) + 1

        print("\n==================================================")
        print("      REPORTE DE INSCRIPCIONES POR MES           ")
        print("==================================================")
        for mes, cantidad in sorted(conteo_meses.items()):
            print(f"📅 Mes ({mes}): ➔ {cantidad} alumno(s) nuevo(s)")
        print("==================================================")

def main():
    academia = AcademiaBaile()
    
    while True:
        print("\n==================================================")
        print("   ACADEMIA DE BAILE 'RITMO Y SABOR ECUADOR'     ")
        print("==================================================")
        print("1. Registrar nuevo alumno")
        print("2. Ver lista de alumnos")
        print("3. Registrar asistencia diaria")
        print("4. Calcular costos / mensualidad")
        print("5. Ver reporte de inscripciones por mes")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            academia.registrar_alumno()
        elif opcion == "2":
            academia.listar_alumnos()
        elif opcion == "3":
            academia.registrar_asistencia()
        elif opcion == "4":
            academia.calcular_mensualidad()
        elif opcion == "5":
            academia.reporte_inscripciones_por_mes()
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema! ¡A bailar se ha dicho! 🎶")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()