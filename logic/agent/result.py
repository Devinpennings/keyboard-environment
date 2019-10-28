class Result:

    def __init__(self, result, state, status):
        self.result = result
        self.state = state
        self.status = status

    def __str__(self):
        return f'result: {self.result}\nstate: {self.state}\nstatus: {self.status}'
