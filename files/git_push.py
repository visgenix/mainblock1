import subprocess
import os

def run_git_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode().strip()
    except subprocess.CalledProcessError as e:
        return e.output.decode().strip()

def git_add_commit_push(repo_path, commit_message,private_key_path):
    # Change to the repository directory
    os.chdir(repo_path)
    
    # Set the GIT_SSH_COMMAND to use the specified private key
    git_ssh_command = f"ssh -i {private_key_path}"
    os.environ["GIT_SSH_COMMAND"] = git_ssh_command

    # Add changes
    add_result = run_git_command("git add .")
    print("Git Add Result:\n", add_result)

    # Commit changes
    commit_result = run_git_command(f"git commit -m \"{commit_message}\"")
    print("Git Commit Result:\n", commit_result)
                                                                                                
    push_result = run_git_command(f"git push")
    print("Git Push Result:\n", push_result)




