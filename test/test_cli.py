import unittest.mock as mock

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

def test_do_action_calls_correct_module():
    from radmin.main import do_action
    with mock.patch('radmin.dump.do_dump') as do_dump, mock.patch('radmin.plan.do_plan') as do_plan, mock.patch('radmin.apply.do_apply') as do_apply:
        do_action(mock.Mock(subcommand='dump', source='source', templates=['1', '2'], output='output'))
        do_dump.assert_called_once_with('source', ['1', '2'], 'output')
        
        do_action(mock.Mock(subcommand='plan', target='target', output='output'))
        do_plan.assert_called_once_with('target', 'output')
        
        do_action(mock.Mock(subcommand='apply', plan='plan'))
        do_apply.assert_called_once_with('plan')