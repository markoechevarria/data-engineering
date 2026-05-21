from collections import Counter, defaultdict

class LogAnalyzer:

    def __init__(self, data):
        self.data = data

    def consolidate(self):

        request_per_ip = Counter()
        status_code = Counter()
        endpoint_counter = Counter()
        unique_endpoints = defaultdict(set)
        inverted_mapping = defaultdict(set)

        for ( ip, route, sc) in self.data:
            request_per_ip[ip] += 1
            status_code.update([sc])
            unique_endpoints[ip].add(route)
            inverted_mapping[route].add(ip)
            endpoint_counter.update([route])

        return { 
            "request_per_ip": dict(request_per_ip),
            "unique_endpoints": dict(unique_endpoints),
            "status_code": dict(status_code),
            "three_most_visited_endpoints": dict(endpoint_counter.most_common(3)),
            "inverted_mapping": dict(inverted_mapping)
        }

if __name__ == "__main__":

    logs = [
        ("192.168.1.10", "/home", 200),
        ("192.168.1.11", "/about", 200),
        ("192.168.1.10", "/home", 200),
        ("192.168.1.12", "/login", 403),
        ("192.168.1.11", "/home", 200),
        ("192.168.1.10", "/settings", 404),
    ]

    logAnalizer = LogAnalyzer(logs)
    a = logAnalizer.consolidate()
    print(a)
