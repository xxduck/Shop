from django import template


register =  template.Library()


@register.tag
def upper(parser, token):
    nodelist = parser.parse("endupper")
    parser.delete_first_token()
    return UpperNode(nodelist)


class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        content = self.nodelist.render(context)
        return content.upper()