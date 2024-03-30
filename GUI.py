import flet as ft

import BD

def LoginGui(page:ft.Page):
    def on_column_scroll(e: ft.OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )

    def btn_sumarMoradores_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,moradorAusente=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarRechazo_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,rechazo=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarImpedido_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,informanteimpedido=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarNoEspanol_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,informanteNoEspanol=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarOtraRazonNoEntrevista_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,otraRazonNoEntrevista=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarViviendaDesocupada_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,viviendaDesocupada=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarViviendaColectiva_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,viviendaColectiva=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarOtroUsoSinVivienda_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,otroUsoSinVivienda=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarDireccionConProblemas_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,dificilAcceso=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarSitioSinEdificacion_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,sinEdificacion=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarDireccionInexistente_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,direccionInexistente=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarCuestionarioCompleto_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,cuestionarioCompleto=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarCuestionarioParcial_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,cuestionarioParcial=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()

    def btn_sumarCuestionarioNoIniciado_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        conexion.insertarDatosBitacora(id_user=btn_entrar_on_click(e)[0] ,cuestionarioNoIniciado=1,local="Linares4",area=txt_area.current.value,llave=txt_llave.current.value,grupo=5,descripcion=txt_Descripcion.current.value.capitalize(),direccion=txt_direccion.current.value.capitalize(),vinculacion=txt_censoEnLinea.current.value.lower())
        conexion.con.close()



    def btn_entrar_on_click(e):
        conexion = BD.Conexion()
        conexion.conectar()
        for user in conexion.traerUsuarios():
            if (user[1].lower() == txt_usuario.current.value.lower()) and (conexion.traerContrasena(user[1])[0] == txt_contrasena.current.value) :
                conexion.con.close()
                page.update()
                page.go(route="/bitacora")
                return  (user[0],user[1])


            else:

                conexion.con.close()

    txt_usuario = ft.Ref[ft.TextField]()
    txt_contrasena = ft.Ref[ft.TextField]()
    txt_area = ft.Ref[ft.TextField]()
    btn_entrar = ft.Ref[ft.TextButton]()
    check_recordar = ft.Ref[ft.Checkbox]()

    txt_llave = ft.Ref[ft.TextField]()
    txt_direccion = ft.Ref[ft.TextField]()

    txt_censoEnLinea = ft.Ref[ft.TextField]()
    txt_Descripcion = ft.Ref[ft.TextField]()

    btn_sumarMoradoresAusentes = ft.Ref[ft.ElevatedButton]()
    btn_sumarRechazo = ft.Ref[ft.ElevatedButton]()

    btn_Sumarimpedido = ft.Ref[ft.ElevatedButton]()
    btn_SumarnoEspanol = ft.Ref[ft.ElevatedButton]()

    btn_SumarotraRazon = ft.Ref[ft.ElevatedButton]()
    btn_SumarviviendaDesocupada = ft.Ref[ft.ElevatedButton]()

    btn_Sumarcolectiva = ft.Ref[ft.ElevatedButton]()
    btn_SumarotroUsoSinVivienda = ft.Ref[ft.ElevatedButton]()

    btn_SumarProblemasAcceso = ft.Ref[ft.ElevatedButton]()
    btn_SumarSitioSinEdificacion = ft.Ref[ft.ElevatedButton]()

    btn_SumarDireccionInexistente = ft.Ref[ft.ElevatedButton]()
    btn_SumarCuestionarioCompleto = ft.Ref[ft.ElevatedButton]()

    btn_SumarCuestionarioParcial = ft.Ref[ft.ElevatedButton]()
    btn_SumarCuestionarioNoIniciado = ft.Ref[ft.ElevatedButton]()

    page.title = "Bitacora App "
    page.padding=0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="#fcf8f5"
    page.window_center()

    page.add(
        ft.Container(padding=10,content=ft.Column(
            horizontal_alignment="center",
            width=500,
            spacing=10,
            controls=[
                ft.TextField(ref=txt_usuario,bgcolor="white",content_padding=20,border_radius=100,hint_text="usuario",max_length=15),
                ft.TextField(ref=txt_contrasena, bgcolor="white", content_padding=20, border_radius=100,hint_text="contraseña",max_length=15,password=True),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.TextButton(ref=btn_entrar,text="Entrar",height=50,width=200,on_click=btn_entrar_on_click),
                            ft.Checkbox(ref=check_recordar,label="recordar")]),padding=10)
            ],))
    )



    bitacoraGui= ft.View(
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll=on_column_scroll,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        route="/bitacora",
        controls=[
            ft.Container(
                width=500,
                content=ft.Column(
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.TextField(ref=txt_area, label="area geografica", width=300,max_length=20),
                        ft.TextField(ref=txt_llave,label="Llave entrevista",width=300,max_length=15),
                        ft.TextField(ref=txt_direccion, label="Direccion",width=300,max_length=100),
                        ft.TextField(ref=txt_censoEnLinea, label="Censo en linea", width=300, max_length=30),
                        ft.TextField(ref=txt_Descripcion, label="Descripcion", width=300, max_length=255),
                        ft.ElevatedButton(ref=btn_sumarMoradoresAusentes, text="Morador Ausente", width=300,height=50,on_click=btn_sumarMoradores_on_click),
                        ft.ElevatedButton(ref=btn_sumarRechazo, text="Rechazo", width=300,height=50,on_click=btn_sumarRechazo_on_click),
                        ft.ElevatedButton(ref=btn_Sumarimpedido, text="Informante impedido", width=300,height=50,on_click=btn_sumarImpedido_on_click),
                        ft.ElevatedButton(ref=btn_SumarnoEspanol, text="No habla español", width=300,height=50,on_click=btn_sumarNoEspanol_on_click),
                        ft.ElevatedButton(ref=btn_SumarotraRazon, text="Otra razon no entrevista", width=300, height=50,on_click=btn_sumarOtraRazonNoEntrevista_on_click),
                        ft.ElevatedButton(ref=btn_SumarviviendaDesocupada, text="Vivienda desocupada", width=300, height=50,on_click=btn_sumarViviendaDesocupada_on_click),
                        ft.ElevatedButton(ref=btn_Sumarcolectiva, text="Vivienda Colectiva", width=300, height=50,on_click=btn_sumarViviendaColectiva_on_click),
                        ft.ElevatedButton(ref=btn_SumarotroUsoSinVivienda, text="Otro uso sin vivienda", width=300, height=50,on_click=btn_sumarOtroUsoSinVivienda_on_click),
                        ft.ElevatedButton(ref=btn_SumarProblemasAcceso, text="Problemas acceso", width=300, height=50,on_click=btn_sumarDireccionConProblemas_on_click),
                        ft.ElevatedButton(ref=btn_SumarSitioSinEdificacion, text="Sitio sin edificacion", width=300,height=50,on_click=btn_sumarSitioSinEdificacion_on_click),
                        ft.ElevatedButton(ref=btn_SumarDireccionInexistente, text="Direccion inexistente", width=300, height=50,on_click=btn_sumarDireccionInexistente_on_click),
                        ft.ElevatedButton(ref=btn_SumarCuestionarioCompleto, text="Cuestionario completo", width=300,height=50,on_click=btn_sumarCuestionarioCompleto_on_click),
                        ft.ElevatedButton(ref=btn_SumarCuestionarioParcial, text="Cuestionario Parcial", width=300,height=50,on_click=btn_sumarCuestionarioParcial_on_click),
                        ft.ElevatedButton(ref=btn_SumarCuestionarioNoIniciado, text="Cuestionario no iniciado", width=300,height=50,on_click=btn_sumarCuestionarioNoIniciado_on_click),





                    ]
                )

            ),

        ]
    )




    page.update()

    page.views.append(bitacoraGui)
ft.app(target=LoginGui,view=ft.WEB_BROWSER)


