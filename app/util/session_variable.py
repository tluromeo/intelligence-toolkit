# Copyright (c) 2024 Microsoft Corporation. All rights reserved.
from typing import Any
import streamlit as st
import traceback

class SessionVariable:
    def __init__(self, default: Any="", prefix:str=""):
        """Create a managed session variable with a default value and a prefix.
        The prefix is used to avoid collisions between variables with the same name.
        
        To modify the variable use the value property, for example: `name.value = "Bob"`
        To get the value use the variable itself, for example: `name`

        Use this class to avoid using st.session_state dictionary directly and be able to
        just use the variables. These variables will share values across files as long as you use
        the same variable name and prefix.
        """
        (_, _, _, text) = traceback.extract_stack()[-2]
        var_name = text[:text.find('=')].strip()

        self._key = "_".join(arg for arg in [prefix, var_name] if arg != "")
        self._value = default
        if self._key not in st.session_state:
            st.session_state[self._key] = default
        else:
            self._value = st.session_state[self._key]

    @property
    def key(self) -> str:
        return self._key

    @property
    def value(self) -> Any:
        return st.session_state[self._key] 

    @value.setter
    def value(self, value: Any) -> None:
        st.session_state[self._key] = value

    def __repr__(self) -> Any:
        return str(st.session_state[self._key])