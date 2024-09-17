import pytest
from unittest.mock import Mock, patch

def test_parse_args():
    from radmin.main import parse_args
    args = parse_args(['dump', '--source', 'source', '--templates', '1', '2', '--output', 'output'])
    assert args.subcommand == 'dump'
    assert args.source == 'source'
    assert args.templates == ['1', '2']
    assert args.output == 'output'
    
    args = parse_args(['plan', '--target', 'target', '--output', 'output'])
    assert args.subcommand == 'plan'
    assert args.target == 'target'
    assert args.output == 'output'
    
    args = parse_args(['apply', '--plan', 'plan'])
    assert args.subcommand == 'apply'
    assert args.plan == 'plan'

# If you prefer to use a fixture, you can do it this way:
@pytest.fixture(autouse=True)
def mock_imports():
    with patch('radmin.main.do_dump') as mock_do_dump, \
         patch('radmin.main.do_plan') as mock_do_plan, \
         patch('radmin.main.do_apply') as mock_do_apply:
        yield mock_do_dump, mock_do_plan, mock_do_apply

def test_do_action_with_fixture(mock_imports):
    _, mock_do_plan, mock_do_apply = mock_imports
    from radmin.main import do_action

    # Test plan action
    args = Mock(subcommand='plan', target='target', output='output')
    do_action(args)
    mock_do_plan.assert_called_once_with('target', 'output')
    
    # Test apply action
    args = Mock(subcommand='apply', plan='plan')
    do_action(args)
    mock_do_apply.assert_called_once_with('plan')

def test_do_dump(mock_imports):
    mock_do_dump, _, _ = mock_imports
    from radmin.main import do_action
    args = Mock(subcommand='dump', source='source', templates=['1', '2'], output='output', db_conn_string="stringy")
    do_action(args)
    mock_do_dump.assert_called_once_with('source', ['1', '2'], 'output', 'stringy')

def test_do_dump_with_environment_conn_string(mock_imports):
    mock_do_dump, _, _ = mock_imports
    from radmin.main import do_action
    args = Mock(subcommand='dump', source='source', templates=['1', '2'], output='output', db_conn_string=None)
    with patch('os.environ', {'RADMIN_DB_CONN_STRING': 'env_string'}):
        do_action(args)
    mock_do_dump.assert_called_once_with('source', ['1', '2'], 'output', 'env_string')