class Process:
    def __init__(self, id: int, time: int, pred: list[int]):
        self.id = id
        self.time = time
        self.pred = None if 0 in pred else pred
        self.start_time = None
        self.end_time = None

    def get_start_time(self):
        if self.start_time is None:
            self.start_time = max(processes[i].get_end_time() for i in self.pred) if self.pred else 0
        return self.start_time

    def get_end_time(self):
        if self.end_time is None:
            self.end_time = self.get_start_time() + self.time
        return self.end_time


def parse_csv(fn: int):
    res = []
    with open(f'files22/{fn}.csv') as f:
        for line in f.readlines()[1:]:
            line = [x.replace('"', '') for x in line.split(';') if x and x != '\n']
            line = list(map(int, line))
            if line:
                res.append(line)
    return res


processes: dict[int, Process] = {}

if __name__ == '__main__':
    data = parse_csv(7)
    for d in data:
        i, t, *p = d
        processes[i] = Process(i, t, p)

    for v in processes.values():
        v.get_end_time()

    m = max(v.end_time for v in processes.values())

    for v in processes.values():
        print(('.' * v.start_time + '#' * (v.end_time - v.start_time)).ljust(m, '.'))
