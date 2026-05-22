import os, shutil, tarfile, sys
from datetime import datetime

def create_backup(source_dir, backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    source_name = os.path.basename(source_dir)
    archive_name = f'{source_name}_{timestamp}.tar.gz'
    archive_path = os.path.join(backup_dir, archive_name)
    with tarfile.open(archive_path, 'w:gz') as tar:
        tar.add(source_dir, arcname=source_name)
    print(f'Backup created: {archive_path}')
    print(f'Size: {os.path.getsize(archive_path) / 1024 / 1024:.2f} MB')

if __name__=='__main__':
    create_backup(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else './backups')
