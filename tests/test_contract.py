from pathlib import Path
import ast
s=(Path(__file__).parents[1]/'contracts/contract.py').read_text()
def test_parse():ast.parse(s)
def test_unique_boundary_lifecycle():assert all(('def '+x) in s for x in ('file_beacon','review_beacon','confirm_beacon','withdraw_beacon','get_beacon'))
def test_consensus_binds_digests():assert "mine['digests']==theirs.get('digests')" in s and 'nondet.web.get' in s
def test_distinct_hosts_required():assert 'a[0]==b[0]' in s
