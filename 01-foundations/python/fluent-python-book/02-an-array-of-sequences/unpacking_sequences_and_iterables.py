lax_coordinates = (33, -118)
latitude, longitude = lax_coordinates

divmod(20,8)
t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)

import os
path, filename = os.path.split('/home/marko/.ssh/id_rsa.pub')
print( path )
print( filename )

a, b, *rest = range(5)
*head, a, b = range(10)

tupla = (*range(4), 4)
lista = [*range(4), 4]
dicti = {*range(4), 4}
print(tupla)
print(lista)
print(dicti)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for name, _, _, (lat, lon) in metro_areas:
    print(f'{name} | {lat} | {lon}')

def handle_command(self, message):
    match message:
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
        case ['LED', ident,  red, green, blue]:
            self.leds[ident].set_color(red, green, blue)
        case _:
            raise InvalidCommand(message)

for record in metro_areas:
    match record:
        case [name, _, _, (lat,lon)] if lon <= 0:
            print(f'{name} | {lat} | {lon}')


def evaluate(exp: Expression, env: Environment) -> Any:
    "Evaluate an expression in an environment"
    match exp:
        case ['quote', x]:
            return x
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        case ['define', Symbol() as name, value_exp]:
            env[name] = evaluate(value_exp, env)
        case _:
            raise SyntaxError(listpstr(exp))


