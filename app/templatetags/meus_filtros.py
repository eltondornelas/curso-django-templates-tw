from django import template

register = template.Library()
# custom-template-tags -> djando docs


# name= é o nome do filtro a ser utilizado no template
@register.filter(name='remover_letra')
def remover_letra(var, letra):
    return var.replace(letra, '')
