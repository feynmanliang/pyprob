# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class Gamma(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGamma(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Gamma()
        x.Init(buf, n + offset)
        return x

    # Gamma
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Gamma
    def Shape(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Gamma
    def Rate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

def GammaStart(builder): builder.StartObject(2)
def GammaAddShape(builder, shape): builder.PrependFloat64Slot(0, shape, 0.0)
def GammaAddRate(builder, rate): builder.PrependFloat64Slot(1, rate, 0.0)
def GammaEnd(builder): return builder.EndObject()
