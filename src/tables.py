from typing import Literal, Union
import pandas as pd


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
