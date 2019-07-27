"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import skydio.lcmtypes.body._wrench_t

class wrench_stamped_t(object):
    __slots__ = ["utime", "wrench"]

    def __init__(self,
                 utime=0,
                 wrench=None,
                 _skip_initialize=False):
        """ If _skip_initialize is True, all other constructor arguments are ignored """
        if _skip_initialize: return
        self.utime = utime
        self.wrench = skydio.lcmtypes.body.wrench_t._default() if wrench is None else wrench

    @staticmethod
    def _skytype_meta():
        return dict(
            type='struct',
            package='body',
            name='wrench_stamped_t',
        )

    @classmethod
    def _default(cls):
        return cls()

    def __repr__(self):
        return 'lcmtypes.body.wrench_stamped_t({})'.format(
            ', '.join('{}={}'.format(name, repr(getattr(self, name))) for name in self.__slots__))

    def encode(self):
        buf = BytesIO()
        buf.write(wrench_stamped_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.utime))
        assert self.wrench._get_packed_fingerprint() == skydio.lcmtypes.body.wrench_t._get_packed_fingerprint()
        self.wrench._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != wrench_stamped_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return wrench_stamped_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = wrench_stamped_t(_skip_initialize=True)
        self.utime = struct.unpack(">q", buf.read(8))[0]
        self.wrench = skydio.lcmtypes.body.wrench_t._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if wrench_stamped_t in parents: return 0
        newparents = parents + [wrench_stamped_t]
        tmphash = (0x546a30a37d5db6d0+ skydio.lcmtypes.body.wrench_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if wrench_stamped_t._packed_fingerprint is None:
            wrench_stamped_t._packed_fingerprint = struct.pack(">Q", wrench_stamped_t._get_hash_recursive([]))
        return wrench_stamped_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
