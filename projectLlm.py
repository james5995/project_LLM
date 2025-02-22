# project_LLM.py

class DeveloperProfile:
    def __init__(self):
        self.name = "project_LLM"
        self.created_by = "james5995"
        self.past_projects = []
        self.skills = []

    def add_project(self, title, description, used_llm=False):
        project = {
            "title": title,
            "description": description,
            "used_llm": used_llm
        }
        self.past_projects.append(project)
        print(f"Added project: {title}")

    def add_skill(self, skill, expertise_level):
        skill_entry = {
            "skill": skill,
            "expertise_level": expertise_level
        }
        self.skills.append(skill_entry)
        print(f"Added skill: {skill} ({expertise_level})")

    def display_profile(self):
        print(f"\nDeveloper: {self.name}")
        print(f"Created by: {self.created_by}")
        
        print("\nPast Projects:")
        for project in self.past_projects:
            llm_note = " (Used LLM)" if project["used_llm"] else ""
            print(f"- {project['title']}{llm_note}: {project['description']}")
        
        print("\nSkills:")
        for skill in self.skills:
            print(f"- {skill['skill']}: {skill['expertise_level']}")

# Create and populate profile
if __name__ == "__main__":
    profile = DeveloperProfile()

    # Adding past projects
    profile.add_project(
        "Chatbot Assistant",
        "Built an AI-powered conversational agent for customer support",
        used_llm=True
    )
    profile.add_project(
        "Web Scraper",
        "Created a tool to extract data from websites efficiently"
    )

    # Adding skills
    profile.add_skill("Natural Language Processing", "Expert")
    profile.add_skill("Python Programming", "Advanced")
    profile.add_skill("Web Analysis", "Advanced")

    # Display the profile
    profile.display_profile()
