from git import Repo,GitCommandError

repo_url = input("what's the url of your repo")
message = input("what's your commit message")

def GitPush(url:str,message:str):
        repo = Repo(url)
        repo.index.add(update=True)
        repo.index.commit(message=message)

        try:
            origin = repo.remote("origin")
            origin.push()
            print("push scuessful")
        except GitCommandError as error:
            print("Push failed",error)

if __name__ == "__main__":
     GitPush(url="https://github.com/justmore5mins/easier-git",message="This is the first commit by python")