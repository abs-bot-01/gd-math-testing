import os
import signal
import subprocess
import time
from pathlib import Path

out = Path('/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/gd-math-levels')
out.mkdir(parents=True, exist_ok=True)
levels = ['stackBasicShapes', 'countWithSingleStick1To3', 'ssMultiplication31', 'stackMultiStick1To3']
for level in levels:
    env = os.environ.copy()
    env['DISPLAY'] = ':99'
    env['GDM_LEVEL_ID'] = level
    log = Path('/tmp') / f'godot-{level}-retry.log'
    with log.open('w') as fh:
        proc = subprocess.Popen(
            ['godot', '--path', '/shared/hermes/gd-math-godot', '--editor-pid=0'],
            env=env, stdout=fh, stderr=subprocess.STDOUT
        )
    time.sleep(25)
    subprocess.run(['import', '-window', 'root', str(out / f'{level}_00_initial.png')], env=env, check=False)
    time.sleep(2)
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
    print(level, 'screenshot=', out / f'{level}_00_initial.png', 'log=', log)
    time.sleep(2)
    
print('done')
