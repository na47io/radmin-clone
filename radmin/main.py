import sys
import argparse
from radmin.dump import do_dump
from radmin.plan import do_plan
from radmin.apply import do_apply

def parse_args(args):
    parser = argparse.ArgumentParser(description='radmin CLI - a tool for managing Clarion Reporting environments with VCS.')

    parser.add_argument('--chdir', help='Change the current working directory before executing the subcommand.')

    subparsers = parser.add_subparsers(dest="subcommand", help='sub-command help', required=True)

    dump_parser = subparsers.add_parser('dump', help='Dump some or all resources from the Clarion Reporting environment.')
    dump_parser.add_argument('--source', help='Name of the source environment to dump resources from.', required=True)
    dump_parser.add_argument('--templates', nargs='+', help='List of template ids to dump.', required=True)
    dump_parser.add_argument('--output', help='Output directory for dumped resources.', required=True)

    plan_parser = subparsers.add_parser('plan', help='Plan changes to the Clarion Reporting environment. Resources are read from all the .json files in the current directory or the input directory (see --chdir option) resursively')
    plan_parser.add_argument('--target', help='Name of the target environment to plan changes for.', required=True)
    plan_parser.add_argument('--output', help='Output directory for the plan file.', required=True)

    apply_parser = subparsers.add_parser('apply', help='Apply changes to the Clarion Reporting environment.')
    apply_parser.add_argument('--plan', help='Path to the plan file to apply.', required=True)

    return parser.parse_args(args)

def do_action(args):
    if args.subcommand == 'dump':
        print(f'Dumping resources from {args.source} environment...')
        do_dump(args.source, args.templates, args.output)
    elif args.subcommand == 'plan':
        print(f'Planning changes for {args.target} environment...')
        do_plan(args.target, args.output)
    elif args.subcommand == 'apply':
        print(f'Applying changes from {args.plan}...')
        do_apply(args.plan)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:]) # sys.argv[1:] is used to skip the first argument which is the script name
    do_action(args)
    