import pandas as pd



def Contar_corredores():
    xlms_file_path = '21K Merlo.xlsm'  # Reemplaza 'archivo.xlsm' con la ruta de tu archivo XLMS

    # Lee el archivo XLMS en un DataFrame
    dfinscriptos = pd.read_excel(xlms_file_path, sheet_name='Inscriptos')


    # Busca el dorsal en la columna 'DORSAL'
    corredores = dfinscriptos[['APELLIDO']].nunique()

    return corredores.iloc[0]



