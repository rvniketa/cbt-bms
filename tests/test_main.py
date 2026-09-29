from cbt_bms.main import main


def test_main_runs(capsys):
    main()
    assert "cbt-bms" in capsys.readouterr().out
