from django import forms
from .models import Daviplata, Vinculacion
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError

class DaviplataForm(forms.ModelForm):
    
    class Meta:
        model = Daviplata
        fields = (
            '__all__'
        )
        exclude = ('user', 'departamento', 
                   'departamento', 
                   'municipio', 'red', 'codigo_dian', 
                   'codigo_total', 'direccion_base', 'exclude')

        widgets = {

            'url_img_f': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 'capture':'camera',
                }
            ),
            'url_img_m': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 'capture':'camera',
                }
            ),
            'url_img_o': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 'capture':'camera',
                }
            ),

            'obervacion': Textarea(attrs={'cols': 80, 'rows': 4}),
               
            
            'fecha_capacitacion': forms.DateInput(
            format=(
                '%m/%d/%Y'
                ), 
            attrs={
                'class':'form-control', 
                'placeholder':'Select a date', 
                'type':'date'
                }
            ),

            'fecha_encuesta': forms.DateInput(
            format=(
                '%m/%d/%Y'
                ), 
            attrs={
                'class':'form-control', 
                'placeholder':'Select a date', 
                'type':'date'
                }   
            ),

            'nombre_establecimiento': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'readonly':'readonly'
                }
            ),
            'direccion_c_b': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'readonly':'readonly'
                }
            ),
            'visualizar': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'readonly':'readonly'
                }
            ),
            'visita_efectiva': forms.Select(
                attrs = {
                    'required': 'required', 
                }
            ),
            'material': forms.Select(
                attrs={
                    "required": True
                }
            )
            
            
    }
    def clean(self):
        cleaned_data = super().clean()
        visita_efectiva = cleaned_data.get('visita_efectiva')
        imagen_matrerial = cleaned_data.get('url_img_m')
        tipo_no_efectiva = cleaned_data.get('tipo_no_efectiva')
        ################# claves ###########################
        
        es_dueño = cleaned_data.get('es_dueño')
        establecimiento_cambio = cleaned_data.get('establecimiento_cambio')
        tipo_establecimiento = cleaned_data.get('tipo_establecimiento')
        ############### HERRAMIENTAS #####################
        impresora = cleaned_data.get('impresora')
        datafono = cleaned_data.get('datafono')
        lector = cleaned_data.get('lector')
        computador = cleaned_data.get('computador')
        ################ SERVICIOS ################
        pago_propios = cleaned_data.get('pago_propios')
        deposito_retiro_propio = cleaned_data.get('deposito_retiro_propio')
        servicio_pagos = cleaned_data.get('servicio_pagos')
        servicio_recaudo = cleaned_data.get('servicio_recaudo')
        servicio_depositos = cleaned_data.get('servicio_depositos')
        transacciones = cleaned_data.get('transacciones')
        deposito_retiro = cleaned_data.get('deposito_retiro')
        pago_subsidios = cleaned_data.get('pago_subsidios')
        tip_seguridad = cleaned_data.get('tip_seguridad')
        Sarlaft_activos = cleaned_data.get('Sarlaft_activos')
        recaudo_servicios = cleaned_data.get('recaudo_servicios')
        tip_riesgo = cleaned_data.get('tip_riesgo')
        acude = cleaned_data.get('acude')
        medio = cleaned_data.get('medio')
        sarlaft_informa = cleaned_data.get('sarlaft_informa')
        otro_especificado = cleaned_data.get('otro_especificado')
        
        ####################################################
        if visita_efectiva == "NO" and tipo_no_efectiva == None:
            raise forms.ValidationError( "Favor tipificar porque no fue efectiva")
        
        if tipo_no_efectiva == "Otros" and otro_especificado:
            raise forms.ValidationError( "Favor tipificar porque no fue efectiva")
        ################## claves ##########################
        
        elif visita_efectiva == "SI" and es_dueño == None:
            raise forms.ValidationError( "Favor responder SI ES DUEÑO? ")
        
        elif visita_efectiva == "SI" and establecimiento_cambio == None:
            raise forms.ValidationError( "Favor responder SI EL ESTABLECIMIENTO CAMBIÓ DE DUEÑO EN EL ULTIMO AÑO? ")
        
        elif visita_efectiva == "SI" and tipo_establecimiento == None:
            raise forms.ValidationError( "Favor responder TIPO DE ESTABLECIMIENTO? ")
        
        
        ############################HERRAMIENTAS#################################
        if visita_efectiva == "SI" and impresora == None:
            raise forms.ValidationError( "Favor responder si tiene impresora")
        
        elif visita_efectiva == "SI" and datafono == None:
            raise forms.ValidationError( "Favor responder si tiene datafono")
        
        elif visita_efectiva == "SI" and lector == None:
            raise forms.ValidationError( "Favor responder si tiene lector")
        
        elif visita_efectiva == "SI" and computador == None:
            raise forms.ValidationError( "Favor responder si tiene lector")
        
        ######################  SERVIVCIOS ###############################
        if visita_efectiva == "SI" and pago_propios == None:
            raise forms.ValidationError( "Favor responder PAGO DE PRODUCTOS PROPIOS?")
        
        elif visita_efectiva == "SI" and deposito_retiro_propio == None:
            raise forms.ValidationError( "Favor responder DEPÓSITO DE RETIRO DAVIPLATA?")
        
        elif visita_efectiva == "SI" and servicio_pagos == None:
            raise forms.ValidationError( "Favor responder PAGOS DE SUBSIDIOS POR GIROS?")
        
        elif visita_efectiva == "SI" and servicio_recaudo == None:
            raise forms.ValidationError( "Favor responder RECAUDO SERVICIOS PÚBLICOS Y PRIVADOS?")
        
        elif visita_efectiva == "SI" and servicio_depositos == None:
            raise forms.ValidationError( "Favor responder DEPÓSITOS Y RETIROS DE CUENTAS AHORRO Y CORRIENTE?")
        
        elif visita_efectiva == "SI" and transacciones == None:
            raise forms.ValidationError( "Favor responder CONOCIMIENTO PARA REALIZAR TRANSACCIONES?")
        
        elif visita_efectiva == "SI" and deposito_retiro == None:
            raise forms.ValidationError( "Favor responder DEPÓSITO Y RETIROS DAVIVIENDA?")
        
        elif visita_efectiva == "SI" and pago_subsidios == None:
            raise forms.ValidationError( "Favor responder PAGOS DE SUBSIDIOS POR GIRO?")
        
        elif visita_efectiva == "SI" and tip_seguridad == None:
            raise forms.ValidationError( "Favor responder TIPS DE SEGURIDAD?")
        
        elif visita_efectiva == "SI" and Sarlaft_activos == None:
            raise forms.ValidationError( "Favor responder SARLAFT/LAVADO DE ACTIVOS?")
        
        elif visita_efectiva == "SI" and recaudo_servicios == None:
            raise forms.ValidationError( "Favor responder RECAUDO SERVICIOS PÚBLICOS Y PRIVADOS?")
        
        elif visita_efectiva == "SI" and tip_riesgo == None:
            raise forms.ValidationError( "Favor responder TIPS DE RIESGO?")
        
        elif visita_efectiva == "SI" and acude == None:
            raise forms.ValidationError( "Favor responder ¿A QUIEN ACUDE?")
        
        elif visita_efectiva == "SI" and medio == None:
            raise forms.ValidationError( "Favor responder ¿MEDIO?")
        
        elif visita_efectiva == "SI" and sarlaft_informa == None:
            raise forms.ValidationError( "Favor responder SARLAFT ¿A QUIEN INFORMARÍA?")
        ##################IMAGENES#######################
        if visita_efectiva == "SI" and imagen_matrerial == None:
            raise forms.ValidationError( "Favor tomar imagen de fachada")
    
        
        ###################################
   

