"""Test ezbee."""
# pylint: disable=broad-except
from ezbee import __version__, ezbee
from ezbee.loadtext import loadtext


def test_sanity():
    """Sanity check."""
    try:
        assert not ezbee([""], [""])
    except Exception:
        assert True


def test_data_en_zh():
    """Test data/test-en/zh.txt.

    pytest tests\test_ezbee.py -k en_zh

    poetry remove holoviews  plotly seaborn
           holoviews 1.14.8 plotly 5.6.0 seaborn 0.11.2
        du -sh .  # 452M
    poetry add -E holoviews plotly seaborn
    """
    text_en = loadtext("data/test-en.txt")
    text_zh = loadtext("data/test-zh.txt")
    list1 = [elm.strip() for elm in text_en.splitlines() if elm.strip()]
    list2 = [elm.strip() for elm in text_zh.splitlines() if elm.strip()]

    # (len(list1), len(list2)) == (33, 36)

    res = ezbee(list1, list2)
    assert len(res) == 36
    assert res[-1] == (35, 32, 0.5)
    assert res[15] == (15, 14, 0.31)
    assert [elm[0] for elm in res if not isinstance(elm[0], str)] == [*range(36)]
    assert [elm[1] for elm in res if not isinstance(elm[1], str)] == [*range(33)]
