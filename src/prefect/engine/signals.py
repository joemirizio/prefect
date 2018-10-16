# Licensed under LICENSE.md; also available at https://www.prefect.io/licenses/alpha-eula

"""
These classes are used to signal state changes when tasks or flows are running. Signals
are used in TaskRunners and FlowRunners as a way of communicating the changes in states.
"""

from prefect.engine import state
from prefect.utilities.exceptions import PrefectError


class PrefectStateSignal(PrefectError):
    """
    Create a new PrefectStateSignal object.

    Args:
        - message (Any, optional): Defaults to `None`. A message about the signal.
    """

    _state_cls = state.State

    def __init__(self, message=None, *args, **kwargs) -> None:  # type: ignore
        super().__init__(message)  # type: ignore
        self.state = self._state_cls(message=self, *args, **kwargs)


class FAIL(PrefectStateSignal):
    """
    Indicates that a task failed.

    Args:
        - message (Any, optional): Defaults to `None`. A message about the signal.
    """

    _state_cls = state.Failed


class TRIGGERFAIL(FAIL):
    """
    Indicates that a task trigger failed.

    Args:
        - message (Any, optional): Defaults to `None`. A message about the signal.
    """

    _state_cls = state.TriggerFailed


class SUCCESS(PrefectStateSignal):
    """
    Indicates that a task succeeded.

    Args:
        - message (Any, optional): Defaults to `None`. A message about the signal.
    """

    _state_cls = state.Success


class RETRY(PrefectStateSignal):
    """
    Used to indicate that a task should be retried.

    Args:
        - message (Any, optional): Defaults to `None`. A message about the signal.
    """

    _state_cls = state.Retrying


class SKIP(PrefectStateSignal):
    """
    Indicates that a task was skipped. By default, downstream tasks will
    act as if skipped tasks succeeded.

    Args:
        - message (Any, optional): Defaults to `None`. A message about the signal.
    """

    _state_cls = state.Skipped


class PAUSE(PrefectStateSignal):
    """
    Indicates that a task should not run and wait for manual execution.

    Args:
        - message (Any, optional): Defaults to `None`. A message about the signal.
    """
