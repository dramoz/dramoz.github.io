# Python script helper functions for Makefile
import os

# --------------------------------------------------------------------------------
verbose = os.environ.get('VERBOSE', '0') != '0'
def vprint(str):
    if verbose:
        print(str)

# --------------------------------------------------------------------------------
def reload_process(command_line):
    from subprocess import Popen
    from shlex import split
    args = split(command_line)
    kill_process(args[0])
    print(f'Running process "{args[0]}"')
    Popen(args, start_new_session=True)

# --------------------------------------------------------------------------------
def run_process(command_line):
    from subprocess import Popen
    from shlex import split
    args = split(command_line)
    print(f'Running process "{args[0]}')
    Popen(args, start_new_session=True)

# --------------------------------------------------------------------------------
def terminate_process(name):
    import psutil
    
    terminated = False
    for process in psutil.process_iter(): #['pid', 'name', 'username']):
        if process.name() == name:
            process.terminate()
            try:
                process.wait(1)
            except psutil.TimeoutExpired:
                process.kill()
            finally:
                terminated = True
            
            break
    
    if terminated:
        print(f'Process "{name}" found, terminating...')
    else:
        print(f'Process "{name}" not running...')
    
# --------------------------------------------------------------------------------
def kill_process(name):
    import psutil
    
    terminated = False
    for process in psutil.process_iter(): #['pid', 'name', 'username']):
        if process.name() == name:
            process.kill()
            terminated = True
            break
    
    if terminated:
        print(f'Process "{name}" found, killing...')
    else:
        print(f'Process "{name}" not running...')
    
