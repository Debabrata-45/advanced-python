class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Freelancer(User):
    def __init__(self, user_id, name, skill):
        super().__init__(user_id, name)
        self.skill = skill
        self.earnings = 0
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def receive_payment(self, amount):
        self.earnings += amount

    def __str__(self):
        return f"Freelancer ID: {self.user_id}, Name: {self.name}, Skill: {self.skill}, Earnings: {self.earnings}"


class Client(User):
    def __init__(self, user_id, name, company):
        super().__init__(user_id, name)
        self.company = company
        self.projects = []

    def post_project(self, project):
        self.projects.append(project)

    def __str__(self):
        return f"Client ID: {self.user_id}, Name: {self.name}, Company: {self.company}"


class Project:
    def __init__(self, project_id, title, budget, client):
        self.project_id = project_id
        self.title = title
        self.budget = budget
        self.client = client
        self.freelancer = None
        self.status = "Open"

    def assign_freelancer(self, freelancer):
        self.freelancer = freelancer
        self.status = "Assigned"
        freelancer.add_project(self)

    def complete_project(self):
        if self.freelancer:
            self.status = "Completed"
        else:
            print("No freelancer assigned")

    def __str__(self):
        freelancer_name = self.freelancer.name if self.freelancer else "None"
        return f"Project ID: {self.project_id}, Title: {self.title}, Budget: {self.budget}, Status: {self.status}, Freelancer: {freelancer_name}"


class Marketplace:
    def __init__(self):
        self.freelancers = {}
        self.clients = {}
        self.projects = {}

    def register_freelancer(self, freelancer):
        self.freelancers[freelancer.user_id] = freelancer
        print(f"Freelancer {freelancer.name} registered")

    def register_client(self, client):
        self.clients[client.user_id] = client
        print(f"Client {client.name} registered")

    def add_project(self, project):
        self.projects[project.project_id] = project
        project.client.post_project(project)
        print(f"Project '{project.title}' added")

    def assign_project(self, project_id, freelancer_id):
        if project_id in self.projects and freelancer_id in self.freelancers:
            project = self.projects[project_id]
            freelancer = self.freelancers[freelancer_id]
            project.assign_freelancer(freelancer)
            print(f"Project '{project.title}' assigned to {freelancer.name}")
        else:
            print("Invalid project ID or freelancer ID")

    def process_payment(self, project_id):
        if project_id in self.projects:
            project = self.projects[project_id]
            if project.status == "Completed" and project.freelancer:
                project.freelancer.receive_payment(project.budget)
                print(f"Payment of {project.budget} sent to {project.freelancer.name}")
            else:
                print("Project not completed or freelancer not assigned")
        else:
            print("Project not found")

    def show_projects(self):
        for project in self.projects.values():
            print(project)