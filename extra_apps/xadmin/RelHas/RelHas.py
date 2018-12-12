# _*_ coding:utf-8 _*_ 
__author__ = 'levi'
__date__ = '2018/12/8 20:44'

class RelHas():
    def getRel(field):
        rel = None
        if hasattr(field, 'rel'):
            rel = field.rel if field.rel else None
            return rel
    def getRelto(field):
        rel_to = None
        if hasattr(field, 'rel'):
            rel_to = field.rel.to if field.rel else None
            return rel_to