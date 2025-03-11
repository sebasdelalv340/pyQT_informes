from fpdf import FPDF
import sqlite3
import os

class ClientePDF(FPDF):

    def fetch_data(self):
        """Consulta SQL para obtener los datos"""
        bd_file = os.path.join(os.path.dirname(__file__), "hotel.db")
        conn = sqlite3.connect(bd_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, apellido1, apellido2, email, dni FROM clientes")  # Cambia según tu tabla
        data = cursor.fetchall()
        conn.close()
        return data

    def header(self):
        # Agregar logo
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        self.image(logo_path, 10, 8, 30)  # Posición y tamaño

        """Agregar cabecera del informe"""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'INFORME DE CLIENTES', 0, 1, 'C')

        # Línea separadora
        self.ln(10)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(10)

    def footer(self):
        """Agregar pie de página con numeración"""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def create_pdf(self):
        """Generar el PDF con los datos obtenidos de la base de datos"""
        self.add_page()

        # Obtener datos de SQL
        data = self.fetch_data()

        # Agregar logo (si tienes uno)
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        self.image(logo_path, 10, 8, 30)  # Posición y tamaño

        # Agregar tabla con los datos
        self.set_font('Arial', '', 12)

        # Encabezado de la tabla
        self.cell(15, 10, 'ID', 1, 0, 'C')
        self.cell(30, 10, 'Nombre', 1, 0, 'C')
        self.cell(30, 10, 'Apellido 1', 1, 0, 'C')
        self.cell(30, 10, 'Apellido 2', 1, 0, 'C')
        self.cell(55, 10, 'Email', 1, 0, 'C')
        self.cell(30, 10, 'DNI', 1, 1, 'C')  # Añadido el campo DNI

        self.set_font('Arial', '', 8)

        # Rellenar la tabla con los datos
        for row in data:
            self.cell(15, 10, str(row[0]), 1, 0, 'C')  # ID
            self.cell(30, 10, row[1], 1, 0, 'C')  # Nombre
            self.cell(30, 10, row[2], 1, 0, 'C')  # Apellido 1
            self.cell(30, 10, row[3], 1, 0, 'C')  # Apellido 2
            self.cell(55, 10, row[4], 1, 0, 'C')  # Email
            self.cell(30, 10, row[5], 1, 1, 'C')  # DNI

        # Guardar el PDF
        pdf = os.path.join(os.path.dirname(__file__), "informe_clientes.pdf")
        self.output(pdf)
        print(f"PDF generado correctamente: {pdf}")

        self.open_pdf(pdf)

    def open_pdf(self, pdf_path):
        """Abrir el PDF después de crearlo"""
        os.startfile(pdf_path)



