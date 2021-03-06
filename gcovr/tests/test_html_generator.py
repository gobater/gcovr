import os
import pytest
import sys
from ..html_generator import _make_short_sourcename

CurrentDrive = os.getcwd()[0:1]


@pytest.mark.parametrize("outfile,source_filename", [('../gcovr', 'C:\\other_dir\\project\\source.c'),
                                                     ('../gcovr/', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr\\', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr\\result.html', 'C:\\other_dir\\project\\source.c'),
                                                     ('..\\gcovr\\result', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('C:\\gcovr', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('C:/gcovr', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c'),
                                                     ('C:/gcovr_files', 'C:\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\other_dir\\project\\source.c')
                                                     ])
@pytest.mark.skipif(sys.platform != 'win32', reason="only for Windows")
def test_windows__make_short_sourcename(outfile, source_filename):
    outfile = outfile.replace('C:', CurrentDrive)
    source_filename = source_filename.replace('C:', CurrentDrive)

    result = _make_short_sourcename(outfile, source_filename)
    print("=" * 100)
    print(outfile)
    print(source_filename)
    print(result)
    assert ':' not in result or (result.startswith(CurrentDrive) and ':' not in result[2:])

    assert len(result) < 256
