"""
   Copyright 10/2020 - 04/2021 Paul Seibert for Diploma Thesis at TU Dresden
   Copyright 05/2021 - 12/2021 TU Dresden (Paul Seibert as Scientific Assistant)
   Copyright 2022 TU Dresden (Paul Seibert as Scientific Employee)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from __future__ import annotations

import tensorflow as tf

from mcrpy.src import descriptor_factory
from mcrpy.descriptors.Descriptor import Descriptor


class VolumeFractions(Descriptor):
    is_differentiable = True

    @staticmethod
    def make_singlephase_descriptor(**kwargs) -> callable:

        @tf.function
        def compute_descriptor(microstructure: tf.Tensor) -> tf.Tensor:
            return tf.math.reduce_mean(microstructure)
        return compute_descriptor


def register() -> None:
    descriptor_factory.register("VolumeFractions", VolumeFractions)
