from django import template

register = template.Library()
import math


@register.simple_tag
def cal_discount(selling_price, discounted_price):
    if discounted_price is not None:
        dis_price = ( discounted_price / selling_price  ) * 100
        # print(dis_price)
        return math.floor(dis_price)


