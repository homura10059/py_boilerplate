py_boilerplate
================

Description
-----------

Pythonスクリプトを書く際のボイラープレート
毎回調べるのがめんどいからまとめていく

Requirements
------------

このプロジェクトを実行するには以下が必要です:

* `python`_ 3.4+
* `pip`_ 8.1.2+
* `setuptools`_ 19.2+

Install
-------

なし

Usage
-----

1. このボイラープレートを元に新しいプロジェクトを作る
2. venvの準備::

    python3 -m venv ./venv # venvの作成
    . venv/bin/activate    # venvをカレントディレクトリに適用

3. 開発用パッケージをインストール::

    pip install -e '.[dev]'

4. pytest を使ったテスト::

    pytest

5. tox を使ったテスト::

    tox

6. パッケージの配布::

    # 配布できる形に固める
    python setup.py sdist
    python setup.py bdist_wheel
    # PyPIへのアップロード
    twine upload dist/*

Contributing
------------

PR歓迎


Support and Migration
---------------------

特に無し

License
-------

`MIT License`_

.. _python: https://www.python.org
.. _MIT License: http://petitviolet.mit-license.org/
.. _pip: https://pypi.org/project/pip/
.. _setuptools: https://pypi.org/project/setuptools/