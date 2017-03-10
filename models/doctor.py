# -*- coding: utf-8 -*-
import time
from openerp.osv import fields, osv

class doctor(osv.osv):
    _name='clinicas.doctor'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Nombre completo del doctor'),
        'cedula':fields.integer('Cedula',help='Cedula de Identidad'),
        'especialidad_ids':fields.many2one('clinicas.especialidad', 'Especialidades'),
        'genero':fields.selection([('F','Femenino'),('M','Masculino')],'Genero', required=True, help='Genero del doctor'),
        
    }
