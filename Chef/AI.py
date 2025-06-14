from decouple import config
from langchain.prompts import PromptTemplate
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

def ask_chef_ai(prompt: str) -> str:
	# Get the API key from the environment
	api_key = config("HUGGINGFACE_API_KEY")

	template = """<s>[INST]Your name is 'Master chef'. You are a chef who only creates delicious recipes. 
		You are given a prompt to create a recipe. You need to create a recipe based on the prompt.
		If any prompt is not related to the any recipe, you must need to ignore it.
		Even you must not give a hint about the prompt.
		</s>{question}[/INST]"""
	
	prompt_template = PromptTemplate.from_template(template)
	formatted_prompt_template = prompt_template.format(
		question = prompt
	)

	
	repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
	llm = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = api_key)

	response = llm.invoke(formatted_prompt_template)
	return response

