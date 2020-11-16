class Writer:

    def __init__(self, file):
        self.out_fp = file.split('.')[0] + '.vm'
        self.out_str = []

    def write_to_file(self):
        with open(self.out_fp, "w") as file:
            for line in self.out_str:
                file.write(line + '\n')
        return

    def write_push(self, mem, idx):
        if mem not in ('constant', 'argument', 'local', 'static', 'this', 'that', 'pointer', 'temp'):
            raise ValueError('Invalid push memory location {}'.format(mem))
        self.out_str.append("push {} {}".format(mem, idx))

    def write_prev_push(self, mem, idx, num):  # for do methods
        if mem not in ('constant', 'argument', 'local', 'static', 'this', 'that', 'pointer', 'temp'):
            raise ValueError('Invalid push memory location {}'.format(mem))
        self.out_str.insert(-num+1, "push {} {}".format(mem, idx))

    def write_pop(self, mem, idx):
        if mem not in ('argument', 'local', 'static', 'this', 'that', 'pointer', 'temp'):
            raise ValueError('Invalid pop memory location {}'.format(mem))
        self.out_str.append("pop {} {}".format(mem, idx))

    def write_math(self, cmd, neg=False):
        if cmd not in ('~', '+', '-', '&', '|', '>', '<', '='):  # (op term)*
            raise ValueError('Invalid math command {}'.format(cmd))
        if cmd == '+':
            self.out_str.append('add')
        elif cmd == '-':
            if neg:
                self.out_str.append('neg')
            else:
                self.out_str.append('sub')
        elif cmd == '&':
            self.out_str.append('and')
        elif cmd == '|':
            self.out_str.append('or')
        elif cmd == '>':
            self.out_str.append('gt')
        elif cmd == '<':
            self.out_str.append('lt')
        elif cmd == '=':
            self.out_str.append('eq')
        elif cmd == '~':
            self.out_str.append('not')

    def write_label(self, label):
        self.out_str.append("label {}".format(label))

    def write_goto(self, label):
        self.out_str.append("goto {}".format(label))

    def write_if(self, label):
        self.out_str.append("if-goto {}".format(label))

    def write_call(self, fcn, nargs):
        self.out_str.append("call {} {}".format(fcn, nargs))

    def write_function(self, name, nlocals):
        # self.out_str.insert(-1*nlocals - 1, "function {}.{} {}".format(self.out_fp.split('/')[-1].split('.')[0], name, nlocals))
        self.out_str.append("function {}.{} {}".format(self.out_fp.split('/')[-1].split('.')[0], name, nlocals))

    def write_return(self):
        self.out_str.append("return")
