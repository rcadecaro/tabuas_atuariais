from typing import Literal, Union
import pandas as pd

#TODO: I can try to impplement the function in cython

class ActuarialTable:
    def __init__(
            self,
            table: Union[
                Literal["UP-94M"],
                Literal["UP-94F"],
                Literal["CSO-80"],
                Literal["AT-83M"],
                Literal["AT-83F"],
                Literal["AT-2000M"],
                Literal["AT-2000F"],
                Literal["BRS 2010M"],
                Literal["BRS 2010F"],
                Literal["BRM 2010M"],
                Literal["BRM 2010F"],
                Literal["SP-2005M"],
                Literal["SP-2005F"],
                Literal["RV-85M"],
                Literal["RV-85F"],
                Literal["GAM-94M"],
                Literal["GAM-94F"],
                Literal["RP-2000M"],
                Literal["RP-2000F"],
                Literal["BRS-2015M"],
                Literal["BRS-2015F"],
                Literal["BRM-2025M"],
                Literal["BRM-2015F"]
            ]
        ) -> None:
        self.table = pd.read_csv()

    def p_x(self):
        pass

    def n_p_x(self):
        pass
    
    def n_bar_q_x(self): #? How do I put a bar here?
        pass

    def bar_n_Q_x(self): #? How do I put a bar here?
        pass

    def n_bar_m_Q_x(self):
        pass

    def m_x(self):
        pass

    def n_p_xy(self):
        pass

    def n_Q_xy(self):
        pass

    def n_p_xOVERy(self): #? There is a bar over xy
        pass

    def bar_n_Q_xOVERy(self):
        pass

    def VP_x(self):
        pass

    def n_E_x(self):
        pass

    def ä_x(self): #? I should find a way to take out the umlaut
        pass

    def a_x(self):
        pass

    def n_bar_ä_x(self):
        pass
