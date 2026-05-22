import psutil, sys, json

def monitor():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    print(f'CPU: {cpu}%')
    print(f'Memory: {mem.percent}% ({mem.used//1024//1024}MB / {mem.total//1024//1024}MB)')
    print(f'Disk: {disk.percent}% ({disk.used//1024//1024//1024}GB / {disk.total//1024//1024//1024}GB)')
    for p in psutil.process_iter(['pid','name','cpu_percent','memory_percent']):
        try:
            if p.info['cpu_percent'] > 1:
                print(f"  PID:{p.info['pid']} {p.info['name'][:20]:20s} CPU:{p.info['cpu_percent']:.1f}% MEM:{p.info['memory_percent']:.1f}%")
        except: pass

if __name__=='__main__': monitor()
