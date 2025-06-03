import os
import yaml
import base64
from dotenv import load_dotenv

# Activate virtual environment manually if needed
venv_path = os.path.join(os.path.dirname(__file__), ".venv")
activate_venv = os.path.join(venv_path, "Scripts", "activate_this.py")

if os.path.exists(activate_venv):
    exec(open(activate_venv).read(), {'__file__': activate_venv})

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.tools import (
    ExtractIngredientsTool, 
    FilterIngredientsTool, 
    DietaryFilterTool,
    NutrientAnalysisTool
)
from src.models import RecipeSuggestionOutput, NutrientAnalysisOutput 
from io import BytesIO

# Load environment variables from .venv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".venv", ".env"))

WATSONX_API_KEY = os.getenv('WATSONX_API_KEY')
WATSONX_URL = os.getenv('WATSONX_URL')
WATSONX_PROJECT_ID = os.getenv('WATSONX_PROJECT_ID')

# Get the absolute path to the config directory
CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")

@CrewBase
class BaseNutriCoachCrew:
    agents_config_path = os.path.join(CONFIG_DIR, 'agents.yaml')
    tasks_config_path = os.path.join(CONFIG_DIR, 'tasks.yaml')

    def __init__(self, image_data, dietary_restrictions: str = None):
        self.image_data = image_data
        self.dietary_restrictions = dietary_restrictions

        with open(self.agents_config_path, 'r') as f:
            self.agents_config = yaml.safe_load(f)
        
        with open(self.tasks_config_path, 'r') as f:
            self.tasks_config = yaml.safe_load(f)