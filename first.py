class Attachee:
    """Class representing an intern/attachee at the tech innovation hub."""
    
    def __init__(self, name, division):
        """Initialize an attachee with a name and division."""
        self.name = name
        self.division = division
        self.tasks = []  # List to store assigned tasks
        self.feedback = {}  # Dictionary to store feedback for each task
        self.scores = {}  # Dictionary to store scores for each task
        self.average_score = 0  # Track average score
    
    def assign_task(self, task):
        """Assign a task to the attachee."""
        self.tasks.append(task)
        self.feedback[task] = ""
        self.scores[task] = 0
        return f"Task '{task}' assigned to {self.name} in {self.division} division."
    
    def add_feedback(self, task, feedback):
        """Add feedback for a specific task."""
        if task in self.tasks:
            self.feedback[task] = feedback
            return f"Feedback added for {self.name}'s task: '{task}'"
        else:
            return f"Error: Task '{task}' not assigned to {self.name}."
    
    def add_score(self, task, score):
        """Add a score for a specific task."""
        if task in self.tasks:
            if 0 <= score <= 10:
                self.scores[task] = score
                self._update_average_score()
                return f"Score of {score}/10 added for {self.name}'s task: '{task}'"
            else:
                return "Error: Score must be between 0 and 10."
        else:
            return f"Error: Task '{task}' not assigned to {self.name}."
    
    def _update_average_score(self):
        """Update the average score based on all task scores."""
        if self.scores:
            self.average_score = sum(self.scores.values()) / len(self.scores)
        else:
            self.average_score = 0
    
    def get_performance_summary(self):
        """Get a summary of the attachee's performance."""
        summary = f"\n--- {self.name}'s Performance Summary ({self.division} Division) ---\n"
        
        if not self.tasks:
            summary += "No tasks assigned yet.\n"
            return summary
        
        summary += f"Average Score: {self.average_score:.1f}/10\n"
        summary += "Tasks:\n"
        
        for task in self.tasks:
            summary += f"  - {task}\n"
            summary += f"    Score: {self.scores[task]}/10\n"
            summary += f"    Feedback: {self.feedback[task] if self.feedback[task] else 'No feedback yet'}\n"
        
        return summary


class TechHub:
    """Class representing the Tech Innovation Hub with all divisions."""
    
    def __init__(self):
        """Initialize the Tech Hub with empty divisions."""
        # The four key divisions in the hub
        self.divisions = ["Engineering", "Tech Programs", "Radio Support", "Hub Support"]
        self.attachees = []  # List to store all attachees
    
    def add_attachee(self, name, division):
        """Add a new attachee to the specified division."""
        if division in self.divisions:
            attachee = Attachee(name, division)
            self.attachees.append(attachee)
            return f"{name} added to {division} division."
        else:
            return f"Error: {division} is not a valid division."
    
    def get_attachee(self, name):
        """Get an attachee by name."""
        for attachee in self.attachees:
            if attachee.name.lower() == name.lower():
                return attachee
        return None
    
    def get_attachees_by_division(self, division):
        """Get all attachees in a specific division."""
        if division in self.divisions:
            return [a for a in self.attachees if a.division == division]
        else:
            return []
    
    def assign_task_by_division(self, division, task):
        """Assign a task to all attachees in a division."""
        if division in self.divisions:
            attachees = self.get_attachees_by_division(division)
            if attachees:
                for attachee in attachees:
                    attachee.assign_task(task)
                return f"Task '{task}' assigned to all attachees in {division} division."
            else:
                return f"No attachees found in {division} division."
        else:
            return f"Error: {division} is not a valid division."
    
    def display_division_performance(self, division):
        """Display performance of all attachees in a division."""
        if division in self.divisions:
            attachees = self.get_attachees_by_division(division)
            if attachees:
                result = f"\n=== {division} Division Performance ===\n"
                for attachee in attachees:
                    result += attachee.get_performance_summary()
                return result
            else:
                return f"No attachees found in {division} division."
        else:
            return f"Error: {division} is not a valid division."
    
    def display_all_attachees(self):
        """Display all attachees grouped by division."""
        result = "\n=== All Attachees by Division ===\n"
        
        for division in self.divisions:
            result += f"\n{division} Division:\n"
            attachees = self.get_attachees_by_division(division)
            
            if attachees:
                for i, attachee in enumerate(attachees, 1):
                    result += f"  {i}. {attachee.name} - Avg Score: {attachee.average_score:.1f}/10\n"
            else:
                result += "  No attachees in this division.\n"
        
        return result

