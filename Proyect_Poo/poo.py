import speech_recognition as sr
import pyttsx3
import webbrowser
# name of the virtual assistant
name = 'daniela'


# your api key
key = 'YOUR_API_KEY_HERE'

# the flag help us to turn off the program
flag = True

listener = sr.Recognizer()

engine = pyttsx3.init()

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    '''
        here, virtual assistant can talk
    '''
    engine.say(text)
    engine.runAndWait()

def listen():
    '''
        The program recover our voice and it sends to another function
    '''
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag

def run(rec):
    if ' universidad de medellín'  in rec:
        print("ola")
        talk("Abriendo la pagina ")
        webbrowser.open("https://udemedellin.edu.co/")
    
    elif "teléfono " in rec:
        talk(" el telefono fijo de la universidad de medellín es: 604 5904500, te recuerdo que el 604 es la extensión para llamar a telefonos fijos en medellín si eres de otra ciudad busca el numero de extensión y agregalo al numero")
        print("604 5904500")
    elif "horario de atención" in rec:
        talk("El horario de atención de la universidad de medellín es de lunes a viernes, 8 a. m. - 12 pm ,y 2 p. m. - 6 p. m")

    elif "calendario institucional" in rec:
        with sr.Microphone() as source:
            talk("Dime, ¿Eres estudiante nuevo o antiguo?")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            print(rec)
            if name in rec:
                if "nuevo" in rec:
                    try:
                        print("inscripción, entrevistas, elección de horarios, inducción")
                        talk("Dime en cual de estas fechas del calendrio institucional para los estudiantes nuevos estas interesado")
                        if name in rec:
                                talk("entré")
                                if "inscripcion" in rec:
                                    talk("Las fechas de inscripciónes de estudiantes nuevos son el 5 de septiembre y 23 de enero del 2023")
                                elif "entrevistas" in rec:
                                    talk("Las entrevistas para los estudiantes que quieren ingresar a nuestra universidad son desde el 4 de octubre del 2022")
                                elif "elección de horario" in rec:
                                    talk("Las elecciónes de horario para los estudiantes nuevos son el 28 de noviembre del 2022")
                                elif "inducción" in rec:
                                    talk("La inducción es el 24 y 25 de enero del 2023")
                                else:
                                    talk("Vuelve a intentarlo, no reconozco: " + rec)
                    except:
                        pass
                    return flag

                elif "antiguo" in rec:
                    try:
                        print("consulta virtual de notas definitivas, consulta virtual de asesoria de prematricula, registro virtual de prematricula y consulta de comprobante de pago, consulta virtual de horario de clase")
                        talk("Dime en cual de estas fechas del calendrio institucional para los estudiantes nuevos estas interesado")
                        with sr.Microphone() as source:
                            voice = listener.listen(source)
                            rec = listener.recognize_google(voice, language='es-ES')
                            rec = rec.lower()
                            print(rec)
                            if "consulta virtual" in rec:
                                talk("Desde el 12 de diciembre del 2022 se podrán consultar las notas definitivas")
                                print("12 de diciembre")
                            elif "consulta virtual de asesoria de prematricula" in rec:
                                talk("Desde el 12 de diciembre se podrán consultar las notas definitivas")
                                print("12 de diciembre del 2022")
                            elif "registro virtual de prematricula y consulta comprobante de pago" in rec:
                                talk("disponible desde 14 y 19 de diciembre, estas fechas aparecian en la prematricula")
                                print("14 y 19 de diciembre del 2023")
                            elif("consulta virtual de horario de clases") in rec:
                                talk("podrás consultar el horario de clases el 27 de enero del 2023")
                                print("27 de enero del 2023")
                    except:
                            pass
                    return flag

    elif "carreras" in rec:
        talk("¿carreras de pre-grado o posgrado? ")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice, language='es-ES')
        rec = rec.lower()
        print(rec)
        if name in rec:
            if "pregrado" in rec:
                talk("¿de que facultad quieres averiguar las carreras de pregrado?")
                voice = listener.listen(source)
                rec = listener.recognize_google(voice, language='es-ES')
                rec = rec.lower()
                print(rec)
                if name in rec:
                    if "derecho" in rec:
                        talk("Derecho, investigación criminal")
                        print("Derecho, investigación criminal")
                    elif "comunicacion" in rec:
                        talk("comunicación y relaciones cooperativas, comunicación grafica publicitaria, comunicación grafica y lenguajes audiovisaules, comunicación y entretenimiento digital")
                        print("comunicación y relaciones cooperativas, comunicación grafica publicitaria, comunicación grafica y lenguajes audiovisaules, comunicación y entretenimiento digital")
                    elif "ingenierías" in rec:
                        talk("Ingeniería ambiental, Ingeniería de sistemas, Ingeniería financiera, Ingeniería civil, Ingeniería industrual, Ingeniería en energia, Ingeniería en telecomunicaciones, Ingeniería electrónica")
                        print("Ingeniería ambiental, Ingeniería de sistemas, Ingeniería financiera, Ingeniería civil, Ingeniería industrual, Ingeniería en energia, Ingeniería en telecomunicaciones, Ingeniería electrónica")
                    elif "ciencias economicas y administrativas" in rec:
                        talk("administración de empresas, negocios internacionales, contaduria publica, economía, mercadeo")
                        print("administración de empresas, negocios internacionales, contaduria publica, economía, mercadeo")
                    elif "ciencias sociales y humanas" in rec:
                        talk("psicología, ciencias politicas")
                        print("psicología, ciencias politicas")
                    elif "ciencias basicas" in rec:
                        talk("computación cientifica")
                        print("computación cientifica")
                    elif "diseño" in rec:
                        talk("diseño y gestión de espacios, diseño y gestion de la moda y el textíl, diseño y gestión de producto")
                        print("diseño y gestión de espacios, diseño y gestion de la moda y el textíl, diseño y gestión de producto")

    elif " facultades" in rec:
        print("Centro de idiomas, ciencias basicas, ingenierias, ciencias economicas y administrativas, ciencias sociales y humanas, comunicación, derecho")
        with sr.Microphone() as source:
            talk("por favor dime cual de estas te gustaría visitar")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            print(rec)
            if name in rec:
                if "centro de idiomas" in rec:
                    talk("Abriendo enlace de la facultad de centro de idiomas")
                    webbrowser.open("https://www.udem.edu.co/index.php/servicios/centro-de-idiomas")
                elif "ciencias básicas" in rec:
                    talk("Abirendo enlace a la facultad de ciencias basicas")
                    webbrowser.open("https://cienciasbasicas.udemedellin.edu.co/#gsc.tab=0")
                elif "ingenierías" or "ingeniería" in rec:
                    talk("Abirendo enlace a la facultad de ingenierias")
                    webbrowser.open("https://ingenierias.udemedellin.edu.co/")
                elif "ciencias económicas y administrativas" in rec:
                    talk("Abriendo enlace de ciencias economicas y administrativas")
                    webbrowser.open("https://fcea.udemedellin.edu.co/")
                elif "ciencias sociales y humanas" in rec:
                    talk("Abriendo enlace de la facultad de ciencias sociales y humanas")
                    webbrowser("https://www.udem.edu.co/index.php/matricula/53-ciencias-sociales-y-humanas")
                elif "comunicación" in rec:
                    talk("Abriendo enlace de la facultad de comunicación")
                    webbrowser("https://comunicacion.udemedellin.edu.co/")
                elif "derecho" in rec:
                    talk("Abriendo enlace de la facultad de derecho")
                    webbrowser("https://derecho.udemedellin.edu.co/#gsc.tab=0") 
    
    elif 'diplomados' in rec:
        talk("La universidad de Medellín cuenta con muchos programas de diplomados, al ser tantos te rediccionaré al apartado de diplomaturas en la pagina de la udem para que así los puedas ver tranquilamente")
        webbrowser.open("https://educacioncontinuada.udemedellin.edu.co/diplomaturas/")

    elif "pensum" in rec:
       with sr.Microphone() as source:
            talk ("Dime, ¿De que carrera deseas el pensum?\nderecho\ninvestigación criminal\nrelaciones corpotativas\ncomunicación gráfica publicitaria\nlenguajes audiovisuales\nentretenimiento digital\ningeniería ambiental\ningeniería civil\ningeniería de sistemas\ningeniería financiera\ningeniería en telecomunicaciones\ningeniería industrial\ningeniería electrónica\nadministración de empresas\nnegocios internacionales\ncontaduria pública\neconomía\nmercadeo\npsicología\nciencias políticas\ncomputación cientifica\ndiseño y gestión de espacios\ngestión moda y textil\ngestión del producto")

            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            print(rec)
            if name in rec:
                try:

                            talk("entré")
                            if "derecho" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de derecho ")
                                webbrowser.open("https://derecho.udemedellin.edu.co/wp-content/uploads/2022/09/plan-de-formacion-Derecho.pdf")
                            elif "investigación criminal" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de investigación criminal")
                                webbrowser.open("https://derecho.udemedellin.edu.co/wp-content/uploads/2022/10/investigacion_criminal_presencial.pdf")
                            elif "relaciones corporativas" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de Relaciones corporativas")
                                webbrowser.open("https://comunicacion.udemedellin.edu.co/wp-content/uploads/2022/04/plan-de-formacion-corporativas.pdf")
                            elif "comunicación gráfica publicitaria " in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de comunicación gráfica publicitaria")
                                webbrowser.open("https://comunicacion.udemedellin.edu.co/wp-content/uploads/2022/04/plan-de-formacion_cgpUdemedellin.pdf")
                            elif "lenguajes audiovisuales" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de comunicación lenguajes audiovisuales")
                                webbrowser.open("https://comunicacion.udemedellin.edu.co/wp-content/uploads/2022/04/plan-de-formacion-audiovisuales.pdf")
                            elif "entretenimiento digital" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de comunicación entretenimiento digital")
                                webbrowser.open("https://comunicacion.udemedellin.edu.co/wp-content/uploads/2022/04/plan-de-formacion-entretenimiento.pdf")
                            elif "ingeniería ambiental" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingenieria ambiental")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_ambiental.pdf")  
                            elif "ingeniería civil" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería civil")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_civil.pdf") 
                            elif "ingeniería de sistemas" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería de sistemas")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_sistemas.pdf")
                            elif "ingeniería financiera" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería financiera")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_financiera.pdf")
                            elif "ingeniería en telecomunicaciones" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería en telecomunicaciones")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_telecomunicaciones.pdf")  
                            elif "ingeniería en energía" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería en energia")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_en_energia.pdf")  
                            elif "ingeniería industrial" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería industrial")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_industrial.pdf")                             
                            elif "ingeniería electrónica" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería electónica")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_electronica.pdf")
                            elif "ingeniería electrónica" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ingeniería electónica")
                                webbrowser.open("https://ingenierias.udemedellin.edu.co/wp-content/uploads/2022/04/ingenieria_electronica.pdf")
                            elif "administración de empresas" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de administración de empresas")
                                webbrowser.open("https://fcea.udemedellin.edu.co/wp-content/uploads/2022/04/administracion_de_empresas.pdf")
                            elif "negocios internacionales" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de negocios internacionales")
                                webbrowser.open("https://fcea.udemedellin.edu.co/wp-content/uploads/2022/04/negocios_internacionales.pdf") 
                            elif "contaduría pública" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de contaduría pública")
                                webbrowser.open("https://fcea.udemedellin.edu.co/wp-content/uploads/2022/04/contaduria_publica.pdf") 
                            elif "economía" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de economía")
                                webbrowser.open("https://fcea.udemedellin.edu.co/wp-content/uploads/2022/04/economia.pdf")
                            elif "mercadeo" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de mercadeo")
                                webbrowser.open("https://fcea.udemedellin.edu.co/wp-content/uploads/2022/04/mercadeo.pdf")
                            elif "psicología" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de psicología")
                                webbrowser.open("https://cienciassocialesyhumanas.udemedellin.edu.co/wp-content/uploads/2022/09/psicologia.pdf") 
                            elif "ciencias políticas" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de ciencias políticas")
                                webbrowser.open("https://cienciassocialesyhumanas.udemedellin.edu.co/wp-content/uploads/2022/09/plan-de-formacionciencia_politica-2022.pdf")
                            elif "computación científica" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de computación científica")
                                webbrowser.open("https://cienciasbasicas.udemedellin.edu.co/wp-content/uploads/2022/09/computacion_cientifica.pdf")
                            elif "diseno y gestión de espacios" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de diseno y gestión de espacios")
                                webbrowser.open("https://diseno.udemedellin.edu.co/wp-content/uploads/2022/04/diseno_espacios.pdf")
                            elif "gestión moda y textíl" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de diseno y gestión moda y textíl")
                                webbrowser.open("https://diseno.udemedellin.edu.co/wp-content/uploads/2022/04/diseno_moda.pdf")
                            elif "gestión del producto" in rec:
                                talk("A continuación te enviaré a la pagina donde podrás encontrar el pensum de diseno y gestión del producto")
                                webbrowser.open("https://diseno.udemedellin.edu.co/wp-content/uploads/2022/04/diseno_producto.pdf")

                except:
                    pass
                return flag



    elif "terminar" in rec:
        talk("Gracias por usar este servicio, vuelve pronto")
        flag = False
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag      
while flag:
    flag = listen()