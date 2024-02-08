from git import Repo
import os

repository = "gitpython"
git_url = "git@github.com:mandjiny89/aws_user.git"

local_repo_directory = os.path.join(os.getcwd(), repository)
destination = 'master'

def clone_repo():
    if os.path.exists(local_repo_directory):
        print("Directory exists, pulling changes from master branch")
        repo = Repo(local_repo_directory)
        origin = repo.remotes.origin
        origin.pull(destination)
        print(os.getcwd())
    else:
        print("Directory does not exists, cloning")
        Repo.clone_from(git_url, local_repo_directory, branch=destination)


def chdirectory(path):
    os.chdir(path)

def create_branch(repo, branch_name):
    print("Creating a new branch with id name " + branch_name)
    current = repo.create_head(branch_name)
    current.checkout()

def update_file():
    print("Modifying the file")
    chdirectory(local_repo_directory)
    opened_file = open("user_list.txt", 'a')
    opened_file.write("{0}".format("Michael"))

def add_and_commit_changes(repo):
    print("Committing changes")
    repo.git.add(update=True)
    repo.git.commit("-m", "updating new rules changes into the repo")


def push_changes(repo, branch_name):
    print("Pushing changes")
    repo.git.push("--set-upstream", 'origin', branch_name)


if __name__ == "__main__":
    #clone the repository
    clone_repo()

    repo = Repo.init(local_repo_directory)
    branch_name = "feature/test"
    # gh_token = config('GH_API_TOKEN')

    #create a new branch
    create_branch(repo, branch_name)

    # update file
    update_file()

    # add and commit changes
    add_and_commit_changes(repo)

    # push changes
    push_changes(repo, branch_name)

    #setup github credentials and session
    # await setup_github(branch_name)