class VinculacionForm(forms.ModelForm):
   
    class Meta:
        model = Vinculacion
        fields = (
        '__all__'   )

        required =('tipo_gestion', 'registro_daviplata')
           
        widgets = {
            'celular': forms.NumberInput(
                
            ),
            'identificacion': forms.NumberInput(
            ),
            'celular_confirma': forms.NumberInput(
                attrs={
                    'onchange':'get_sector_code'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    "required": True
                 }
            ),
            
            }

    
    def clean(self):
        cleaned_data = super().clean()
        celular = cleaned_data.get('celular')
        celular_confirma  = cleaned_data.get('celular_confirma')
        #############Tipo gestion#######################
        tipo_gestion  = cleaned_data.get('tipo_gestion')
        nombre  = cleaned_data.get('nombre')
        nombre_comercio = cleaned_data.get('nombre_comercio')
        categoria = cleaned_data.get('categoria')
        direccion = cleaned_data.get('direccion')
        codigo_transaccion = cleaned_data.get('codigo_transaccion')
        no_transaccion = cleaned_data.get('no_transaccion')
        se_registro = cleaned_data.get('se_registro')
        no_register = cleaned_data.get('no_register')
        registro_daviplata = cleaned_data.get('registro_daviplata')
        motivo_no_registro = cleaned_data.get('motivo_no_registro')
        solicito_tencard = cleaned_data.get('solicito_tencard')
        porque_no_solicito = cleaned_data.get('porque_no_solicito')
        sticker = cleaned_data.get('sticker')
        razon_no_sticker = cleaned_data.get('razon_no_sticker')

        ########################################
        if sticker == "NO" and razon_no_sticker == None:
            raise forms.ValidationError( "Completar Razón por la cual no se pegó el sticker" )
        #################################
        if solicito_tencard == "NO" and porque_no_solicito == None:
            raise forms.ValidationError( "Completar ¿Por qué no se solicitó la tentcard?" )
        ##################

        if registro_daviplata == "NO" and motivo_no_registro == None:
            raise forms.ValidationError( "Completar Por qué no se realizó el registro DaviPlata." )

        if celular != celular_confirma:
            raise forms.ValidationError( "Celular incorrecto." )
        

        ###########################################################
        
        if tipo_gestion.id ==1 and nombre == None:
            raise forms.ValidationError( "Completar Nombre del cliente DaviPlata" )
        
        elif tipo_gestion.id ==1 and celular == None:
            raise forms.ValidationError( "Completar No. celular activado en DaviPlata" )
        
        elif tipo_gestion.id ==1 and nombre_comercio == None:
            raise forms.ValidationError( "Completar Nombre comercio" )
        
        elif tipo_gestion.id ==1 and categoria == None:
            raise forms.ValidationError( "Completar ¿A cuál de las siguientes categorías pertenece el comercio?" )
        
        ###################################NUEVO#########################################
        
        if tipo_gestion.id ==2 and nombre == None:
            raise forms.ValidationError( "Completar Nombre del cliente DaviPlata" )
        
        elif tipo_gestion.id ==2 and celular == None:
            raise forms.ValidationError( "Completar No. celular activado en DaviPlata" )
        
        elif tipo_gestion.id ==2 and nombre_comercio == None:
            raise forms.ValidationError( "Completar Nombre comercio" )
        
        elif tipo_gestion.id ==2 and categoria == None:
            raise forms.ValidationError( "Completar ¿A cuál de las siguientes categorías pertenece el comercio?" )
        
        ########################REMARCACION##########################
        if tipo_gestion.id ==3 and nombre == None:
            raise forms.ValidationError( "Completar Nombre del cliente DaviPlata" )
        
        elif tipo_gestion.id ==3 and celular == None:
            raise forms.ValidationError( "Completar No. celular activado en DaviPlata" )
        
        elif tipo_gestion.id ==3 and nombre_comercio == None:
            raise forms.ValidationError( "Completar Nombre comercio" )
        
        elif tipo_gestion.id ==3 and categoria == None:
            raise forms.ValidationError( "Completar ¿A cuál de las siguientes categorías pertenece el comercio?" )
        
        ########## DIRECCION  ###########################

        if direccion == None:
            raise forms.ValidationError( "Completar Dirección Comercio" )
        
        ############## Codigo transaccion #######################

        if codigo_transaccion == None and no_transaccion == None:
            raise forms.ValidationError( "Completar ¿Por qué no se realizó la transacción de $1?" )
        
        if se_registro == "NO" and no_register == None:
            raise forms.ValidationError( "Completar ¿Por que no se realizo el registro en perfil mi negocio?" )
        
        return self.cleaned_data
    

   
        
    


        
    
        

        
        
    
        
        
        
    

    
    
    
    
        
        
    
        
    