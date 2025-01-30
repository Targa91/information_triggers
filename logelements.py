class TLogElement:
    """Базовый класс для логического элемента."""
    def __init__(self):
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0
        if not hasattr(self, "_calc"):
            raise NotImplementedError("Нельзя создать такой объект!!!")

    def __setIn1(self, newIn1):
        if newIn1 in (0, 1):
            self.__in1 = newIn1
            self._calc()

    def __setIn2(self, newIn2):
        if newIn2 in (0, 1):
            self.__in2 = newIn2
            self._calc()

    In1 = property(lambda self: self._TLogElement__in1, __setIn1)
    In2 = property(lambda self: self._TLogElement__in2, __setIn2)
    Res = property(lambda self: self._res)


class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(not self.In1)


class TAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 * self.In2

class Tor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if self.In1 == self.In2 == 1:
            self._res = 1
        else:
            self._res = self.In1 + self.In2


class T_ecvival(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(self.In1 == self.In2)

class T_xor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if self.In1 == self.In2 == 1:
            self._res = 0
        elif self.In1 == self.In2 == 0:
            self._res = 1
        else:
            self._res = self.In1 * self.In2

class T_xand(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if self.In1 == self.In2 == 1:
            self._res = 0
        elif self.In1 == self.In2 == 0:
            self._res = 1
        else:
            self._res = self.In1 + self.In2

class T_xxor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if self.In1 == self.In2 == 1:
            self._res = 0
        elif self.In1 == self.In2 == 0:
            self._res = 0
        else:
            self._res = self.In1 + self.In2

class T_imp(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        if  self.In1 == self.In2 == 1:
            self._res = 1
        elif  self.In1 == self.In2 == 0:
            self._res = 1
        else:
            self._res = int(not self.In1) * self.In2

class TTrigger(TLogElement):
    def __init__(self,Q):
        TLogElement.__init__(self)
        self.q = Q

    def _calc(self):
        if self.q == 0:
            if  self.In1 == self.In2 == 1:
                self._res = 1
            elif  self.In1 == self.In2 == 0:
                self._res = 0
            else:
                self._res = self.In1 * int(not self.In2)
        if self.q == 1:
            if  self.In1 == self.In2 == 1:
                self._res = 1
            elif  self.In1 == self.In2 == 0:
                self._res = 1
            else:
                self._res = self.In1 * int(not self.In2)


# trigger_and = TAnd()
# for x in 0,1:
#     for y in 0,1:
#         trigger_and.In1 = x
#         trigger_and.In2 = y
#         print(trigger_and.In1,trigger_and.In2,trigger_and._res)
# print('----------------------------------------------------')
# trigger_or = Tor()
# for x in 0,1:
#     for y in 0,1:
#         trigger_or.In1 = x
#         trigger_or.In2 = y
#         print(trigger_or.In1,trigger_or.In2,trigger_or._res)
# print('----------------------------------------------------')
# trigger_ecviv = T_ecvival()
# for x in 0,1:
#     for y in 0,1:
#         trigger_ecviv.In1 = x
#         trigger_ecviv.In2 = y
#         print(trigger_ecviv.In1,trigger_ecviv.In2,trigger_ecviv._res)

# trigger_or = Tor()
# trigger_or_not = TNot()
# for x in 0,1:
#     for y in 0,1:
#         trigger_or.In1 = x
#         trigger_or.In2 = y
#         trigger_or_not.In1 = trigger_or.Res
#         print(trigger_or.In1,trigger_or.In2,trigger_or_not._res)
# print('----------------------------------------------------')

