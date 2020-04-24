from diagrams import Diagram, Cluster
from diagrams.gcp.compute import Run
from diagrams.gcp.devtools import Build, GCR, SourceRepositories as GSR
from diagrams.gcp.database import SQL
from diagrams.onprem.vcs import Github
from diagrams.onprem.client import Client, User

with Diagram("Test", show=False):
    with Cluster("Google Cloud Platform"):
        with Cluster("CI/CD"):
            dev = GSR("source mirror")
            cicd = dev >> Build("build") >> GCR("container deploy")

        with Cluster("Services"):
            app = Run("Rails + React App")
            cicd >> app >> SQL("database")
        
    User("developer") >> Github("code push") >> dev
    Client("client") >> app