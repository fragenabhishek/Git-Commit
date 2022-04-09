import yaml
from datetime import datetime
from git import Repo

FILE_TO_COMMIT_NAME: str = 'hi.yaml'

def update_file_to_commit():
    # read file contents and update commit time.
    with open(FILE_TO_COMMIT_NAME, 'r') as file:
        YAML_FILE = {
            'LAST_COMMIT_ON':datetime.now().strftime("%A %B %d %Y at %X%p")
            }
    # Write new contents to file to be commited.
    with open(FILE_TO_COMMIT_NAME, 'w') as file: yaml.dump(YAML_FILE, file, default_flow_style=False, sort_keys=True)
    return YAML_FILE

def commit_repository(YAML_FILE):
    repo = Repo('.')
    repo.index.add([FILE_TO_COMMIT_NAME])
    repo.index.commit(f'Last commit was on {YAML_FILE["LAST_COMMIT_ON"]}.')
    origin = repo.remote('origin')
    origin.push()

if __name__ == '__main__': 
    commit_repository(update_file_to_commit())
    #update_file_to_commit()
    print("commit_sucessful")
