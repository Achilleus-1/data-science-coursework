"""Execute every exercise script using only the included synthetic fixture data."""
import os
import pathlib
import subprocess
import sys
root = pathlib.Path(__file__).resolve().parents[1]
env = dict(os.environ, MPLBACKEND='Agg', PYTHONUTF8='1')
for path in sorted(root.glob('*/exercises.py')):
    result = subprocess.run([sys.executable, str(path)], cwd=path.parent, env=env,
                            capture_output=True, text=True, encoding='utf-8', timeout=120)
    if result.returncode:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    print('Passed: ' + path.parent.name)
