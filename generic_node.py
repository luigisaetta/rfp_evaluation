"""
Generic node
"""

from langchain_core.runnables import Runnable
from eval_state import EvaluationState


class GenericNode(Runnable):
    """
    Does something
    """

    def invoke(self, state: EvaluationState, config=None, **kwargs) -> EvaluationState:
        """
        Does something... to be specified in subclasses
        """
        return state
