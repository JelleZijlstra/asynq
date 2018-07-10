import types
from typing import Any, Callable, Iterable, List, Mapping

from . import futures

import asynq

class AsyncTaskCancelledError(GeneratorExit): ...

class AsyncTaskResult(GeneratorExit):
    def __init__(self, result: Any) -> None: ...

class AsyncTask(futures.FutureBase):
    def __init__(
        self,
        generator: types.GeneratorType,
        fn: Callable[..., Any],
        args: Iterable[object],
        kwargs: Mapping[str, object],
    ) -> None: ...
    def can_continue(self) -> bool: ...
    def is_blocked(self) -> bool: ...
    def dump_perf_stats(self) -> None: ...
    def to_str(self) -> str: ...
    def collect_perf_stats(self) -> None: ...
    def traceback(self) -> List[str]: ...
    def dump(self, indent: int = ...) -> None: ...
