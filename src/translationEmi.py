
#Donne les coordonnées du point translaté, peut être utilisé comme une fonction annexe
#Dans le cas pratique on aura juste le vecteur de translation et on adaptera
def translation (x_ini,y_ini,x_translation,y_translation):

    x_translation= x_ini+x_translation
    y_translation=y_ini+y_translation

    return (x_translation,y_translation)