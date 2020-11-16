from enum import Enum


class Kind(Enum):
    STATIC = 0
    FIELD = 1
    ARG = 2
    VAR = 3


class SymbolTable:

    def __init__(self):
        self.class_table = {Kind.FIELD: {}, Kind.STATIC: {}}
        self.local_table = {Kind.ARG: {}, Kind.VAR: {}}

    def start_subroutine(self):
        self.local_table = {Kind.ARG: {}, Kind.VAR: {}}

    def define(self, name, var_type, kind):
        if kind in (Kind.STATIC, Kind.FIELD):
            self.class_table[kind][name] = (var_type, len(self.class_table[kind]))
        elif kind in (Kind.ARG, Kind.VAR):
            self.local_table[kind][name] = (var_type, len(self.local_table[kind]))
        else:
            raise ValueError("{} is not a support kind of var!".format(kind))

    def get_var_count(self, kind):
        if kind in (Kind.STATIC, Kind.FIELD):
            return len(self.class_table[kind])
        elif kind in (Kind.ARG, Kind.VAR):
            return len(self.local_table[kind])
        else:
            raise ValueError("{} is not a support kind of var!".format(kind))

    def get_var_kind(self, name):
        if name in self.class_table[Kind.FIELD]:
            return Kind.FIELD
        elif name in self.class_table[Kind.STATIC]:
            return Kind.STATIC
        elif name in self.local_table[Kind.ARG]:
            return Kind.ARG
        elif name in self.local_table[Kind.VAR]:
            return Kind.VAR
        else:
            return None

    def get_vm_seg(self, name):
        if name in self.class_table[Kind.FIELD]:
            return 'this'
        elif name in self.class_table[Kind.STATIC]:
            return 'static'
        if name in self.local_table[Kind.ARG]:
            return 'argument'
        elif name in self.local_table[Kind.VAR]:
            return 'local'
        else:
            return None

    def get_var_type(self, name):
        if name in self.class_table[Kind.FIELD]:
            return self.class_table[Kind.FIELD][name][0]
        elif name in self.class_table[Kind.STATIC]:
            return self.class_table[Kind.STATIC][name][0]
        elif name in self.local_table[Kind.ARG]:
            return self.local_table[Kind.ARG][name][0]
        elif name in self.local_table[Kind.VAR]:
            return self.local_table[Kind.VAR][name][0]
        else:
            return None

    def get_var_index(self, name):
        if name in self.class_table[Kind.FIELD]:
            return self.class_table[Kind.FIELD][name][1]
        elif name in self.class_table[Kind.STATIC]:
            return self.class_table[Kind.STATIC][name][1]
        elif name in self.local_table[Kind.ARG]:
            return self.local_table[Kind.ARG][name][1]
        elif name in self.local_table[Kind.VAR]:
            return self.local_table[Kind.VAR][name][1]
        else:
            return None

    def get_var(self, name):
        if name in self.class_table[Kind.FIELD]:
            return self.class_table[Kind.FIELD][name]
        elif name in self.class_table[Kind.STATIC]:
            return self.class_table[Kind.STATIC][name]
        elif name in self.local_table[Kind.ARG]:
            return self.local_table[Kind.ARG][name]
        elif name in self.local_table[Kind.VAR]:
            return self.local_table[Kind.VAR][name]
        else:
            return None
