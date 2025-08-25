import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth


@pytest.mark.parametrize("username, password", [
    ("sarimura", "sarimura_pass")
])
def test_registor(authenticator, username, password):
    authenticator.register(username,password)
    #authenticator.register(username,password)
    assert username in authenticator.users



@pytest.mark.parametrize("username, password, expected", [
    ("sarimura", "sarimura_pass","エラー: ユーザーは既に存在します。")
])
def test_registor_same(authenticator, username, password, expected):
    authenticator.register(username,password)
    with pytest.raises(ValueError, match=expected):
        authenticator.register(username,password)


@pytest.mark.parametrize("username, password, expected", [
    ("sarimura", "sarimura_pass","ログイン成功")
])
def test_login(authenticator, username, password, expected):
    authenticator.register(username,password)
    assert authenticator.login(username,password) == expected


@pytest.mark.parametrize("username, password, password_false, expected", [
    ("sarimura", "sarimura_pass","false_pass","エラー: ユーザー名またはパスワードが正しくありません。")
])
def test_login_false(authenticator, username, password, password_false, expected):
    authenticator.register(username,password)
    with pytest.raises(ValueError, match=expected):
        authenticator.login(username,password_false)

