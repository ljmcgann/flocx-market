# put import statements for all objects in the objects directory in
# register_all Called as a hook in common/services.py


def register_all():

    __import__('flocx_market.objects.bid')
    __import__('flocx_market.objects.offer')
    __import__('flocx_market.objects.contract')
