from enum import Enum
from typing import Any
from typing import Collection
from typing import List
from typing import Optional
from typing import overload
from typing import Type
from typing import Union

from typing_extensions import Literal

class OutputType(Enum):
    ID: int = ...
    SUBWORD: int = ...

class BPE:
    bpe_cython: Any = ...
    def __init__(self, model: str, n_threads: int = ...) -> None: ...
    @staticmethod
    def train(
        data: str,
        model: str,
        vocab_size: int,
        coverage: float = ...,
        n_threads: int = ...,
        pad_id: int = ...,
        unk_id: int = ...,
        bos_id: int = ...,
        eos_id: int = ...,
    ) -> BPE: ...
    @overload
    def encode(
        self,
        sentences: List[str],
        output_type: Literal[OutputType.ID],
        bos: bool = ...,
        eos: bool = ...,
        reverse: bool = ...,
        dropout_prob: float = ...,
    ) -> List[List[int]]: ...
    @overload
    def encode(
        self,
        sentences: List[str],
        output_type: Literal[OutputType.SUBWORD],
        bos: bool = ...,
        eos: bool = ...,
        reverse: bool = ...,
        dropout_prob: float = ...,
    ) -> List[List[str]]: ...
    def vocab_size(self) -> int: ...
    def vocab(self) -> List[str]: ...
    def subword_to_id(self, subword: str) -> int: ...
    def id_to_subword(self, id: int) -> str: ...
    def decode(
        self, ids: List[int], ignore_ids: Optional[Collection[int]] = ...
    ) -> str: ...
