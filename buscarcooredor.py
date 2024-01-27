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
        tiempo = corredor_data['T.CHIP'].values[0]
        #si encontramos encontramos al corredor verificamos si el tiempo es distinto de nan
        if pd.isna(tiempo):  # Verifica si el valor de 'Tiempo' es NaN
            dorsal = corredor_data['DORSAL'].values[0]
            runner = corredor_data['APELLIDO'].values[0]
            tiempo = "El Tiempo es NaN"
            datos_corredor = [dorsal, runner, tiempo]
            return datos_corredor
        dorsal = corredor_data['DORSAL'].values[0]
        runner = corredor_data['APELLIDO'].values[0]
        tiempo = corredor_data['T.CHIP'].values[0]
        posicion_general = corredor_data['POS. GRAL'].values[0]
        posicion_categoria = corredor_data['POS. CAT'].values[0]

        datos_corredor = [dorsal, runner, tiempo,posicion_general,posicion_categoria]
        return datos_corredor
    else:
        return "Dorsal inexistente"
