# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class MultivariateNormal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMultivariateNormal(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MultivariateNormal()
        x.Init(buf, n + offset)
        return x

    # MultivariateNormal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MultivariateNormal
    def Mean(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MultivariateNormal
    def Covariance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def MultivariateNormalStart(builder): builder.StartObject(2)
def MultivariateNormalAddMean(builder, mean): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(mean), 0)
def MultivariateNormalAddCovariance(builder, covariance): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(covariance), 0)
def MultivariateNormalEnd(builder): return builder.EndObject()
