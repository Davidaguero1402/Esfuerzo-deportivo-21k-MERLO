from flask import Flask, render_template, request

from buscarcooredor import found_runner

from contadorcorredores import Contar_corredores

app = Flask(__name__)

cantidad_de_corredores = Contar_corredores()

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'POST':
        dorsal = request.form.get('dorsal') #esto es el elemento name de la etiqueta del formulario
        print(dorsal)

        if dorsal is not None:
            
            datos_corredor = found_runner(dorsal)
            print(datos_corredor)

            if datos_corredor != 'Dorsal inexistente' and  datos_corredor[2]!='El Tiempo es NaN':
                print("estoy aca")
                #print(datos_corredor)

                datos={'dorsal':datos_corredor[0], 'titulo': 'Tu tiempo','nombre':datos_corredor[1],'tiempo': datos_corredor[2],'posicion_general': datos_corredor[3], 'posicion_categoria':datos_corredor[4]}
                #Devolvemos los datos del corredor
                return render_template('tutiempo.html', datos = datos)
            #si el corredor de no tiene tiempo asignado devolvemos
            elif datos_corredor[2] == 'El Tiempo es NaN':
                print("estoy aca timpo nan")
                datos={'dorsal':dorsal, 'titulo': 'Tiempo no encontrado','nombre':datos_corredor[1],'tiempo': "Lo sentimos no tienes tiempo asignado"}
                return render_template('tiemponan.html', datos = datos)
                
            else:
                print("estoy aca else")
                #sino encontramos al dorsal que se busco retornamos otra pagina dorsalnotfound
                datos={'dorsal':dorsal, 'titulo': 'Dorsal no encontrado', 'nombre':datos_corredor[1]}
                return render_template('dorsalnotfound.html', datos = datos)
    

    diccionario_index = {'corredores': cantidad_de_corredores, 'titulo':'Esfuerzo deportivo' }

    return render_template('index.html',diccionario=diccionario_index)
 



if __name__ == '__main__':
    print('Ejecutando la aplicación en el puerto 8000...')
    
    app.run(host='0.0.0.0' ,port=8000, debug=True)
