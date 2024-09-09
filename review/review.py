import argparse
import os
import git
from git import InvalidGitRepositoryError

def input_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Review the git log')
    parser.add_argument('-n', '--number', type=int, default=10, help='Number of commits to show')
    parser.add_argument('-a', '--author', type=str, help='Author of the commits')
    parser.add_argument('-s', '--since', type=str, help='Show commits more recent than a specific date')
    parser.add_argument('-u', '--until', type=str, help='Show commits older than a specific date')
    parser.add_argument('-m', '--message', type=str, help='Show commits with specific message')
    return parser.parse_args()

def main():
    args = input_parser()
    print(args)
    try:
        repo = git.Repo(os.getcwd(), search_parent_directories=True)
        print(f'Current repository: {repo}')
    except InvalidGitRepositoryError as err:
        exit(print(f'请在git目录下使用该命令: {err}'))

if __name__ == '__main__':
    main()