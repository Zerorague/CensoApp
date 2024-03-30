import psycopg2 as ps

class Conexion():
    def __init__(self,dbname="dfld1s3b7nf5j6",user="ufp6rdc8691itb",host="cbbirn8v9855bl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com",password="p8321329702672939dd561997c0937c3d289e8f5febfbb3c6b67d307882d377c9"):
        self.__dbname=dbname
        self.__user=user
        self.__host=host
        self.__password=password

    def conectar(self) :
        try:
            self.con= ps.connect(dbname=self.__dbname,user=self.__user,host=self.__host,password=self.__password,port=5432)
            print("conectada")
        except:
            print(f"error al intentar conectar a la base de datos {self.__dbname}")

    # --------------------Bitacora-----------------------------
    def insertarDatosBitacora(self, local:str, grupo:int, id_user:int, llave:str, area:str, direccion:str,
                              moradorAusente=0, rechazo=0, informanteimpedido=0, informanteNoEspanol=0, otraRazonNoEntrevista=0,
                              viviendaDesocupada=0, viviendaColectiva=0,
                              otroUsoSinVivienda=0, dificilAcceso=0, sinEdificacion=0, direccionInexistente=0,
                              cuestionarioCompleto=0, cuestionarioParcial=0, cuestionarioNoIniciado=0,
                              vinculacion=None, coordenada=None, descripcion=None):
        cursor=self.con.cursor()
        cursor.execute(f"""INSERT INTO BITACORA (local,grupo,id_user,llave,area_geografica,
        direccion,morador_ausente,rechazo,informante_impedido,informante_no_habla_espanol,
        otra_razon_de_no_entrevista,vivienda_desocupada,vivienda_colectiva,otro_uso_sin_vivienda,
        dificil_acceso,sitio_sin_edificacion,direccion_inexistente,cuestionario_completo,cuestionario_parcial,
        cuestionario_no_iniciado,vinculacion_censo,coordenada,descripcion) 
        values ('{local}',{grupo},{id_user},'{llave}','{area}','{direccion}',{moradorAusente},{rechazo},{informanteimpedido},
        {informanteNoEspanol},{otraRazonNoEntrevista},{viviendaDesocupada},{viviendaColectiva},{otroUsoSinVivienda},{dificilAcceso},{sinEdificacion},
        {direccionInexistente},{cuestionarioCompleto},{cuestionarioParcial},{cuestionarioNoIniciado},
        '{vinculacion}','{coordenada}','{descripcion}')""")

        self.con.commit()
        self.con.close()
#--------------------Usuarios-----------------------------
    def traerUsuarios(self):
        self.conectar()
        cursor= self.con.cursor()
        cursor.execute("select id,user_name from users")
        usuarios=cursor.fetchall()
        self.con.close()
        return usuarios

#--------------------Contraseña-----------------------------

    def traerContrasena(self,usuario):
        self.conectar()
        cursor= self.con.cursor()
        cursor.execute(f"select password from users where user_name = '{usuario}'")
        contrasena=cursor.fetchone()
        self.con.close()
        return contrasena


