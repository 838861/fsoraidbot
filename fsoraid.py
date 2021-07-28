#/usr/bin/env python
# coding: utf-8

import argparse
import json

def command_show(args):
    wave = args.wave
    level = args.level
    find_by_wave = True if args.level is None else False
    w = wave if wave < 8 else 8 + (wave - 8) % 6

    target = [t for t in [(args.deathclaw, 'デス'),(args.mirelurk, 'カニ'), (args.sentory, 'ロボ')] if t[0]]
    with open('data_bosses.json', 'r') as f:
        data = json.load(f)

    result = [bosses for bosses in data['Bosses'] if bosses['nickname'] == target[0][1]]

    if result is None:
        print('unmatched')
    elif find_by_wave:
        b = [boss for boss in result if boss['Wave'] == w]
        if b is not None and len(b) > 0:
            item = b[0]
            print(f"Name:{item['Name']}")
            if wave <= 13:
              print(f"Wave:{wave}")
            else:
              print(f"Wave:{wave}({item['Wave']})")

            print(f"Level:{item['Level']}")
            print(f"HP:{'{:,}'.format(item['HP'])}")
        else:
            print('unmatched')
    else:
        b = [boss for boss in result if boss['Level'] == level]
        if b is not None and len(b) > 0:
            item = b[0]
            print(f"Name:{item['Name']}")
            print(f"Wave:{wave}({item['Wave']})")
            print(f"Level:{item['Level']}")
            print(f"HP:{'{:,}'.format(item['HP'])}")
        else:
            print('unmatched')

def command_attack(args):
    print(args)

def command_remain(args):
    wave = args.wave
    level = args.level
    parcent = args.parcentage
    find_by_wave = True if args.level is None else False
    w = wave if wave < 8 else 8 + (wave - 8) % 6

    target = [t for t in [(args.deathclaw, 'デス'),(args.mirelurk, 'カニ'), (args.sentory, 'ロボ')] if t[0]]
    with open('data_bosses.json', 'r') as f:
        data = json.load(f)

    result = [bosses for bosses in data['Bosses'] if bosses['nickname'] == target[0][1]]

    if result is None:
        print('unmatched by nickname')
    elif find_by_wave:
        b = [boss for boss in result if boss['Wave'] == w]
        if b is not None and len(b) > 0:
            item = b[0]
            hp = item['HP']
            minhp = item['HP'] * (parcent - 1) // 100
            maxhp = item['HP'] * parcent // 100
            print(f"{item['Name']} Wave:{wave}({item['Wave']}) Lv:{item['Level']}")
            print(f"Remaining HP:{'{:,}'.format(minhp)} ~ {'{:,}'.format(maxhp)} / {'{:,}'.format(item['HP'])} ({parcent}%)")
        else:
            print(f'unmatched by wave({w})')
    else:
        b = [boss for boss in result if boss['Level'] == level]
        if b is not None and len(b) > 0:
            item = b[0]
            hp = item['HP']
            minhp = item['HP'] * (parcent - 1) // 100
            maxhp = item['HP'] * parcent // 100
            print(f"{item['Name']} Lv:{item['Level']}")
            print(f"Remaining HP:{'{:,}'.format(minhp)} ~ {'{:,}'.format(maxhp)} / {'{:,}'.format(item['HP'])} ({parcent}%)")
        else:
            print('unmatched by level')

def command_help(args):
    print(parser.parse_args([args.command, '--help']))

help_wave = '何波か指定してね'
help_level = 'ボスのレベルを指定してね'
help_deathclaw = 'デスクロー'
help_mirelurk = 'マイアラーククイーン'
help_sentory = 'セントリーボット(or コーサー)'
help_punch = 'このダメージで何回殴れば処せるのか'
help_parcentage = '残りHPをパーセンテージで指定してね'

parser = argparse.ArgumentParser(description='FSO raid helper tools')
subparsers = parser.add_subparsers()

# コマンドの parser を作成
parser_show = subparsers.add_parser('show', help='see `show -h`')
show_cmd_paramset_w_or_l = parser_show.add_mutually_exclusive_group(required=True)
show_cmd_paramset_w_or_l.add_argument('-w', '--wave', type=int, help=help_wave)
show_cmd_paramset_w_or_l.add_argument('-l', '--level', type=int, help=help_level)

show_cmd_paramset_target = parser_show.add_mutually_exclusive_group(required=True)
show_cmd_paramset_target.add_argument('-d', '--deathclaw', action='store_true', help=help_deathclaw)
show_cmd_paramset_target.add_argument('-m', '--mirelurk', action='store_true', help=help_mirelurk)
show_cmd_paramset_target.add_argument('-s', '--sentory', action='store_true', help=help_sentory)
parser_show.set_defaults(handler=command_show)

parser_attack = subparsers.add_parser('attack', help='see `attack -h`')
attack_cmd_paramset_w_or_l = parser_attack.add_mutually_exclusive_group(required=True)
attack_cmd_paramset_w_or_l.add_argument('-w', '--wave', type=int, help=help_wave)
attack_cmd_paramset_w_or_l.add_argument('-l', '--level', type=int, help=help_level)

attack_cmd_paramset_target = parser_attack.add_mutually_exclusive_group(required=True)
attack_cmd_paramset_target.add_argument('-d', '--deathclaw', action='store_true', help=help_deathclaw)
attack_cmd_paramset_target.add_argument('-m', '--mirelurk', action='store_true', help=help_mirelurk)
attack_cmd_paramset_target.add_argument('-s', '--sentory', action='store_true', help=help_sentory)

parser_attack.add_argument('-p', '--punch', type=int, default=1, help=help_punch)
parser_attack.set_defaults(handler=command_attack)

parser_remain = subparsers.add_parser('remain', help='see `remain -h`')
remain_cmd_paramset_w_or_l = parser_remain.add_mutually_exclusive_group(required=True)
remain_cmd_paramset_w_or_l.add_argument('-w', '--wave', type=int, help=help_wave)
remain_cmd_paramset_w_or_l.add_argument('-l', '--level', type=int, help=help_level)

remain_cmd_paramset_target = parser_remain.add_mutually_exclusive_group(required=True)
remain_cmd_paramset_target.add_argument('-d', '--deathclaw', action='store_true', help=help_deathclaw)
remain_cmd_paramset_target.add_argument('-m', '--mirelurk', action='store_true', help=help_mirelurk)
remain_cmd_paramset_target.add_argument('-s', '--sentory', action='store_true', help=help_sentory)

parser_remain.add_argument('-p', '--parcentage', type=int, default=1, help=help_parcentage)
parser_remain.set_defaults(handler=command_remain)

# help コマンドの parser を作成
parser_help = subparsers.add_parser('help', help='see `help`')
parser_help.add_argument('command', help='command name which help is shown')
parser_help.set_defaults(handler=command_help)

# コマンドライン引数をパースして対応するハンドラ関数を実行
args = parser.parse_args()
if hasattr(args, 'handler'):
    args.handler(args)
else:
    # 未知のサブコマンドの場合はヘルプを表示
    parser.print_help()

