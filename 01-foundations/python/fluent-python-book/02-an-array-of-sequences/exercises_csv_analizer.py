from pathlib import Path
from collections import defaultdict

class CSVAnalizer:

    def __init__(self, path):

        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Could not find path {path}")

        self.rows = []

        with open(path, 'r', encoding='utf-8') as f:

            for line in f:
                parts = [part.strip() for part in line.split(',')]

                if len(parts) != 3:
                    continue

                name, department, salary = parts

                try: 
                    salary = int(salary)
                except ValueError:
                    continue

                self.rows.append((name, department, salary))

    def __str__(self):

        if not self.rows:
            return "No data available"

        rows = "\n".join(
            f"|{i:^4}|{name:^15}|{occupation:^15}|{salary:^6}|"
            for i, (name, occupation, salary) in enumerate(self.rows, start=1)
        )
        border = '-'*45

        return f"{border}\n{rows}\n{border}"

    def department_info(self):

        total = defaultdict(int)

        for row in self.rows:
            _, department, salary = row
            total[department] += salary

        return dict(total)

    def highest_paid_employeer(self):

        if not self.rows:
            return None

        name, _, salary = max(
            self.rows, 
            key= lambda row: row[2]
        )

        return name, salary

    def filtering(self, departmentt):

        return ( row for row in self.rows if row[1] == departmentt)

    def transpose(self):

        return list(zip(*self.rows))

if __name__ == '__main__':
    analizer = CSVAnalizer("job_data.csv")
    print(analizer)
    print(analizer.department_info())
    print(analizer.highest_paid_employeer())
    for row in analizer.filtering("Engineering"):
        print(row)
    print(analizer.transpose())

