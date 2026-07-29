import re


class IdeaParser:

    def parse(self, ideas):

        projects = []

        ideas = ideas.replace("**", "")

        sections = re.split(
            r"Project Title:",
            ideas,
            flags=re.IGNORECASE
        )

        field_map = {
            "Problem Solved": "problem_solved",
            "Novelty": "novelty",
            "Suggested Dataset": "suggested_dataset",
            "Tech Stack": "tech_stack",
            "Difficulty": "difficulty",
            "Resume Impact": "resume_impact_score",
            "Resume Impact Score": "resume_impact_score",
            "Research Potential": "research_potential_score",
            "Research Potential Score": "research_potential_score",
        }

        for section in sections[1:]:

            section = section.strip()

            if not section:
                continue

            project = {}

            lines = section.splitlines()

            project["title"] = lines[0].strip()

            for field, key in field_map.items():

                pattern = rf"{re.escape(field)}:\s*(.*?)\s*(?=\n[A-Za-z][A-Za-z ]*:\s|\Z)"

                match = re.search(
                    pattern,
                    section,
                    re.DOTALL | re.IGNORECASE
                )

                if match:
                    value = match.group(1).strip()

                    # Collapse multiple blank lines
                    value = re.sub(r"\n\s*\n", "\n", value)

                    project[key] = value

                else:
                    project[key] = ""

            projects.append(project)

        return projects 