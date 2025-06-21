import os
import shutil
from pathlib import Path

def organize_folder(folder_path):
    """Organize files in the specified folder"""
    
    # Define where different file types should go
    file_mappings = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.rtf', '.tex', '.wpd'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
        'Presentations': ['.ppt', '.pptx', '.odp'],
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.c', '.php', '.json', '.xml', '.yml', '.yaml'],
        'Software': ['.exe', '.msi', '.app', '.deb', '.rpm', '.dmg', '.pkg', '.appimage'],
        'Installers': ['.iso', '.img', '.bin', '.run'],
        'Data': ['.sql', '.db', '.sqlite'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
        'Ebooks': ['.epub', '.mobi', '.azw', '.azw3', '.fb2', '.lit']
    }
    
    # Create folders if they don't exist
    created_folders = []
    for folder_name in file_mappings.keys():
        folder = folder_path / folder_name
        if not folder.exists():
            folder.mkdir(exist_ok=True)
            created_folders.append(folder_name)
    
    # Create 'Others' folder for uncategorized files
    others_path = folder_path / 'Others'
    others_path.mkdir(exist_ok=True)
    
    # Keep track of what we moved
    move_summary = {folder: 0 for folder in file_mappings.keys()}
    move_summary['Others'] = 0
    
    # Move files to appropriate folders
    moved_count = 0
    skipped_count = 0
    
    for item in folder_path.iterdir():
        # Skip if it's a directory
        if item.is_dir():
            continue
        
        # Skip hidden files (starting with .)
        if item.name.startswith('.') and item.name != '.':
            skipped_count += 1
            continue
            
        # Get file extension
        file_ext = item.suffix.lower()
        moved = False
        
        # Check which folder this file belongs to
        for folder_name, extensions in file_mappings.items():
            if file_ext in extensions:
                destination = folder_path / folder_name / item.name
                
                # Handle duplicates by adding a number
                if destination.exists():
                    base = item.stem
                    num = 1
                    while destination.exists():
                        destination = folder_path / folder_name / f"{base}_{num}{file_ext}"
                        num += 1
                
                # Move the file
                try:
                    shutil.move(str(item), str(destination))
                    print(f"✓ Moved: {item.name} → {folder_name}/")
                    moved = True
                    moved_count += 1
                    move_summary[folder_name] += 1
                except Exception as e:
                    print(f"✗ Failed to move {item.name}: {e}")
                break
        
        # If file type not recognized, move to 'Others'
        if not moved and file_ext:  # Only move files with extensions
            destination = others_path / item.name
            if destination.exists():
                base = item.stem
                num = 1
                while destination.exists():
                    destination = others_path / f"{base}_{num}{file_ext}"
                    num += 1
            
            try:
                shutil.move(str(item), str(destination))
                print(f"✓ Moved: {item.name} → Others/")
                moved_count += 1
                move_summary['Others'] += 1
            except Exception as e:
                print(f"✗ Failed to move {item.name}: {e}")
    
    return moved_count, skipped_count, move_summary, created_folders

def display_summary(folder_path, moved_count, skipped_count, move_summary, created_folders):
    """Display organization summary"""
    print(f"\n{'='*50}")
    print(f"✨ Organization complete!")
    print(f"{'='*50}")
    print(f"📍 Organized folder: {folder_path}")
    print(f"📦 Files moved: {moved_count}")
    if skipped_count > 0:
        print(f"⏭️  Files skipped: {skipped_count} (hidden files)")
    
    if created_folders:
        print(f"\n📁 New folders created: {', '.join(created_folders)}")
    
    print("\n📊 File distribution:")
    for folder, count in move_summary.items():
        if count > 0:
            print(f"   {folder}: {count} files")
    
    # Count total files in each folder now
    print("\n📈 Current folder contents:")
    for folder in folder_path.iterdir():
        if folder.is_dir() and not folder.name.startswith('.'):
            file_count = len([f for f in folder.iterdir() if f.is_file()])
            if file_count > 0:
                print(f"   {folder.name}: {file_count} total files")

def main():
    print("🗂️  Desktop File Organizer Pro")
    print("=" * 50)
    print("Organize any folder by file type!")
    print("=" * 50)
    
    print("\n💡 Examples:")
    print(f"   • Downloads: {Path.home() / 'Downloads'}")
    print(f"   • Desktop: {Path.home() / 'Desktop'}")
    print(f"   • Custom: C:\\MyFolder or /home/user/myfolder")
    
    # Get folder path from user
    folder_input = input("\n📁 Enter the folder path to organize (or 'exit' to quit): ").strip()
    
    if folder_input.lower() == 'exit':
        print("\n👋 Goodbye!")
        return
    
    # Handle shortcuts for common folders
    if folder_input.lower() in ['downloads', 'download']:
        folder_path = Path.home() / 'Downloads'
    elif folder_input.lower() == 'desktop':
        folder_path = Path.home() / 'Desktop'
    elif folder_input.lower() in ['documents', 'docs']:
        folder_path = Path.home() / 'Documents'
    else:
        folder_path = Path(folder_input)
    
    # Validate the path
    if not folder_path.exists():
        print(f"\n Error: The folder '{folder_path}' does not exist!")
        return
    
    if not folder_path.is_dir():
        print(f"\n Error: '{folder_path}' is not a folder!")
        return
    
    # Show folder info
    print(f"\n Selected folder: {folder_path}")
    file_count = len([f for f in folder_path.iterdir() if f.is_file()])
    print(f"Contains {file_count} files")
    
    if file_count == 0:
        print("\n This folder is empty! Nothing to organize.")
        return
    
    # Confirm action
    response = input("\nProceed with organization? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\n🔄 Organizing files...\n")
        try:
            moved_count, skipped_count, move_summary, created_folders = organize_folder(folder_path)
            display_summary(folder_path, moved_count, skipped_count, move_summary, created_folders)
        except Exception as e:
            print(f"\n Error: {e}")
    else:
        print("\n File organizing complete!")

if __name__ == "__main__":
    main()