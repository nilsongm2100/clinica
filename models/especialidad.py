# -*- coding: utf-8 -*-
import time
from openerp.osv import fields, osv

class especialidad(osv.osv):
    _name='clinicas.especialidad'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Nombre de la especialidad'),
       
        'doctor_ids':fields.many2one('clinicas.doctor', 'Doctores'),
        
    }
   
