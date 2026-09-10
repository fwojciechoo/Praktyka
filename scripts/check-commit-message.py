import re
import sys

pattern = r"^(feat|fix|test|docs|refactor|chore|ci)(\([a-z0-9_-]+\))?!?: .+"

message = open(sys.argv[1], encoding="utf_8").read().splitlines()[0]

if re.match(pattern, message):
    print("Valid conventional commit message")
    sys.exit(0)
else:
    print("Invalid conventional commit message")
    sys.exit(1)