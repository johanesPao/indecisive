import os
import warnings
from dotenv import load_dotenv


class Env:
    def __init__(
        self,
        tv_user: str | None = None,
        tv_pass: str | None = None
    ) -> None:
        '''
        A class to load all the environment required to run the program

        Attributes
        ----------
        tv_user : str | None
            tradingview username, can be overwritten on class initiation (default is None)
        tv_pass : str | None
            tradingview password for the given username, must be filled when username is filled (default is None)

        Methods
        -------
        None
        '''
        load_dotenv()
        # check for tv_user and tv_pass
        if tv_user is not None and tv_pass is None:
            warnings.warn('tv_pass cannot be None when tv_user being supplied, reverting tv_user to None')
            tv_user = None
        if tv_user is None and tv_pass is not None:
            warnings.warn('tv_user cannot be None when tv_pass being supplied, reverting tv_pass to None')
            tv_pass = None
            
        self.tv_user = os.getenv('TV_USER') if tv_user is None else tv_user
        self.tv_pass = os.getenv('TV_PASS') if tv_pass is None else tv_pass