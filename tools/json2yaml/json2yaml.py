#!/usr/bin/env python3
import json, sys, yaml
data = json.load(sys.stdin if len(sys.argv) == 1 else open(sys.argv[1]))
print(yaml.dump(data, allow_unicode=True, default_flow_style=False))
