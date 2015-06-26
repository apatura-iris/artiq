_prefixes_str = "pnum_kMG"
_smallest_prefix_exp = -12


def _register_unit(unit, prefixes):
    exponent = _smallest_prefix_exp
    for prefix in _prefixes_str:
        if prefix in prefixes:
            full_name = prefix + unit if prefix != "_" else unit
            globals()[full_name] = 10.**exponent
        exponent += 3


_register_unit("s", "pnum_")
_register_unit("Hz", "_kMG")
_register_unit("dB", "_")
_register_unit("V", "um_k")
