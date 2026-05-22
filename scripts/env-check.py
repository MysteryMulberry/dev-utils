import subprocess, sys, shutil

def check_tools():
    tools = ['python', 'node', 'npm', 'git', 'docker', 'curl', 'make', 'jq']
    for tool in tools:
        path = shutil.which(tool)
        if path:
            try:
                version = subprocess.run([tool, '--version'], capture_output=True, text=True, timeout=5)
                print(f'  {tool}: {version.stdout.strip()[:30]}')
            except:
                print(f'  {tool}: found at {path}')
        else:
            print(f'  {tool}: NOT FOUND')

if __name__=='__main__':
    print('Environment Check:')
    check_tools()
