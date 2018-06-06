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


# 自定义过滤器
def ass(value1):
    return value1 + "world"


register.filter("ass", ass)
