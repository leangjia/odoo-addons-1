# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Sistemas de Datos (<http://www.sdatos.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'SDatos User Warehouse',
    'version' : '0.1',
    'author' : 'Sistemas de Datos',
    'maintainer': 'Sistemas de Datos',
    'category' : 'Warehouse Management',
    'summary': 'A Warehouse for user',
    'description' : """
User Warehouse
==============

This module allows define a preferred warehouse for each salesman/user
    """,
    'website': 'http://www.sdatos.com',
    # End General Data
    'depends' : ['base', 
                 'sale', 
                 'stock', 
                 'sale_stock'],        
    'data': ['views/user_view.xml'],  
    'installable': False,        
    'auto_install': False,        
    'application': False,
}