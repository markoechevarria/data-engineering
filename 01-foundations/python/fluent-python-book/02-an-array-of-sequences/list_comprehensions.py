symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print( codes )

## with list comprenhensions
beyond_ascii = [ ord(s) for s in symbols if ord(s) > 127 ]

# with map and filter functions
beyond_ascii = list( filter( lambda c : c > 127, map( ord, symbols) ) )

# cartesion product with list comprenhension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
thirts = [(color, size) for color in colors for size in sizes]
