py_boilerplate
================

python boilerplate for o-hayato


Table of Contents
-----------------

* [Description](#description)
* [Requirements](#requirements)
* [Install](#install)
* [Usage](#usage)
* [Contributing](#contributing)
* [Support and Migration](#support-and-migration)
* [License](#license)

Description
-----------

Pythonスクリプトを書く際のボイラープレート
毎回調べるのがめんどいからまとめていく

Requirements
------------

このプロジェクトを実行するには以下が必要です:

* [python][python]  3.4+
* [pip][pip]  8.1.2+
* [setuptools][setuptools]  19.2+

Install
-------

1. このボイラープレートを元に新しいプロジェクトを作る
1. `setup.cfg` 内の `py_boilerplate` を新しいプロジェクト名で置換する
1. venvの準備:
    ```console
    python3 -m venv ./venv # venvの作成
    . venv/bin/activate    # venvをカレントディレクトリに適用
    ```   
1. 開発用パッケージをインストール
    ```console
    pip install -e .[dev]
    ```
Usage
-----


1. pytest を使ったテスト
    ```console
    pytest
    ```
1. tox を使ったテスト
    ```console
    tox
    ```
1. ビルド
    ```console
    inv build
    ```
1. パッケージの配布
    ```console
    inv relese
    ```

Contributing
------------

PR歓迎


Support and Migration
---------------------

特に無し

License
-------

[MIT License][MIT License]


[python]: https://www.python.org
[MIT License]: http://petitviolet.mit-license.org/
[pip]: https://pypi.org/project/pip/
[setuptools]: https://pypi.org/project/setuptools/
