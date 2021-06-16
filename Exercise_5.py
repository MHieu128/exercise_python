class Restangle:
    def __init__(obj, width, height):
        obj.width = width
        obj.height = height
    
    def Perimeter(obj):
        return obj.width * obj.height

    def Area(obj):
        return (obj.width + obj.height) * 2

r1 = Restangle(4,5)
print (f'this is premeter: {r1.Perimeter()}')
print (f'this is area: {r1.Area()}')