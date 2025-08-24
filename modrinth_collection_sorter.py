import sys
import datetime
import webbrowser

# Script Logic Explanation:
# This script checks ALL mods in the source collection (e.g., 114 mods)
# For each mod, it checks if there's a version available for the target Minecraft version
# - If YES: The mod is processed (either marked as already in target collection or available for update)
# - If NO: The mod is listed as "not available for target version"
# So the script doesn't actually stop early - it processes all mods but categorizes them differently

CURRENT_MINECRAFT_VERSION = '1.21.6'  # The version you are currently using
TARGET_MINECRAFT_VERSION = '1.21.8'  # The version you want to check for updates
LOADER = 'fabric'  # Your desired mod loader (e.g., "fabric", "forge", "quilt", "neoforge")
COLLECTION_ID = 'HO2OnfaY'  # Your source collection ID
TARGET_COLLECTION_ID = 'WiQSfz9H'  # Your target collection ID (replace as needed)

sys.argv = [
    'download_modrinth.py',
    '-cv', CURRENT_MINECRAFT_VERSION,
    '-tv', TARGET_MINECRAFT_VERSION,
    '-l', LOADER,
    '-c', COLLECTION_ID,
    '-t', TARGET_COLLECTION_ID
]

import argparse
import json
import os
from urllib import request, error

class ModrinthClient:
    def __init__(self):
        self.base_url = "https://api.modrinth.com"

    def get(self, url):
        try:
            with request.urlopen(self.base_url + url) as response:
                return json.loads(response.read())
        except error.URLError as e:
            print(f"Network error: {e}")
            return None

    def get_mod_version(self, mod_id):
        return self.get(f"/v2/project/{mod_id}/version")

    def get_collection(self, collection_id):
        return self.get(f"/v3/collection/{collection_id}")

modrinth_client = ModrinthClient()

def parse_args():
    parser = argparse.ArgumentParser(
        description="Check for mod updates in a Modrinth collection from your current Minecraft version to a target version and compare with a target collection."
    )
    parser.add_argument(
        "-c",
        "--collection",
        required=True,
        help="ID of the source collection to check."
    )
    parser.add_argument(
        "-cv", "--current-version", required=True, help='Current Minecraft version you are using.'
    )
    parser.add_argument(
        "-tv", "--target-version", required=True, help='Target Minecraft version to check for updates.'
    )
    parser.add_argument(
        "-l",
        "--loader",
        required=True,
        help='Loader to use ("fabric", "forge", "quilt" etc).',
    )
    parser.add_argument(
        "-t",
        "--target-collection",
        required=True,
        help="ID of the target collection to check for already saved mods."
    )
    return parser.parse_args()

args = parse_args()

LOGS_DIR = "modrinth_collection_sorter_logs"
HAS_VERSION_LOG = "has_target_version_mods.txt"
ALREADY_IN_TARGET_LOG = "already_in_target_collection.txt"

for d in [LOGS_DIR]:
    if not os.path.exists(d):
        os.mkdir(d)

def log_event(log_file, mod_id, mod_name, message_prefix, entry_count=None):
    log_path = os.path.join(LOGS_DIR, log_file)
    if entry_count is None:
        entry_count = 0
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip() and line.strip()[0].isdigit() and ". [" in line:
                        entry_count += 1
        entry_count += 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mod_link = f"https://modrinth.com/mod/{mod_id}"
    log_message = (
        f"{message_prefix}\n"
        f"🔹 MOD_NAME: {mod_name}\n"
        f"🆔 MOD_ID: {mod_id}\n"
        f"🎮 CURRENT_MC_VERSION: {args.current_version}\n"
        f"🎯 TARGET_MC_VERSION: {args.target_version}\n"
        f"🛠️ LOADER: {args.loader.upper()}\n"
        f"🔗 MOD_LINK: {mod_link}\n"
    )
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{entry_count}. [{timestamp}]\n{log_message}\n\n")
    print(f"{entry_count}. [{timestamp}]\n{log_message}\n")

def check_mod_for_target_version(mod_id):
    mod_versions_data = modrinth_client.get_mod_version(mod_id)
    if not mod_versions_data:
        return False
    has_version = any(
        args.target_version in mod_version["game_versions"] and args.loader in mod_version["loaders"]
        for mod_version in mod_versions_data
    )
    return has_version

def main():
    collection_details = modrinth_client.get_collection(args.collection)
    if not collection_details:
        print(f"Collection id={args.collection} not found")
        return
    mods = collection_details["projects"]
    print(f"Mods in source collection: {mods}\n")
    print(f"Total mods in source collection: {len(mods)}\n")
    print(f"Processing all {len(mods)} mods to check for {args.target_version} compatibility...\n")

    # Get mods in the target collection
    target_collection_details = modrinth_client.get_collection(args.target_collection)
    if not target_collection_details:
        print(f"Target collection id={args.target_collection} not found")
        target_mods = []
    else:
        target_mods = set(target_collection_details["projects"])

    has_update_count = 0
    already_in_target_count = 0
    no_update_count = 0
    has_update_mod_links = []
    no_update_mods = []
    
    for idx, mod_id in enumerate(mods, 1):
        print(f"Checking mod {idx}/{len(mods)}: {mod_id}")
        
        if check_mod_for_target_version(mod_id):
            mod_details = modrinth_client.get(f"/v2/project/{mod_id}")
            mod_name = mod_details["title"] if mod_details and "title" in mod_details else "Unknown"
            if mod_id in target_mods:
                already_in_target_count += 1
                log_event(ALREADY_IN_TARGET_LOG, mod_id, mod_name, "⏩ ALREADY IN TARGET COLLECTION:", already_in_target_count)
            else:
                has_update_count += 1
                log_event(HAS_VERSION_LOG, mod_id, mod_name, f"✅ HAS {args.target_version} VERSION UPDATE (BUT NOT IN TARGET COLLECTION):", has_update_count)
                has_update_mod_links.append(f"https://modrinth.com/mod/{mod_id}")
        else:
            # Mod doesn't have update for target version
            mod_details = modrinth_client.get(f"/v2/project/{mod_id}")
            mod_name = mod_details["title"] if mod_details and "title" in mod_details else "Unknown"
            no_update_count += 1
            no_update_mods.append(f"{no_update_count}. {mod_name} ({mod_id})")

    print(f"\nSummary:")
    print(f"Total mods checked: {len(mods)}")
    print(f"Mods with update for {args.target_version} but not in target collection: {has_update_count}")
    print(f"Mods already in target collection: {already_in_target_count}")
    print(f"Mods without update for {args.target_version}: {no_update_count}")
    
    if no_update_mods:
        print(f"\nMods NOT available for {args.target_version} (not in target collection):")
        for mod_entry in no_update_mods:
            print(mod_entry)

    if has_update_mod_links:
        open_links = input("\nDo you want to open all mods that have a version update in your browser? (Y/N): ").strip().lower()
        if open_links == 'y':
            print("Opening all updated mod links in your browser...")
            for link in has_update_mod_links:
                webbrowser.open_new_tab(link)
        else:
            print("Not opening any links.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        input("\nAll tasks finished. Press Enter to exit...")
