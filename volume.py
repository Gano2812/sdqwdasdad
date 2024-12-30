import subprocess
import random
import string
import os

def generate_random_volume_id():
    return '-'.join(''.join(random.choices(string.hexdigits.lower(), k=4)) for _ in range(2))

def change_volume_id(drive_letter):
    volumeid_path = r'C:\Users\%username%\AppData\Local\Temp'
    if not os.path.exists(volumeid_path):
        return

    try:
        subprocess.run([volumeid_path, drive_letter], capture_output=True, text=True)
    except subprocess.CalledProcessError:
        return

    new_volume_id = generate_random_volume_id()

    try:
        subprocess.run([volumeid_path, drive_letter, new_volume_id], check=True)
    except subprocess.CalledProcessError:
        return

if __name__ == "__main__":
    drives_to_change = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'J:']
    for drive in drives_to_change:
        change_volume_id(drive)
