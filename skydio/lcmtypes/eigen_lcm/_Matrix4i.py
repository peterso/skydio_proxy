"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class Matrix4i(object):
    __slots__ = ["data"]

    def __init__(self,
                 data=None,
                 _skip_initialize=False):
        """ If _skip_initialize is True, all other constructor arguments are ignored """
        if _skip_initialize: return
        self.data = [ 0 for dim0 in range(16) ] if data is None else data

    @staticmethod
    def _skytype_meta():
        return dict(
            type='struct',
            package='eigen_lcm',
            name='Matrix4i',
        )

    @classmethod
    def _default(cls):
        return cls()

    def __repr__(self):
        return 'lcmtypes.eigen_lcm.Matrix4i({})'.format(
            ', '.join('{}={}'.format(name, repr(getattr(self, name))) for name in self.__slots__))

    def encode(self):
        buf = BytesIO()
        buf.write(Matrix4i._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>16i', *self.data[:16]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != Matrix4i._get_packed_fingerprint():
            raise ValueError("Decode error")
        return Matrix4i._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = Matrix4i(_skip_initialize=True)
        self.data = list(struct.unpack('>16i', buf.read(64)))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if Matrix4i in parents: return 0
        tmphash = (0xab77edfd340d62d) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if Matrix4i._packed_fingerprint is None:
            Matrix4i._packed_fingerprint = struct.pack(">Q", Matrix4i._get_hash_recursive([]))
        return Matrix4i._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
