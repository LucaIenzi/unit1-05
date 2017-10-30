# Created by: luca.ienzi
# Created on: oct 2017
# Created for: ICS3U
#  This program shows thr price for how big you want your pizza to be

import ui

def calculate_button_Touch_upinside(sender):
    PI = 3.14
    labour_cost = 0.75
    rent_cost = 1.00
    material_cost = 0.50
    hst = 1.13
    
    diameter = float(view['diameter_textbox'].text)
    sub_total = labour_cost + rent_cost + (material_cost * diameter)
    cost = sub_total  *(hst)
    view['answer_lable'].text = 'the cost is:' + '${:,.2f}'.format(cost)
view = ui.load_view()
view.present('sheet')
