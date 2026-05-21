# tuples used as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# tuples as inmutables lists

def fixed(o):
    try: 
        hash(o)
    except TypeError:
        return False
    return True

a = 10
b = 'alpha'
c = (1,2)
tf = (10, 'alpha', (1,2))
tm = (10, 'alpha', [1,2])


