import pandas as pd

def found_runner(a):
    xlms_file_path = '21K Merlo.xlsm'  # Reemplaza 'archivo.xlsm' con la ruta de tu archivo XLMS

    # Lee el archivo XLMS en un DataFrame
    dfinscriptos = pd.read_excel(xlms_file_path, sheet_name='Inscriptos')

    # Convierte 'a' en un entero
    a = int(a)

    # Busca el dorsal en la columna 'DORSAL'
    corredor_data = dfinscriptos[dfinscriptos['DORSAL'] == a]

    # Verifica si se encontró el corredor
    if not corredor_data.empty:
        dorsal = corredor_data['DORSAL'].values[0]
        runner = corredor_data['APELLIDO'].values[0]
        tiempo = corredor_data['T.CHIP'].values[0]
        datos_corredor = [dorsal, runner, tiempo]
        return datos_corredor
    else:
        return "Dorsal inexistente"
