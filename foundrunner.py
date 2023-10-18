import pandas as pd
# Especifica la ruta de tu archivo XLMS
#Esta seria la idea basica de como buscar un corredor desde el execel
def found_runner(a):
    xlms_file_path = '21K Merlo.xlsm'  # Reemplaza 'archivo.xlsm' con la ruta de tu archivo XLMS

# Lee el archivo XLMS en un DataFrame
    df = pd.read_excel(xlms_file_path)

# Especifica el nombre de la hoja que deseas leer
    #hoja_tiempo = 'Tiempos'
    hoja_de_inscriptos = 'Inscriptos'

   # dftime = pd.read_excel(xlms_file_path, sheet_name=hoja_tiempo)
    dfinscriptos = pd.read_excel(xlms_file_path, sheet_name=hoja_de_inscriptos)

    #Con la sisguiente linea compruevo la "Conexcion""
    corredores = dfinscriptos[['APELLIDO']]
    tiempos = dfinscriptos[['T.CHIP']]

    dorsales = dfinscriptos[['DORSAL']]
    
    a=int(a)
    if a in dorsales.values:
        #Debo crear una estructura de repeticion para buscar los datos del corredor
        #i = dorsales[dorsales == a].index[0]
        i=0
        dorsalbuscado=dorsales.iloc[a]
        
        while(i != dorsalbuscado.values):
            i+=1

        dorsal= dorsales.iloc[i-2]
        runner= corredores.iloc[i-2]
        #tiemp= tiempos.iloc[i]
        datos_corredor =[dorsal.values, runner.values, tiempos.loc[i-2]]
        return datos_corredor   
    else:
        return("Dorsal inexistente")


            

