import subprocess
import random
import string

def generate_random_volume_id():
    # Generate a random hexadecimal string of length 8 in the format xxxx-xxxx
    random_id = '-'.join(''.join(random.choices(string.hexdigits.lower(), k=4)) for _ in range(2))
    return random_id

def change_volume_id(drive_letter):
    # Replace with the actual path to VolumeID64.exe
    volumeid_path = r'C:\spoofer\2. Hwid Spoofer\Penis\VolumeID64.exe'

    # Get the current volume ID before changing
    try:
        result_before = subprocess.run([volumeid_path, drive_letter], capture_output=True, text=True, shell=True)
        current_volume_id_before = result_before.stdout.strip().splitlines()[-1].strip()
        print(f"Current Volume ID of {drive_letter} before change: {current_volume_id_before}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to get current Volume ID before change for {drive_letter}: {e}")
        return

    # Generate a new random Volume ID
    new_volume_id = generate_random_volume_id()

    # Change the volume ID
    try:
        subprocess.run([volumeid_path, drive_letter, new_volume_id], check=True, shell=True)
        print(f"Successfully changed Volume ID of {drive_letter} to {new_volume_id}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change Volume ID for {drive_letter}: {e}")
        return

    # Get the current volume ID after changing
    try:
        result_after = subprocess.run([volumeid_path, drive_letter], capture_output=True, text=True, shell=True)
        current_volume_id_after = result_after.stdout.strip().splitlines()[-1].strip()
        print(f"Current Volume ID of {drive_letter} after change: {current_volume_id_after}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to get current Volume ID after change for {drive_letter}: {e}")
        return

    # Verify if the Volume ID has actually changed
    if current_volume_id_after == new_volume_id:
        print(f"Volume ID of {drive_letter} was successfully changed to {new_volume_id}.")
    else:
        print(f"Failed to verify Volume ID change for {drive_letter}. Current Volume ID is {current_volume_id_after}, expected {new_volume_id}.")

if __name__ == "__main__":
    drives_to_change = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'J:']

    for drive in drives_to_change:
        change_volume_id(drive)
