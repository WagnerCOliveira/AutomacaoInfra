def test_named_running_and_enabled(host):
    named = host.service("named")
    assert named.is_running
    assert named.is_enabled


def test_consulta_dns(host):
    dns = host.addr("teste.exemplo.com.br")
    assert dns.is_resolvable
